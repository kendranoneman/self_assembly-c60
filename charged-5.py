import hoomd, hoomd.md
import hoomd.deprecated as d
import numpy.random as rand
import sys
import helpers

maxT=1e8
dcdPeriod=1e6
msdPeriod=1e5
pppmGrid=64
pppmOrder=6
rcut=2.5
dt=0.001

mix,q,e,T,nr,cc_eps=helpers.get_params(int(sys.argv[1]))
jobname = helpers.make_name(mix,q,e,T,nr,cc_eps)
mfile,ifile,tfile,efile,lfile= helpers.make_filenames(jobname)

hoomd.context.initialize()
uc = hoomd.lattice.unitcell(N=2, #two types of particles 
            a1=[3,0,0],          #unit cell axes
            a2=[0,3,0,],
            a3=[0,0,3],
            dimensions=3,
            position=[[0,0,0],[0,1.5,0]], #xyz coords of the N particles
            type_name=['R','C'],
            mass=[1.022222,1.0], 
            diameter = [0.1,1.0], #Just the diameter we draw, not the one we use
            moment_inertia=[[5.047,5.303,5.300],[0,0,0]], #new and improved moments
            orientation=[[1,0,0,0],[1,0,0,0]])
s = hoomd.init.create_lattice(unitcell=uc,n=[nr,nr,nr])
s.particles.types.add('A') 
s.particles.types.add('B') 
rigid=hoomd.md.constrain.rigid() 
### CHARGES
rigid.set_param('R',types=['A','B'],positions=[[-0.0104,0.,0.],[0.4673,0.,0.]],diameters=[1.0,.272],charges=[-1.257,1.257]) #proper dipole moment
rigid.create_bodies() 
nl = hoomd.md.nlist.tree()
lj = hoomd.md.pair.lj(r_cut=rcut,nlist=nl)
lj.set_params(mode='xplor') #Interactions
lj.pair_coeff.set('A','A',epsilon=1.0,sigma=1.0)
lj.pair_coeff.set('B','B',epsilon=0.06,sigma=.272) #little oxygens
lj.pair_coeff.set('C','C',epsilon=cc_eps,sigma=cc_eps)
lj.pair_coeff.set('R',['R','A','B','C'],epsilon=0.0,sigma=0.0) #rigid points
lj.pair_coeff.set('B',['A','C'],epsilon=0.25,sigma=.636) #oxygen with fullerene
lj.pair_coeff.set('A','C',epsilon=1.0,sigma=1.0)
char = hoomd.group.charged()
nonrigid = group.nonrigid()
pppm = hoomd.md.charge.pppm(group=char,nlist=nl)
pppm.set_params(Nx=pppmGrid,Ny=pppmGrid,Nz=pppmGrid,order=pppmOrder,rcut=rcut)
hoomd.md.integrate.mode_standard(dt=dt)
ta=hoomd.group.type(name='as',type='A')
tb=hoomd.group.type(name='bs',type='B')
tc=hoomd.group.type(name='cs',type='C')

#potential energy v. time 
logger = hoomd.analyze.log(filename=lfile, quantities=['potential_energy', 'pppm_energy'], period=1e3, header_prefix='#', overwrite=True)

rigid = hoomd.group.rigid_center()
a=d.analyze.msd(filename=mfile,groups=[ta,tb,tc,rigid],period=msdPeriod,overwrite=True)
hoomd.md.integrate.langevin(group=hoomd.group.union(name='all',a=rigid,b=hoomd.group.type('C')),kT=T,seed=rand.randint(2**32)) ###
d.dump.xml(group=hoomd.group.all(),filename=ifile,vis=True, inertia=True,orientation=True,constraint=True)
hoomd.dump.dcd(group=hoomd.group.all(),filename=tfile,overwrite=True,period=dcdPeriod)
hoomd.run(maxT)
d.dump.xml(group=hoomd.group.all(),filename=efile,vis=True, inertia=True,orientation=True,constraint=True)
