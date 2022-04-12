from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

from BOT.CHATS.Create_DB.DB_chats import path_photo_template
from BOT.configure import app, ECHO_CHATS
from UI.template.template_main_menu import Ui_MainWindow
from UI.template.template_start_menu import Ui_StartWindow
from PyQt5.QtGui import QPixmap

import sqlite3 as sql
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.can_close = True
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self.Window)
        self.ui.pushButton.clicked.connect(lambda: self.get_requre())
        self.Window.show()
        self.position_group = 0
        self.Chats_ID = list()
        self.res_bd = list()

    def show_window_2(self):
        pass
        # self.Window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self.Window)
        # self.ui.pushButton_7.clicked.connect(lambda: self.get_top_10_UI())
        # self.ui.pushButton_8.clicked.connect(lambda: self.get_realtime())
        # self.ui.pushButton_9.clicked.connect(lambda: self.get_top_user())
        # self.ui.pushButton_10.clicked.connect(lambda: self.get_top_user_UI_please())
        # self.ui.pushButton_11.clicked.connect(lambda: self.get_info_list_please())
        # self.ui.pushButton_13.clicked.connect(lambda: self.get_info(1))
        # self.ui.pushButton_14.clicked.connect(lambda: self.get_info(-1))
        # self.ui.pushButton_12.clicked.connect(lambda: self.show_list_exit())
        # self.ui.pushButton_12.clicked.connect(lambda: self.show_list_exit())
        # self.ui.pushButton_16.clicked.connect(lambda: self.show_list_start())
        # self.ui.pushButton_15.clicked.connect(lambda: self.exit_and_delete())
        # self.Window.show()


    def get_requre(self):
        from BOT.HANDLERS import app
        from BOT.configure import req_chat

        requre = self.ui.lineEdit_2.text()
        keys = self.ui.lineEdit_3.text()
        if len(requre) == 0:
            self.can_close = False
        else:
            self.can_close = True
        if self.can_close:
            result_text = requre + " | " + keys
            app.send_message(chat_id="@Echooechobot", text = result_text)
            print(requre)
            print(keys)
            self.show_window_2()
            # self.StartWindow.close()
            print("here")
            app.send_message(chat_id=req_chat, text=result_text)


    def get_top_10_UI(self, top=10, hour=24):
        self.ui.stackedWidget.setCurrentIndex(0)
        con = sql.connect('BOT_DB.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM MESSAGES WHERE date > (?) ORDER BY views DESC LIMIT (?)""", (hour, top))
        records = cur.fetchall()
        con.commit()
        for _ in records:
            name_view = f'<html><head/><body><p><span style=" font-style:italic;"> from </span><span style=" font-weight:600;">{_[1]}</span></body></html>'
            view_date = (f'<html><head/><body><p>                                                                  view: <span style=" font-weight:600;">{_[3]}</span> date: <span style=" text-decoration: underline;">{datetime.utcfromtimestamp(_[4]).strftime("%Y-%m-%d %H:%M:%S")}</span></p></body></html>')

            self.ui.textBrowser.append(name_view)
            self.ui.textBrowser.append(view_date)

            try:
                msg = app.get_messages(_[0], _[2])
                text_message = msg.text
                self.ui.textBrowser.append(text_message)
            except Exception:
                text_message = "No text"
                self.ui.textBrowser.append(text_message)

            self.ui.textBrowser.append("\n\n\n")

    def get_realtime(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        con = sql.connect('BOT_DB.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM MESSAGES ORDER BY date DESC LIMIT 30""")
        records = cur.fetchall()
        con.commit()
        for _ in records:
            name_view = f'<html><head/><body><p><span style=" font-style:italic;"> from </span><span style=" font-weight:600;">{_[1]}</span></body></html>'
            view_date = (
                f'<html><head/><body><p>                                                                  view: <span style=" font-weight:600;">{_[3]}</span> date: <span style=" text-decoration: underline;">{datetime.utcfromtimestamp(_[4]).strftime("%Y-%m-%d %H:%M:%S")}</span></p></body></html>')

            self.ui.textBrowser_2.append(name_view)
            self.ui.textBrowser_2.append(view_date)

            try:
                msg = app.get_messages(_[0], _[2])
                text_message = msg.text
                if msg.text == None:
                    text_message = "No text"
                self.ui.textBrowser_2.append(text_message)
            except Exception:
                text_message = "No text"
                self.ui.textBrowser_2.append(text_message)

            self.ui.textBrowser_2.append("\n\n\n")

    def get_top_user(self):
        self.ui.stackedWidget.setCurrentIndex(2)



    def get_top_user_UI_please(self):

        top = int(self.ui.lineEdit.text())
        hour = int(self.ui.lineEdit_2.text())
        print(top)
        print(hour)
        con = sql.connect('BOT_DB.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM MESSAGES WHERE date > (?) ORDER BY views DESC LIMIT (?)""", (hour, top))
        records = cur.fetchall()
        con.commit()
        for _ in records:

            name_view = f'<html><head/><body><p><span style=" font-style:italic;"> from </span><span style=" font-weight:600;">{_[1]}</span></body></html>'
            view_date = (
                f'<html><head/><body><p>                                                                  view: <span style=" font-weight:600;">{_[3]}</span> date: <span style=" text-decoration: underline;">{datetime.utcfromtimestamp(_[4]).strftime("%Y-%m-%d %H:%M:%S")}</span></p></body></html>')

            self.ui.textBrowser_3.append(name_view)
            self.ui.textBrowser_3.append(view_date)

            try:
                msg = app.get_messages(_[0], _[2])
                text_message = msg.text
                self.ui.textBrowser_3.append(text_message)
            except Exception:
                text_message = "No text"
                self.ui.textBrowser_3.append(text_message)

            self.ui.textBrowser_3.append("\n\n\n")

    def get_info_list_please(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        con = sql.connect('BOT_DB.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM CHATS""")
        records = cur.fetchall()
        con.commit()
        for _ in records:
            self.Chats_ID.append(int(_[0]))
        self.res_bd = records
        print(records)


    def get_info(self, index : int):

        temp_groups = self.Chats_ID
        print(self.Chats_ID)
        if (len(temp_groups) > 0):
            self.position_group += index
            if (self.position_group < 0):
                self.position_group = len(temp_groups) + index
            if (self.position_group == len(temp_groups)):
                self.position_group = 0
            print("Прошло")
            temp_groups_requre = temp_groups[self.position_group]

            index_res = 0
            for _ in self.res_bd:
                if (_[0] == temp_groups_requre):
                    break
                else:
                    index_res += 1

            records = self.res_bd[index_res]
            if (records[5] == -1):
                pin_mg = "Нет"
            else:
                pin_mg = "Есть"
            temp_info = f'<html><head/><body><p><span style="font-weight:600;">Название канала: {records[1]} </span></p>\n'
            text_info = (f'<html><head/><body><p><span style=" font-weight:600;">Название:</span> {records[1]}</p>'
                        f'<p><span style=" font-weight:600;">Кол-во участников: </span>{records[2]}</p>'
                        f'<p><span style=" font-weight:600;">Описание:</span> {records[4]}</p>'
                         f'<p><span style=" font-weight:600;">Закрепленное сообщение: </span>{pin_mg}</p>'
                         f'<p><span style=" font-weight:600;">Макс. просмотры:</span> {records[6]}</p></body></html>')
            self.ui.label_14.setText(text_info)
            pix_map = QPixmap(str(path_photo_template + records[3]))
            print(pix_map)
            self.ui.label_15.setPixmap(pix_map)
        else:
            pass
            self.ui.label_14.setText(str("Вы не подписаны на группы"))

    def show_list_exit(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def show_list_start(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def exit_and_delete(self):
        con = sql.connect('BOT_DB.db')
        cur = con.cursor()
        cur.execute("""SELECT chat_id FROM CHATS""")
        records = cur.fetchall()
        con.commit()
        b = len(records)
        for _ in records:
            b -= 1
            try:
                app.leave_chat(int(_[0]), delete=True)
                print("отписка")
            except Exception:
                print("Ошибка отписки")
        if (b == 0):
            print("goodbue")
            self.ui.close()
            app.stop()

