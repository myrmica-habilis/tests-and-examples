#!/usr/bin/python
# coding: utf-8

# via https://stackoverflow.com/questions/53100965

from PySide2 import QtWidgets
import time


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.resize(640, 400)

        lineEntry = QtWidgets.QLineEdit(time.strftime("%H:%M:%S",
                                                      time.localtime()))
        # default text does not dissappear upon mouse click

        lineEntry.setPlaceholderText(
                      "Enter a valid time in 24-hour hh:mm:ss format.")
        # placeholder text does not dissappear upon mouse click
        # (it disappears after typing the first char)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lineEntry)
        self.setLayout(layout)

    def run(self, app):
        self.show()
        app.exec_()


def main():
    app = QtWidgets.QApplication()
    appWindow = MainWindow()
    appWindow.run(app)


if __name__ == "__main__":
    main()
