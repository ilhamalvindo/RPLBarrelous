# Form implementation generated from reading ui file 'databebanui.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import requests


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 434)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 40, 49, 16))
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 170, 22))
        self.lineEdit.setPlaceholderText("Input ID")
        self.lineEdit.setObjectName("lineEdit")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 170, 16))
        self.label_2.setObjectName("label_2")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 110, 170, 22))
        self.lineEdit_2.setPlaceholderText("Input Tanggal")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 170, 16))
        self.label_3.setObjectName("label_3")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 160, 170, 22))
        self.lineEdit_3.setPlaceholderText("Input Nama Data Beban")
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 210, 170, 22))
        self.lineEdit_4.setPlaceholderText("Input Harga")
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 170, 16))
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 260, 170, 22))
        self.lineEdit_5.setPlaceholderText("Input Kuantitas")
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 240, 170, 16))
        self.label_5.setObjectName("label_5")
        
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 310, 170, 22))
        self.lineEdit_6.setPlaceholderText("Input Satuan")
        self.lineEdit_6.setObjectName("lineEdit_6")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 170, 16))
        self.label_6.setObjectName("label_6")
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 21, 24))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 360, 241, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.InsertData)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def InsertData(self):

        url = 'http://localhost:8000/dataBeban'

        body = {
            "idBeban": self.lineEdit.text(),
            "tanggal": self.lineEdit_2.text(),
            "namaBeban": self.lineEdit_3.text(),
            "harga": self.lineEdit_4.text(),
            "kuantitas": self.lineEdit_5.text(),
            "satuan": self.lineEdit_6.text()
            }

        try :
            requests.post(url, json=body)
            QtWidgets.QMessageBox.about(self, 'Connection', 'success')

        except :
            QtWidgets.QMessageBox.about(self, 'Connection', "Failed")
            self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ID Beban"))
        self.label_2.setText(_translate("Dialog", "Tanggal"))
        self.label_3.setText(_translate("Dialog", "Nama Data Beban"))
        self.label_4.setText(_translate("Dialog", "Harga"))
        self.label_5.setText(_translate("Dialog", "Kuantitas"))
        self.label_6.setText(_translate("Dialog", "Satuan"))
        self.pushButton_2.setText(_translate("Dialog", "Insert Data Beban"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
