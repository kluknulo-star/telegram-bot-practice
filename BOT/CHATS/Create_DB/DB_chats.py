import sqlite3 as sql
from BOT.configure import ECHO_CHATS
path_photo_template =  "C:\\Users\\Kirill\\PycharmProjects\\ParserStar\\BOT\\downloads\\"

def set_chat_db(client, info,max_views):

    try:
        photo_name = f"{info.username}_chat.jpg"
        client.download_media(message=info.photo.small_file_id, file_name=photo_name)
        # "D:\\ChocoWork\\University\\Practice\\user_bot\\downloads\\"
        path_photo = path_photo_template + photo_name
    except Exception:
        photo_name = "None"
        print("Нет аватарки")

    pin_message = info.pinned_message
    if pin_message == None:
        print("НЕТ закрепленного сообщения")
        pin_id = -1
    else:
        pin_id = pin_message.message_id
        print("ЕСТЬ закрепленное сообщение")

    print("Д А Н Н Ы Е  З А П И С А Н Ы  В  Б Д")

    con = sql.connect('BOT_DB.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO CHATS VALUES (?,?,?,?,?,?,?)""", (info.id, info.title, info.members_count, photo_name, info.description, pin_id, max_views))
    con.commit()
    return True