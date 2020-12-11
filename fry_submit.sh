#!/bin/bash -l
#SBATCH -p nvlink
#SBATCH -J C60
#SBATCH -o /home/kendranoneman/fullerenes/outputfiles/C60.o%j
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mail-type=all
#SBATCH --mail-user=kendranoneman@u.boisestate.edu
#SBATCH -t 24:00:00

on-conda
source activate py3.5.3

python charged-6.py $1

#cp files you'd like to move off of scratch
#mv files that you'd like moved off of scratch
