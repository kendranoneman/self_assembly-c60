#!/bin/bash -l
#SBATCH -p gpuq
#SBATCH -J C60
#SBATCH -o outfiles/C60.o%j
#SBATCH -n 8
#SBATCH --mail-type=all
#SBATCH --mail-user=kendranoneman@u.boisestate.edu
#SBATCH -t 24:00:00
#SBATCH --gres=gpu:1

module use /home/knoneman/software/lib/python/hoomd/
module purge
module load hoomd-blue/intel/mvapich2/2.1.5

python charged-6.py $1
#cp files you'd like to move off of scratch
#mv files that you'd like moved off of scratch
