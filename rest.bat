@echo off

for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo Current time is %mydate%:%mytime% >> rest.log

start cmd /k "Scripts\activate && python stretch-break-verses.py

