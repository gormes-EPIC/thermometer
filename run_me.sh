#!/bin/bash

# Set variables
REPO_DIR="/home/pi/thermometer"
PYTHON_FILE="controller.py"  # or whatever your script is

# Go to repo
cd "$REPO_DIR" || exit

# Pull latest changes
git pull origin main  # or whatever your default branch is

# Activate virtual environment if needed
# source venv/bin/activate

# Run the Python file
python3 "$PYTHON_FILE"
