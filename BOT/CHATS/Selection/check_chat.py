import pyrogram.types

from BOT.CHATS.Create_DB.DB_chats import set_chat_db
from BOT.CHATS.Create_DB.DB_history import set_message_db
from BOT.Utils.Time import get_time
from BOT.configure import ECHO_CHATS


def get_check_chat(client, id : int, keys):

    info_chat = client.get_chat(chat_id=id)
    if info_chat.members_count < 1000:
        return False

    if not info_chat.type == "channel":
        return False


    # перевод в Unix time
    last_time = get_time(mounth = 2)
    # Unix time в обычный формат
    # last_datetime = datetime.fromtimestamp(last_time)

    run = True
    _offset = 0
    pull_message = pyrogram.types.List()

    while (run):
        try:
            _msg = client.get_history(chat_id=id, limit=200, offset=_offset)
            pull_message.extend(_msg)
            if _msg[-1].date < last_time:
                run = False
            else:
                _offset += 200
        except Exception:
            run = False
            print("Закончил RUN")

    if len(pull_message) < 2:
        return False
    elif (len(pull_message) > 200):
        start = len(pull_message) - 200
    else:
        start = 0

    delete_from_number = -1
    for _ in range(start, len(pull_message)):
        if pull_message[_].date < last_time:
            delete_from_number = _
            break

    max_views = 0
    for _ in pull_message:
        try:
            if max_views < _.views:
                max_views = _.views
        except Exception:
            print("Какая-то ошибка в сравнении просмотров")

    print(f" {delete_from_number=}")
    if not delete_from_number == -1:
        pull_message = pull_message[:delete_from_number]

    print(f"Count pull message: {len(pull_message)}")


    set_message_db(pull_message, info_chat)
    set_chat_db(client, info_chat, max_views)
    ECHO_CHATS.append(info_chat.id)

    print(ECHO_CHATS)

    return True