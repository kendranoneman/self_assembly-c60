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

mix,q,e,T,nr,c_eps=helpers.get_params(int(sys.argv[1]))
jobname = helpers.make_name(mix,q,e,T,nr,c_eps)
mfile,ifile,tfile,efile,lfile= helpers.make_filenames(jobname)
hoomd.context.initialize()
d.init.read_xml(filename='restart.xml')
rigid=hoomd.md.constrain.rigid() 
### CHARGES
nl = hoomd.md.nlist.tree()
lj = hoomd.md.pair.lj(r_cut=rcut,nlist=nl)
lj.set_params(mode='xplor') #TODO:Interactions
lj.pair_coeff.set('A','A',epsilon=1.0,sigma=1.0)
lj.pair_coeff.set('A','B',epsilon=1.0,sigma=.7) #was 0.5
lj.pair_coeff.set('B','B',epsilon=1.0,sigma=.4)
lj.pair_coeff.set('R',['R','A','B','C'],epsilon=0.0,sigma=0.0)
lj.pair_coeff.set('A','C',epsilon=1.0,sigma=1.0)
lj.pair_coeff.set('B','C',epsilon=1.0,sigma=1.0)
lj.pair_coeff.set('C','C',epsilon=c_eps,sigma=1.0)
char = hoomd.group.charged()
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
