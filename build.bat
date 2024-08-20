@echo off
REM Check if a virtual environment exists, and if not, create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate

REM Install Python dependencies from requirements.txt
if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo No requirements.txt file found. Skipping dependency installation.
)

REM Indicate that the build process is complete
echo Build complete.

@REM deactivate