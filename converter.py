from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def __init__(self):
        self.files = None
        self.about = None
        self.jpg = None
        self.png = None
        self.select = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 305)
        MainWindow.setFixedSize(299, 305)
        MainWindow.setWindowIcon(QtGui.QIcon('converter.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {background-color: rgb(20, 20, 40);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 241, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.select = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select.sizePolicy().hasHeightForWidth())
        self.select.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.select.setFont(font)
        self.select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select.setStyleSheet("color: rgb(57, 9, 130);")
        self.select.setObjectName("select")
        self.verticalLayout.addWidget(self.select)
        self.png = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.png.sizePolicy().hasHeightForWidth())
        self.png.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.png.setFont(font)
        self.png.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.png.setStyleSheet("color: rgb(57, 9, 130);")
        self.png.setObjectName("png")
        self.verticalLayout.addWidget(self.png)
        self.jpg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jpg.sizePolicy().hasHeightForWidth())
        self.jpg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.jpg.setFont(font)
        self.jpg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.jpg.setStyleSheet("color: rgb(57, 9, 130);")
        self.jpg.setObjectName("jpg")
        self.verticalLayout.addWidget(self.jpg)
        self.about = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.about.setFont(font)
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about.setStyleSheet("QPushButton {\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(0, 0, 127);\n"
                                  "border: 0 solid black;\n"
                                  "border-radius: 5px;\n"
                                  "padding: 5px 0;}\n"
                                  "QPushButton:hover {\n"
                                  "background-color: rgb(0, 0, 100);\n"
                                  "border: 1 solid #0000ff;}")
        self.about.setObjectName("about")
        self.verticalLayout.addWidget(self.about)
        self.files = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.files.setStyleSheet("color: rgb(255, 255, 255);\nmargin-top: 5px;")
        self.files.setAlignment(QtCore.Qt.AlignCenter)
        self.files.setObjectName("files")
        self.verticalLayout.addWidget(self.files)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter"))
        self.select.setText(_translate("MainWindow", "Select WebP Images"))
        self.png.setText(_translate("MainWindow", "Convert to PNG"))
        self.jpg.setText(_translate("MainWindow", "Convert to JPG"))
        self.about.setText(_translate("MainWindow", "ABOUT"))
        self.files.setText(_translate("MainWindow", "Files selected: [0]"))
