#!/bin/bash -l
#PBS -q normal
#PBS -N mixPar
#PBS -j oe 
#PBS -l walltime=48:00:00,nodes=10:ppn=16:xk
#PBS -m abe 
#PBS -M ericjankowski@boisestate.edu 

#Load the hoomd module
module load hoomd/v2.1.6

#Change into the directory that you're going to work in 
#cd /mnt/b/projects/eot/bacx/kendra/fullerenes
cd /mnt/b/projects/eot/bacx/eric/fullerenes

#Run your job script
#aprun -n 1 -N 1 -d 16 python uncharged.py ${NAME} ${T} ${N}
aprun -n 1 -N 1 -d 16 python charged-5.py  300 &
aprun -n 1 -N 1 -d 16 python charged-5.py  301 &
aprun -n 1 -N 1 -d 16 python charged-5.py  302 &
aprun -n 1 -N 1 -d 16 python charged-5.py  303 &
aprun -n 1 -N 1 -d 16 python charged-5.py  304 &
aprun -n 1 -N 1 -d 16 python charged-5.py  305 &
aprun -n 1 -N 1 -d 16 python charged-5.py  306 &
aprun -n 1 -N 1 -d 16 python charged-5.py  307 &
aprun -n 1 -N 1 -d 16 python charged-5.py  308 &
aprun -n 1 -N 1 -d 16 python charged-5.py  309 &
wait
#aprun -n 1 -N 1 -d 16 python charged-1.py   8
