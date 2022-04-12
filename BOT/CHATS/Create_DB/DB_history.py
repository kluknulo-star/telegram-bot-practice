import sqlite3 as sql

def set_message_db(messages, info_chat):
    con = sql.connect('BOT_DB.db')
    cur = con.cursor()
    for _ in messages:
        cur.execute("""INSERT INTO MESSAGES VALUES (?,?,?,?,?)""", (info_chat.id, info_chat.title, _.message_id, _.views, _.date))
        con.commit()