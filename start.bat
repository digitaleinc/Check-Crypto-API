@echo off
@title Check-Crypto-API by A.K.

rem Change directory to the script's directory
cd %~dp0

rem Activate the virtual environment
call venv\Scripts\activate.bat

rem Run your Python script
python main.py

rem Deactivate the virtual environment
call venv\Scripts\deactivate.bat

echo.
echo Thanks for using Check-Crypto-API by A.K.
echo.

pause