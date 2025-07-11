@echo off
echo Installing Discord Reminder dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ✅ Dependencies installed successfully!
    echo.
    echo Next steps:
    echo 1. Edit config.json with your Discord webhook URL
    echo 2. Run: python discord_reminder.py
    echo    or double-click: run_reminder.bat
) else (
    echo.
    echo ❌ Failed to install dependencies
    echo Make sure you have Python and pip installed
)

pause
