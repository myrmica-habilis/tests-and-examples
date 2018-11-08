#!/usr/bin/env python
# vim: set fileencoding=utf-8

# https://www.root.cz/clanky/nastaveni-stylu-vykreslovani-widgetu-oken-i-dialogu-v-knihovne-pyside/#k06

import sys, functools

# import "jádra" frameworku Qt i modulu pro GUI
from PySide2 import QtWidgets, QtCore, QtGui

# nový widget bude odvozen od obecného widgetu
class MainWindowContent(QtWidgets.QWidget):

    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindowContent, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):

        # tlačítka, na které je navázán handler
        quitButton = self.prepareQuitButton()
        openFileButton = self.prepareOpenFileButton()
        colorDialogButton = self.prepareColorDialogButton()
        messageBoxButton = self.prepareMessageBoxButton()

        # vytvoření testovacích widgetů vkládaných do okna
        tree = self.prepareTree()
        slider = self.prepareSlider()
        lineEdit = self.prepareLineEdit()
        textEdit = self.prepareTextEdit()
        dial = self.prepareDial()

        # různě ostylovaná návěští
        testLabel1 = QtWidgets.QLabel("Normal/Default")
        testLabel2 = QtWidgets.QLabel("Box")
        testLabel3 = QtWidgets.QLabel("Panel")
        testLabel4 = QtWidgets.QLabel("Win Panel")
        testLabel5 = QtWidgets.QLabel("HLine")
        testLabel6 = QtWidgets.QLabel("VLine")
        testLabel7 = QtWidgets.QLabel("StyledPanel")

        testLabel2.setFrameStyle(QtWidgets.QFrame.Box)
        testLabel3.setFrameStyle(QtWidgets.QFrame.Panel)
        testLabel4.setFrameStyle(QtWidgets.QFrame.WinPanel)
        testLabel5.setFrameStyle(QtWidgets.QFrame.HLine)
        testLabel6.setFrameStyle(QtWidgets.QFrame.VLine)
        testLabel7.setFrameStyle(QtWidgets.QFrame.StyledPanel)

        # testovací přepínací tlačítka
        testRadioButton1 = QtWidgets.QRadioButton("radio button #1")
        testRadioButton2 = QtWidgets.QRadioButton("radio button #2")
        testRadioButton3 = QtWidgets.QRadioButton("radio button #3")

        # testovací zaškrtávací tlačítka
        testCheckBox1 = QtWidgets.QCheckBox("check box 1")
        testCheckBox2 = QtWidgets.QCheckBox("check box 2")

        # které tlačítko bude vybráno
        testRadioButton3.setChecked(True)
        testCheckBox2.setChecked(True)

        # vytvoření správců geometrie
        topLayout = QtWidgets.QHBoxLayout()
        leftLayout = QtWidgets.QVBoxLayout()
        centerLayout = QtWidgets.QVBoxLayout()
        rightLayout = QtWidgets.QVBoxLayout()

        # umístění widgetů do okna - levý sloupec
        leftLayout.addWidget(tree)
        leftLayout.addWidget(slider)

        # umístění widgetů do okna - prostřední sloupec
        centerLayout.addWidget(lineEdit)
        centerLayout.addWidget(textEdit)
        centerLayout.addWidget(openFileButton)
        centerLayout.addWidget(colorDialogButton)
        centerLayout.addWidget(messageBoxButton)
        centerLayout.addWidget(quitButton)

        # umístění widgetů do okna - pravý sloupec
        rightLayout.addWidget(testRadioButton1)
        rightLayout.addWidget(testRadioButton2)
        rightLayout.addWidget(testRadioButton3)
        rightLayout.addWidget(testCheckBox1)
        rightLayout.addWidget(testCheckBox2)

        rightLayout.addWidget(testLabel1)
        rightLayout.addWidget(testLabel2)
        rightLayout.addWidget(testLabel3)
        rightLayout.addWidget(testLabel4)
        rightLayout.addWidget(testLabel5)
        rightLayout.addWidget(testLabel6)
        rightLayout.addWidget(testLabel7)
        rightLayout.addWidget(dial)

        # umístění layoutů do hlavního layoutu
        topLayout.addLayout(leftLayout)
        topLayout.addLayout(centerLayout)
        topLayout.addLayout(rightLayout)

        # nastavení správce geometrie a vložení všech komponent do okna
        self.setLayout(topLayout)

    def prepareOpenFileButton(self):
        # tlačítko
        openFileButton = QtWidgets.QPushButton('Open file...', self)
        openFileButton.resize(openFileButton.sizeHint())

        # navázání akce na signál
        openFileButton.clicked.connect(self.showOpenFileDialog)
        return openFileButton

    def prepareMessageBoxButton(self):
        # tlačítko
        messageBoxButton = QtWidgets.QPushButton('Message Box', self)
        messageBoxButton.resize(messageBoxButton.sizeHint())

        # navázání akce na signál
        messageBoxButton.clicked.connect(self.showCustomMessageBox)
        return messageBoxButton

    def prepareLineEdit(self):
        # jednořádkové vstupní textové pole
        lineEdit = QtWidgets.QLineEdit(self)
        # naplnění textového pole textem
        lineEdit.setText(u"příliš žluťoučký kůň úpěl ďábelské ódy")
        return lineEdit

    def prepareTextEdit(self):
        # víceřádkové vstupní textové pole
        textEdit = QtWidgets.QTextEdit(self)

        # nastavení základních vlastností textového pole
        textEdit.setAcceptRichText(False)
        textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        # vložení obsahu souboru do víceřádkového textového pole
        try:
            with open("01_empty_window.py", "r", encoding="utf-8") as fin:
                content = fin.read()
                textEdit.insertPlainText(content)
        except:
            pass

        return textEdit

    def prepareColorDialogButton(self):
        # tlačítko s popisem
        colorDialogButton = QtWidgets.QPushButton('Select color', self)
        colorDialogButton.resize(colorDialogButton.sizeHint())

        # navázání akce na signál
        colorDialogButton.clicked.connect(self.showColorDialog)
        return colorDialogButton

    def prepareQuitButton(self):
        # tlačítko s popisem
        quitButton = QtWidgets.QPushButton('Quit', self)
        quitButton.resize(quitButton.sizeHint())

        # navázání akce na signál
        quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        return quitButton

    def showOpenFileDialog(self):
        # handler po stlačení tlačítka "Open file..."
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", u".")

        self.showMessageBox(u'Vybraný soubor\n{f}'.format(f=fileName))

    def showColorDialog(self):
        # handler po stlačení tlačítka "Select color"
        colorDialog = QtWidgets.QColorDialog()
        colorDialog.setCurrentColor(QtGui.QColor("#aabbcc"))
        result = colorDialog.exec_()

        selected = colorDialog.selectedColor()
        message = "Selected color: {r} {g} {b}\nClicked on: {c}".format(
            r=selected.red(),
            g=selected.green(),
            b=selected.blue(),
            c="Ok" if result == 1 else "Cancel")

        self.showMessageBox(message)

    def showMessageBox(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.exec_()

    def showCustomMessageBox(self):
        # handler po stlačení tlačítka "Message Box"
        # vytvoření dialogu
        msgBox = QtWidgets.QMessageBox()

        # nastavení zprávy a ikony, která se má zobrazit vedle zprávy
        msgBox.setText(u'Zpráva')
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)

        # nastavení tlačítek, které mají být součástí dialogu
        msgBox.addButton("Help", QtWidgets.QMessageBox.HelpRole)
        msgBox.addButton("Accept", QtWidgets.QMessageBox.AcceptRole)
        msgBox.addButton("Reject", QtWidgets.QMessageBox.RejectRole)

        # zobrazení dialogu
        msgBox.exec_()

    def prepareTree(self):
        # vytvoření stromu
        tree = QtWidgets.QTreeWidget(self)
        tree.setHeaderLabel("strom")
        tree.setColumnCount(1)

        # naplnění stromu daty
        items = []
        for i in range(1, 11):
            item = QtWidgets.QTreeWidgetItem(None, ["prvek #{i}".format(i=i)])
            items.append(item)
            QtWidgets.QTreeWidgetItem(item, ["podprvek A"])
            QtWidgets.QTreeWidgetItem(item, ["podprvek B"])
            QtWidgets.QTreeWidgetItem(item, ["podprvek C"])
        tree.insertTopLevelItems(0, items)

        # po vložení všech prvků do stromu je můžeme rozbalit
        skip = False
        for item in items:
            if not skip:
                item.setExpanded(True)
            skip = not skip

        return tree

    def prepareSlider(self):
        # vytvoření slideru
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)

        return slider

    def prepareDial(self):
        # vytvoření widgetu
        dial = QtWidgets.QDial()

        return dial

# nový widget bude odvozen od obecného hlavního okna
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        # zavoláme konstruktor předka
        super(MainWindow, self).__init__()

        # konfigurace GUI + přidání widgetu do okna
        self.prepareGUI()

    def prepareGUI(self):
        # velikost není potřeba specifikovat
        # self.resize(320, 240)
        self.setWindowTitle("Styles")

        # hlavní menu
        menubar = self.menuBar()

        # příkaz File/Quit
        fileQuitItem = QtWidgets.QAction(QtGui.QIcon('icons/application-exit.png'),
                                     '&Quit', self)
        fileQuitItem.triggered.connect(self.close)
        fileQuitItem.setStatusTip('Quit the application')
        fileQuitItem.setShortcut('Ctrl+Q')

        # položka File v hlavním menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(fileQuitItem)

        # položka Style v hlavním menu
        styleMenu = menubar.addMenu('&Style')

        # jednotlivé položky menu s nabízenými styly
        for key in QtWidgets.QStyleFactory.keys():
            styleMenuItem = QtWidgets.QAction(key, self)
            styleMenuItem.triggered.connect(functools.partial(self.setStyle, key))    # funguje
            # styleMenuItem.triggered.connect(lambda key=key: self.setStyle(key))     # nefunguje
            styleMenu.addAction(styleMenuItem)

        # tlačítko Quit
        quitAction = QtWidgets.QAction(QtGui.QIcon('icons/application-exit.png'),
                                   '&Quit', self)
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip('Quit the application')

        # tlačítko About
        aboutAction = QtWidgets.QAction(QtGui.QIcon('icons/dialog-information.png'),
                                    '&About', self)
        aboutAction.triggered.connect(self.aboutDialog)
        aboutAction.setStatusTip('About this application')

        # nástrojový pruh
        self.toolbar = self.addToolBar('title')

        # přidání tlačítek na nástrojový pruh
        self.toolbar.addAction(quitAction)
        self.toolbar.addAction(aboutAction)

        # vložení komponenty do okna
        self.setCentralWidget(MainWindowContent())

    def setStyle(self, styleName):
        # nastavení vybraného stylu
        QtWidgets.QApplication.setStyle(styleName)

    def aboutDialog(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText('About:\n...\n...\n...')
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.exec_()

    def run(self, app):
        # zobrazení okna na obrazovce
        self.show()
        # vstup do smyčky událostí (event loop)
        app.exec_()

def main():
    #QtGui.QApplication.setStyle("plastique")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow().run(app)

if __name__ == '__main__':
    main()
