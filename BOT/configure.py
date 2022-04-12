from pyrogram import Client

from Utils.Clean_db import last_session_story


with open('config.ini', 'r') as f:
    data = f.read().splitlines()
    donor = data[3].split(" = ")[1]  # список доноров
    moder = data[4].split(" = ")[1]  # модерация
    channel = data[5].split(" = ")[1]  # канал пересылки постов
    req_chat = int(data[6].split(" = ")[1])
    ECHO_CHATS = list()
    ECHO_CHATS.append(int(data[7].split(" = ")[1]))

ECHO_CHATS.append(-1001585200953) #kluknulo_main
last_session_story(True)
app = Client("my_account")