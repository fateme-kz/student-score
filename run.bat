@echo off

REM Activate the virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate
call pip list

REM Run the main Python script
echo Running the application...
python app.py

REM Keep the command prompt open after the script finishes

