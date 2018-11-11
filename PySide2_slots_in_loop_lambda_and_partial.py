from PySide2 import QtWidgets
import functools

class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        labelLambda = QtWidgets.QLabel("Slots connected using <b>lambda</b>:")
        layout.addWidget(labelLambda)

        for color in ["orange", "magenta", "blue"]:
            button = QtWidgets.QPushButton(color)
            button.clicked.connect(lambda *args, c=color: self.set_bg_color(c))
                # this lambda works
            # button.clicked.connect(lambda checked, c=color: self.set_bg_color(c))
                # this raises TypeError: <lambda>() missing 1 required positional argument: 'checked'
            layout.addWidget(button)

        horizLine = QtWidgets.QLabel()
        horizLine.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
        layout.addWidget(horizLine)

        labelPartial = QtWidgets.QLabel("Slots connected using <b>partial</b>:")
        layout.addWidget(labelPartial)

        for color in ["yellow", "gold", "silver"]:
            button = QtWidgets.QPushButton(color)
            button.clicked.connect(functools.partial(self.set_bg_color, color))
                # this works
            layout.addWidget(button)

        self.setLayout(layout)

    def set_bg_color(self, color):
        self.setStyleSheet("background: {}".format(color))

    def run(self, app):
        self.show()
        app.exec_()

def main():
    app = QtWidgets.QApplication()
    MainWidget().run(app)

if __name__ == '__main__':
    main()
