#!/bin/bash

# create the environment files
conda list --explicit > conda_env.txt
conda env export > conda_env.yml

# Move these files into a env folder
mv conda_env.txt env/ && mv conda_env.yml env/