from PyQt5.QtWidgets import QApplication
from UI.custom.get_require_and_start import MainWindow
import sys
import threading
def loop():
    application = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(application.exec_())

if __name__ == '__main__':
    from HANDLERS import app
    t = threading.Thread(target=loop, args=())
    t.start()
    app.run()

