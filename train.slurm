#!/bin/bash
#SBATCH --job-name=train_model 
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=3
#SBATCH --gres=gpu:v100:1
#SBATCH --time=5:00:00
#SBATCH --mem=20GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=yf1451@nyu.edu
#SBATCH --output=train_RoBERTa_Twitter_Bert-base-NER.out
#SBATCH --error=train_RoBERTa_Twitter_Bert-base-NER.err


singularity exec --nv\
         --overlay /scratch/yf1451/NLU_Final/overlay-25GB-500K.ext3:ro \
        /scratch/work/public/singularity/cuda11.2.2-cudnn8-devel-ubuntu20.04.sif \
        /bin/bash -c "source /ext3/env.sh ; conda activate base; cd /scratch/yf1451/NLU_Final/Corsair/code;
        python _main.py 
        " 
