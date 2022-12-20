import os.path
import sys
import random

from PyQt5 import QtMultimedia
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QPainter, QColor
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic


class Solution(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'UI.ui'), self)
        self.circles = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Git и желтые окружности")
        self.pushButton.clicked.connect(self.clicked)

    def paintEvent(self, a0):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))

        for x, y, r in self.circles:
            qp.drawEllipse(x, y, 2 * r, 2 * r)

        # Завершаем рисование
        qp.end()

    def clicked(self):
        r = random.randint(10, min(self.width(), self.height()) // 2)
        x = random.randint(0, self.width() - r * 2)
        y = random.randint(0, self.height() - r * 2)
        self.circles.append((x, y, r))
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Solution()
    ex.show()
    sys.exit(app.exec())
