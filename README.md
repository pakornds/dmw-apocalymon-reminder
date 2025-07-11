# Discord Webhook Reminder

A Python script that sends reminder messages to Discord every 1.5 hours using webhooks.

## Features

- 🔔 Sends reminders every 1 hour and 30 minutes
- 📱 Beautiful Discord embed messages
- 📝 Logging to file and console
- 🧪 Webhook testing functionality
- ⏰ Timestamps on all messages

## Setup Instructions

### 1. Get Discord Webhook URL

1. Go to your Discord server
2. Right-click on the channel where you want reminders
3. Select "Edit Channel"
4. Go to "Integrations" tab
5. Click "Create Webhook"
6. Copy the webhook URL

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure the Script

1. Open `discord_reminder.py`
2. Replace `YOUR_DISCORD_WEBHOOK_URL_HERE` with your actual webhook URL:
   ```python
   WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
   ```

### 4. Run the Script

```powershell
python discord_reminder.py
```

## Usage

- The script will first test the webhook connection
- If successful, it will send an initial "system started" message
- Then it will send reminder messages every 90 minutes (1.5 hours)
- All activity is logged to `reminder.log`
- Press `Ctrl+C` to stop the reminder system

## Files

- `discord_reminder.py` - Main reminder script
- `requirements.txt` - Python dependencies
- `reminder.log` - Log file (created when script runs)

## Customization

You can customize the reminder message by modifying the `send_reminder()` method in the `DiscordReminder` class.

## Troubleshooting

- **Webhook test fails**: Check that your webhook URL is correct
- **Permission errors**: Make sure the webhook has permission to send messages to the channel
- **Import errors**: Run `pip install -r requirements.txt` to install dependencies
