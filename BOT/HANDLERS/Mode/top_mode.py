import sqlite3 as sql

from pyrogram import filters

from BOT.Utils.Time import get_time
from BOT.configure import app, ECHO_CHATS

@app.on_message(filters.command("top"))
def send_post(client, message):
    top = 10
    hour = get_time(hour=24)
    if len(message.command) > 1:
        top = int(message.command[1])
        hour = get_time(hour = int(message.command[2]))

    print(message)
    con = sql.connect('BOT_DB.db')
    cur = con.cursor()
    cur.execute("""SELECT * FROM MESSAGES WHERE date > (?) ORDER BY views DESC LIMIT (?)""", (hour, top))
    records = cur.fetchall()
    print(records)
    con.commit()
