import sys
import random
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 502)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Кнопка"))


class Solution(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setupUi(self)
        self.circles = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Git и желтые окружности")
        self.pushButton.clicked.connect(self.clicked)

    def paintEvent(self, a0):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)

        for x, y, r, color in self.circles:
            qp.setBrush(color)
            qp.drawEllipse(x, y, 2 * r, 2 * r)

        # Завершаем рисование
        qp.end()

    def clicked(self):
        r = random.randint(10, min(self.width(), self.height()) // 2)
        x = random.randint(0, self.width() - r * 2)
        y = random.randint(0, self.height() - r * 2)
        self.circles.append(
            (
                x,
                y,
                r,
                QColor(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )
        )
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Solution()
    ex.show()
    sys.exit(app.exec())
