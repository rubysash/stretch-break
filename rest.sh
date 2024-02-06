#!/bin/bash

# Get the current username dynamically
CURRENT_USER=$(whoami)

# Export the DISPLAY variable
export DISPLAY=:0

# Optionally, set XDG_RUNTIME_DIR if needed (replace USERNAME with your actual username)
export XDG_RUNTIME_DIR=/run/user/$(id -u)

# Check if the user is logged in
if who | grep -q "^$CURRENT_USER "; then
  # User is logged in, run the script
  /home/james/v/python/stretch-break/bin/python3 /home/james/v/python/stretch-break/stretch-break-verses.py
fi

