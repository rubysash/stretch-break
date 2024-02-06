# stretch-break

Very simple program to help me remember to stretch.  Requires cron, at, or taskscheduler for the heavy lifting.

## Word/Verse Configuration

- Make a backup of the file you want to edit (verses.json or words.json)
- Modify the file as you like, they are text/json

## Installation Windows

```
git clone git@github.com:rubysash/stretch-break.git
cd stretch-break
scripts\activate
python -m pip install pip --upgrade
python -m pip install -r requirements.txt
```
## Automation Windows

I've created the rest.bat that will both log the word/verse and start the venv

```
start cmd /k "Scripts\activate && python stretch-break-verses.py"
```

Use task scheduler in windows to schedule that bat file to run every 30 minutes when you are logged in.

## Installation Linux

```
git clone git@github.com:rubysash/stretch-break.git
python3 -m venv stretch-break
cd stretch-break
source bin/activate
python3 -m pip install pip --upgrade
python3 -m pip install -r requirements.txt
```

## Automation Linux

I've created the rest.sh script which will load the proper environment and run the script.

The rest.sh must be executable `chmod +x rest.sh`, adjust the path to your python3 for this venv and your script 

```
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
```

Use crontab -e to edit the schedule.   This is not designed to work in a multi-user environment.

Test your direct call first, and when it works without being in the environment, it should also work in cron.  You can use the `>> /path/to/log 2>&1` to investigate if it doesn't trigger as you expect.

Here is my 20 minute timer for cron that calls the script, which checks if i'm logged in, and only runs when I'm logged in:
```
*/20 * * * * /home/james/v/python/stretch-break/rest.sh >> /home/james/v/python/stretch-break/cronlog.log 2>&1
```

