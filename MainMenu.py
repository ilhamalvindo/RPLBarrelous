# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuEntry_bahan_dasar = QtWidgets.QMenu(self.menubar)
        self.menuEntry_bahan_dasar.setObjectName("menuEntry_bahan_dasar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionEntry_Bahan_Dasar = QtGui.QAction(MainWindow)
        self.actionEntry_Bahan_Dasar.setObjectName("actionEntry_Bahan_Dasar")

        self.actionInput_Data_Beban = QtGui.QAction(MainWindow)
        self.actionInput_Data_Beban.setObjectName("actionInput_Data_Beban")

        self.menuEntry_bahan_dasar.addAction(self.actionEntry_Bahan_Dasar)
        self.menuEntry_bahan_dasar.addAction(self.actionInput_Data_Beban)
        self.menubar.addAction(self.menuEntry_bahan_dasar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEntry_bahan_dasar.setTitle(_translate("MainWindow", "Main Menu"))
        self.actionEntry_Bahan_Dasar.setText(_translate("MainWindow", "Entry Bahan Dasar"))
        self.actionInput_Data_Beban.setText(_translate("MainWindow", "Input Data Beban"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
