import requests

# Replace 'BOT_TOKEN' with your actual bot token
bot_token = 'BOT_TOKEN'
chat_id = 'USER_CHAT_ID'  # Replace with your chat ID - not the bot chat ID otherwise the bot will try to send a message to himself.

# URL for sending messages via the Telegram Bot API
api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Message you want to send
message_text = "Hello from your Telegram bot!"

# Parameters for the API request
params = {
    'chat_id': chat_id,
    'text': message_text
}

# Send the API request
response = requests.post(api_url, params=params)

# Check the response status
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Response code: {response.status_code}")
    print(response.text)
