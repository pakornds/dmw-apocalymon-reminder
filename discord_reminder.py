import requests
import time
import schedule
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reminder.log'),
        logging.StreamHandler()
    ]
)


class DiscordReminder:
    def __init__(self, webhook_url):
        """
        Initialize the Discord reminder with webhook URL

        Args:
            webhook_url (str): Discord webhook URL
        """
        self.webhook_url = webhook_url

    def send_reminder(self, message=None):
        """
        Send a reminder message to Discord

        Args:
            message (str): Custom message to send. If None, sends default reminder.
        """
        if message is None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"@everyone **Reminder!** - {current_time}\n\nThis is your scheduled reminder every 1.5 hours!"

        # Create the embed for a nicer looking message
        embed = {
            "title": "⏰ Scheduled Reminder",
            "description": message,
            "color": 0x00ff00,  # Green color
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {
                "text": "Discord Reminder Bot"
            }
        }

        payload = {
            "embeds": [embed]
        }

        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 204:
                logging.info("Reminder sent successfully!")
                return True
            else:
                logging.error(
                    f"Failed to send reminder. Status code: {response.status_code}")
                logging.error(f"Response: {response.text}")
                return False

        except requests.exceptions.RequestException as e:
            logging.error(f"Error sending reminder: {e}")
            return False

    def test_webhook(self):
        """
        Test the webhook connection
        """
        test_message = "🧪 **Test Message**\n\nWebhook is working correctly!"
        return self.send_reminder(test_message)


def load_config():
    """
    Load configuration from config.json file
    """
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("config.json file not found!")
        return None
    except json.JSONDecodeError:
        logging.error("Invalid JSON in config.json file!")
        return None


def main():
    # Load configuration
    config = load_config()
    if config is None:
        print("❌ Failed to load configuration!")
        return

    WEBHOOK_URL = config.get("webhook_url", "")
    REMINDER_INTERVAL = config.get("reminder_interval_minutes", 90)

    # Validate webhook URL
    if WEBHOOK_URL == "YOUR_DISCORD_WEBHOOK_URL_HERE" or not WEBHOOK_URL:
        print("❌ Please set your Discord webhook URL in config.json!")
        print("To get a webhook URL:")
        print("1. Go to your Discord server")
        print("2. Right-click on the channel where you want reminders")
        print("3. Select 'Edit Channel'")
        print("4. Go to 'Integrations' tab")
        print("5. Click 'Create Webhook'")
        print("6. Copy the webhook URL and update config.json")
        return

    # Create reminder instance
    reminder = DiscordReminder(WEBHOOK_URL)

    # Test the webhook first
    print("Testing webhook connection...")
    if not reminder.test_webhook():
        print("❌ Webhook test failed! Please check your webhook URL.")
        return

    print("✅ Webhook test successful!")

    # Schedule the reminder every 1.5 hours (configurable)
    schedule.every(REMINDER_INTERVAL).minutes.do(reminder.send_reminder)

    print("🚀 Discord reminder started!")
    print(
        f"📅 Sending reminders every {REMINDER_INTERVAL} minutes ({REMINDER_INTERVAL/60:.1f} hours)")
    print("📝 Logs are saved to 'reminder.log'")
    print("⏹️  Press Ctrl+C to stop")

    # Send initial reminder
    reminder.send_reminder(
        "🎉 **Reminder System Started!**\n\nYou will now receive reminders every 1.5 hours!")

    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info("Reminder system stopped by user")
        print("\n👋 Reminder system stopped!")


if __name__ == "__main__":
    main()
