# stretch-break

Very simple program to help me remember to stretch.  Requires cron, at, or taskscheduler for the heavy lifting.

# Instructions:

1. install the modules you need with 'pip install somemodule'
2. edit your words.json file, it must be valid json
3. save the script as stretch-break.py
4. create a .bat file with 1 line in it:  python stretch-break.py (or use my example)
5. copy font file into same location you save this file (arial.ttf)
6. test it from CLI:  python stretch-break.py, if it works great, else figure out why
7. Schedule task to run the bat file in windows task scheduler to run as you see fit (I run mine every 30 minutes all the time, except when logged out).

# Windows/Linux

It will work on Linux, but not as written.   I will need to add a switch to detect OS and not load the Win32 stuff.



