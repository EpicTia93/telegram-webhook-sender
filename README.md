# telegram-webhook-sender
This python snippet allows you to send a webhook from your telegram bot.

## Installation 
requests module is needed and not pre-installed so make sure you download it using the latest pip version with:
<pre>
    pip install requests
</pre>

## Usage
After downloading the "requests" module replace BOT_TOKEN in line 4 with your bot token and USER_CHAT_ID in line 5 with your own Chat ID which you can find using the bot @myidbot. 
After that navigate from cmd in the script directory and run the script to grab the Chat ID with:
<pre>
    python telegram_send.py
</pre>
