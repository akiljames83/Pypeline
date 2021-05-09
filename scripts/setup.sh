#!/bin/bash

# local constants
create_conda_env=false
powershell=false
bash=true
zsh=false

# create conda environment if not done already
if $create_conda_env ; then
    conda create --name pypeline_dev --file conda_env.txt python=3.9
    echo "Environment created..."
else
    echo "Environment not created..."
fi

# configure `conda activate` based on users shell
if $powershell ; then 
    conda init powershell
elif $bash ; then
    conda init bash
elif $zsh ; then
    conda init zsh
fi

# activate conda environment
conda activate pypeline_dev

# install package
echo "Installing the pypeline package..."
pip install -e .

echo "Done!"