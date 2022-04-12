import time

from pyrogram import filters

from BOT.CHATS.Selection.check_chat import get_check_chat
from BOT.configure import app, req_chat, ECHO_CHATS

@app.on_message(filters.chat(req_chat))
def try_inline(client, message):
    #main_search - первые 15 инлайн запросов

    all_text = message.text.split(" ")
    search = ""
    keys = dict()
    bool_text = True
    for _ in all_text:
        if _ == '|':
            bool_text = False
            search = search[:-1]
            continue
        elif bool_text:
            search += _ + ' '
        else:
            keys[_] = 0

    print(search)
    print(keys)



    # Процесс поиска
    main_search = client.get_inline_bot_results("SearcheeBot", message.text)
    extended_search_bool = False
    if len(main_search.results) == 15:
        # main_search - 16-30 инлайн запрос передается со смещением 15
        extended_search = client.get_inline_bot_results("SearcheeBot", message.text, offset="15")
        size_res = len(main_search.results) + len(extended_search.results)
    else:
        size_res = len(main_search.results)

    try:
        # print(main_search.results[0].id)
        client.send_inline_bot_result(req_chat, main_search.query_id, main_search.results[0].id)
    except Exception as err:
        message.reply_text("No one result!")
        return

    for _ in range(len(main_search.results)):
        # ссылка на чат(для приватных)
        url_temp = main_search.results[_].send_message.reply_markup.rows[0].buttons[0].url
        temp, url = url_temp.split("://")
        url = "https://" + url

        #название канала
        description_temp = main_search.results[_].description
        description_list = description_temp.split(" ")
        description = description_list[0]

        if (description == "приватный"):
            try:
                print(f"Join PRIVATE channel {url}")
                chat = client.join_chat(url)
                print("Wait for 5 sec...")

                res = get_check_chat(client, chat.id, keys)
                time.sleep(10)
                if not res:
                    client.leave_chat(chat.id, True)
                print(f"Run away for PRIVATE channel {url}")

            except Exception as inst:
                print(f"Приватный   {Exception}")
        else:
            try:
                print(f"Join channel {description}")
                chat = client.join_chat(description)
                print("Wait for 5 sec...")
                res = get_check_chat(client, chat.id, keys)
                time.sleep(10)
                if not res:
                    client.leave_chat(chat.id, True)
                print(f"Run away for channel {description}")
            except Exception as inst:
                print(f"Обычный   {type(inst)}")
        print("-------------------------\n")


    # для расширенного поиска (выкл)
    # if (extended_search_bool):
    #     for _ in range(len(main_search.results)):
    #         # name_chat = main_search.results[_].
    #         url = main_search.results[_].send_message.reply_markup.rows[0].buttons[0].url
    #         description = main_search.results[_].description
    #         print(f"{url} | {description}")

