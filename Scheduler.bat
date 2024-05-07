@echo off

rem Set the path to your Python interpreter
set PYTHON=python

rem Set the path to your requirements.txt file
set REQUIREMENTS=requirements.txt

rem Set the path to your main Python script
set MAIN=main.py

rem Set the name of your virtual environment
set VENV_NAME=myenv

rem Check if the virtual environment exists
if not exist %VENV_NAME% (
    rem Create the virtual environment
    %PYTHON% -m venv %VENV_NAME%
)

rem Activate the virtual environment
call %VENV_NAME%\Scripts\activate

rem Install required packages if not already installed
%PYTHON% -m pip install -r %REQUIREMENTS%

rem Run the main Python script
%PYTHON% %MAIN%

rem Deactivate the virtual environment
deactivate
