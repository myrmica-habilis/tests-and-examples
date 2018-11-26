from PySide2 import QtWidgets

class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.entry_date = QtWidgets.QDateEdit()
        self.entry_time = QtWidgets.QTimeEdit()
        self.button = QtWidgets.QPushButton("Print")
        self.button.clicked.connect(self.print_out)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.entry_date)
        layout.addWidget(self.entry_time)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def print_out(self):
        print(self.entry_date.date().toString("yyyy"))
        print(self.entry_date.date().toString("MM"))
        print(self.entry_date.date().toString("dd"))
        print(self.entry_time.time().toString("hh"))
        print(self.entry_time.time().toString("mm"))
        print(self.entry_time.time().toString("ss"))

    def run(self, app):
        self.show()
        app.exec_()

def main():
    app = QtWidgets.QApplication()
    MainWidget().run(app)

if __name__ == '__main__':
    main()
