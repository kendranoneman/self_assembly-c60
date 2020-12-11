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
aprun -n 1 -N 1 -d 16 python charged-4.py  290 &
aprun -n 1 -N 1 -d 16 python charged-4.py  291 &
aprun -n 1 -N 1 -d 16 python charged-4.py  292 &
aprun -n 1 -N 1 -d 16 python charged-4.py  293 &
aprun -n 1 -N 1 -d 16 python charged-4.py  294 &
aprun -n 1 -N 1 -d 16 python charged-4.py  295 &
aprun -n 1 -N 1 -d 16 python charged-4.py  296 &
aprun -n 1 -N 1 -d 16 python charged-4.py  297 &
aprun -n 1 -N 1 -d 16 python charged-4.py  298 &
aprun -n 1 -N 1 -d 16 python charged-4.py  299 &
wait
#aprun -n 1 -N 1 -d 16 python charged-1.py   8
