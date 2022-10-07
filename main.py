import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui_main import Ui_MainWindow
from ui_SplashScreenCicle import Ui_SplashScreen
from circular_progress import CircularProgress

# Globals
counter = 0
# SplashScreen3
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # remove title and bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # import circular progress
        self.progress = CircularProgress()

        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 40
        self.progress.progress_width = 3
        self.progress.ad_shadow(True)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

    # add drop Shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        # QTaimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1)


        # show
        self.show()
    # update progress bar
    def update(self):
        global counter

        # set value to progress bar
        self.progress.set_Value(counter)

        # close sphash screen and open main app
        if counter >= 100:
            # stop time
            self.timer.stop()

            # show main app
            self.main = MainWindow()
            self.main.show()

            # drop sphash screen
            self.close()

        # interface countet
        counter += 1



# main window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # show window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
