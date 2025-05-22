#!/bin/bash

# Set the directory where your repo should live
TARGET_DIR="/home/pi/thermometer"
REPO_URL="https://github.com/gormes-EPIC/thermometer.git"

# If the directory already exists, pull the latest changes
if [ -d "$TARGET_DIR/.git" ]; then
    echo "Pulling latest changes in $TARGET_DIR..."
    cd "$TARGET_DIR" && git pull
else
    echo "Cloning fresh repo into $TARGET_DIR..."
    git clone "$REPO_URL" "$TARGET_DIR"
fi
