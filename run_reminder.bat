@echo off
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting Discord Reminder...
python discord_reminder.py

pause
