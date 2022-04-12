import sqlite3 as sql

def last_session_story(clean : bool):
    if clean:
        try:
            con = sql.connect('BOT_DB.db')
            cur = con.cursor()
            cur.execute("""DROP TABLE CHATS""")
            con.commit()
            cur.execute("""DROP TABLE MESSAGES""")
            con.commit()
        except Exception:
            print("До этого ни разу не использовалась БД")

        try:
            con = sql.connect('BOT_DB.db')
            cur = con.cursor()
            cur.execute("""CREATE TABLE CHATS (chat_id INT, title VARCHAR, members INT, photo_name VARCHAR, description TEXT, pin_id INT, max_view INT)""")
            con.commit()
            cur.execute("""CREATE TABLE MESSAGES (chat_id INT, title VARCHAR, message_id INT, views INT, date INT)""")
            con.commit()
        except Exception:
            print("Что-то пошло не так с созданием полей БД")
