Scheduler bot

This bot is used to book tennis court reservations 

## Installation

- Only step is to install python from https://www.python.org/ftp/python/3.11.8/python-3.11.8-embed-amd64.zip
- run the python.exe file
- click yes to all it's prompts and install

## Usage

editor.bat is used to edit the time and venue the bot should target, simply run it and wait for the code to run in command prompt
- click the link and you'll be redirected to the edit page to change values

Scheduler.bat is used to run the code, don't run directly, instead add it to task scheduler
- open task scheduler
- click create basic task
- name it
- set trigger to weekly
- set the time you want it to run
- set the action to start a program
- set the program/script to the path of the Scheduler.bat file
- click finish

Congrats, now your bot will now always run at the time you set as long as you PC is on and you have stable internet