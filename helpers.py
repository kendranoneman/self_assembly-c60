import os
import numpy

def make_name(mix,q,e,T,N,cc_eps):
    return "mix{}-q{}-e{}-T{}-N{}-ccep{}".format(mix,q,e,T,N,cc_eps)

def checkdir(name):
    if not os.path.exists(name):
        os.makedirs(name)
    return

def get_params(i):
    line = numpy.loadtxt('params.txt')[i]
    print(line)
    mix = int(line[1])
    q = int(line[2])
    e = int(line[3])
    T = float(line[4])
    N = int(line[5])
    cc_eps = float(line[6])
    return mix,q,e,T,N,cc_eps

def make_filenames(jobname):
    m="runs/"+jobname+"/msd.log"
    i="runs/"+jobname+"/init.xml"
    t="runs/"+jobname+"/traj.dcd"
    e="runs/"+jobname+"/restart.xml"
    l="runs/"+jobname+"/log.log"
    checkdir("runs/"+jobname)
    return m,i,t,e,l

