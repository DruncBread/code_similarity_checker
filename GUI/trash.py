from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 417)
        MainWindow.setMaximumSize(QtCore.QSize(1500, 870))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.btn_get_file1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_file1.setGeometry(QtCore.QRect(650, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_get_file1.setFont(font)
        self.btn_get_file1.setObjectName("get_file1")
        self.gridLayout.addWidget(self.btn_get_file1, 1, 2, 1, 1)

        self.file_path1 = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path1.setGeometry(QtCore.QRect(20, 40, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_path1.setFont(font)
        self.file_path1.setReadOnly(True)
        self.file_path1.setObjectName("file_path1")
        self.gridLayout.addWidget(self.file_path1, 0, 1, 1, 2)

        self.btn_get_file2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_file2.setGeometry(QtCore.QRect(650, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_get_file2.setFont(font)
        self.btn_get_file2.setObjectName("get_file2")
        self.gridLayout.addWidget(self.btn_get_file2, 4, 2, 1, 1)

        self.file_path2 = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path2.setGeometry(QtCore.QRect(20, 200, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_path2.setFont(font)
        self.file_path2.setReadOnly(True)
        self.file_path2.setObjectName("file_path2")
        self.gridLayout.addWidget(self.file_path2, 3, 1, 1, 2)

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(1000, 1000, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_submit.setFont(font)
        self.btn_submit.setObjectName("submit")
        self.gridLayout.addWidget(self.btn_submit, 4, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Code Similarity Checker"))
        self.btn_get_file1.setText(_translate("MainWindow", "Choose file"))
        self.btn_get_file2.setText(_translate("MainWindow", "Choose file"))
        self.file_path1.setText("file path 1")
        self.label.setText(_translate("MainWindow", "Choose .py file 1"))
        self.label_2.setText(_translate("MainWindow", "Choose .py file 2"))
        self.label_3.setText(_translate("MainWindow", "                                                             \n"
                                                      "               "))
        self.label_4.setText(_translate("MainWindow", "      "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
