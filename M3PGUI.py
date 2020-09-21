# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M3PGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 461, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(480, 10, 271, 311))
        self.listView.setAutoFillBackground(False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setTextElideMode(QtCore.Qt.ElideNone)
        self.listView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listView.setObjectName("listView")
        self.pushButton_Analysis = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Analysis.setGeometry(QtCore.QRect(480, 330, 91, 41))
        self.pushButton_Analysis.setObjectName("pushButton_Analysis")
        self.pushButton_CutImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CutImage.setGeometry(QtCore.QRect(570, 330, 91, 41))
        self.pushButton_CutImage.setObjectName("pushButton_CutImage")
        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(660, 330, 91, 41))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 530, 731, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 380, 741, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 400, 731, 111))
        self.tabWidget.setObjectName("tabWidget")
        self.Log1 = QtWidgets.QWidget()
        self.Log1.setObjectName("Log1")
        self.textEdit = QtWidgets.QTextEdit(self.Log1)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 691, 71))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.Log1, "")
        self.Log2 = QtWidgets.QWidget()
        self.Log2.setObjectName("Log2")
        self.tabWidget.addTab(self.Log2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Analysis.setText(_translate("MainWindow", "Analysis"))
        self.pushButton_CutImage.setText(_translate("MainWindow", "Cut Image"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Log2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

