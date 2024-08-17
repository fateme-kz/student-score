@echo off
REM Navigate to the directory where this script is located
cd /d %~dp0

REM Activate the virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate

REM Run the main Python script
echo Running the application...
python server.py


REM Run the Flask application
python -m flask run

REM Keep the command prompt open after the script finishes
pause
