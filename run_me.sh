#!/bin/bash

# Set variables
REPO_DIR="/home/pi/thermometer"
PYTHON_FILE="controller.py"  

# Go to repo
cd "$REPO_DIR" || exit

# Pull latest changes
/usr/bin/git pull origin main 

# change the file to be executable
chmod 777 run_me.sh

# Run the Python file
python3 "$PYTHON_FILE"
