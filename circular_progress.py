from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # custom properti

        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0xFF79c6
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0xFF79c6


        # set default size without layout
        self.resize(self.width, self.height)

    # add dropshadow
    def ad_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    # set value
    def set_Value(self, value):
        self.value = value
        self.repaint()  # render progress bar after change value


    # paint evante (desingener your circulapar progress here)
    def paintEvent(self, event):
#################### Pen, set pen , draw e suas variates pra desenho #################################
        # set progress parametres
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # painter
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))


        # ceat rectangle
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # pen
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # set Pound Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # creat arc / circular progress
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)
#############################################################################
        # creat text
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")
        # end
        paint.end()