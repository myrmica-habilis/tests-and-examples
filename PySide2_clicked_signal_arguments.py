from PySide2 import QtWidgets


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        button = QtWidgets.QPushButton("Click to print info")
        button.setObjectName("My pushbutton")

        # this passes a boolean (checked state):
        button.clicked[bool].connect(self.print_info)

        # this passes no arguments:
        # button.clicked.connect(self.print_info)

        radioButton = QtWidgets.QRadioButton("Click to print info")
        radioButton.setObjectName("My radiobutton")

        # this passes a boolean (checked state):
        radioButton.clicked[bool].connect(self.print_info)

        # this passes no arguments:
        # radioButton.clicked.connect(self.print_info)

        checkbox = QtWidgets.QCheckBox("Click to print info")
        checkbox.setObjectName("My checkbox")

        # this passes a boolean (checked state):
        checkbox.clicked[bool].connect(self.print_info)

        # this passes no arguments:
        # checkbox.clicked.connect(self.print_info)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(radioButton)
        layout.addWidget(checkbox)
        self.setLayout(layout)

    def print_info(self, *args):
        print("Sender of the signal:", self.sender().objectName())
        print("Arguments:", args)

    def run(self, app):
        self.show()
        app.exec_()


def main():
    app = QtWidgets.QApplication()
    MainWidget().run(app)


if __name__ == '__main__':
    main()
