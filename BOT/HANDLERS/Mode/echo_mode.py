from pyrogram import filters

from BOT.configure import app, ECHO_CHATS


@app.on_message(filters.chat(ECHO_CHATS))
def send_post(client, message):
    print(message)
