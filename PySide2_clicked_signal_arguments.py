from PySide2 import QtWidgets

class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        button = QtWidgets.QPushButton("Click to print info")
        button.setObjectName("My pushbutton")
        button.clicked.connect(self.print_info)
        radioButton = QtWidgets.QRadioButton("Click to print info")
        radioButton.setObjectName("My radiobutton")
        radioButton.clicked.connect(self.print_info)
        checkbox = QtWidgets.QCheckBox("Click to print info")
        checkbox.setObjectName("My checkbox")
        checkbox.clicked.connect(self.print_info)

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
