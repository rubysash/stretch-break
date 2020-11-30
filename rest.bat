@echo off

for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%
echo Current time is %mydate%:%mytime% >> rest.log

C:\Python39\pythonw.exe stretch-break.py

