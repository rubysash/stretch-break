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

The rest.sh must be executable `chmod +x rest.sh`

```
bin/python3 stretch-break-verses.py
```

Use crontab -e to edit the schedule.   This is not designed to work in a multi-user environment.

Test your direct call first, and when it works without being in the environment, it shoudl also work in cron.

```
*/20 * * * * /home/james/v/python/stretch-break/rest.sh
```

