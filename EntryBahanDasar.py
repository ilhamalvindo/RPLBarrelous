from PyQt6 import QtCore, QtWidgets
from PyQt6.QtSql import QSqlDatabase
import sys
# import psycopg2
import requests

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 24, 24))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.button = QtWidgets.QPushButton("Inset Data", Dialog)
        self.button.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button.clicked.connect(self.InsertData)
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 150, 22))
        self.lineEdit.setPlaceholderText("Input ID")
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 100, 150, 22))
        self.lineEdit_2.setPlaceholderText("Input nama bahan dasar")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 150, 150, 22))
        self.lineEdit_3.setPlaceholderText("Input kuantitas")
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 91, 16))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 130, 16))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 91, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Entry Bahan Dasar"))
        self.label.setText(_translate("Dialog", "ID Bahan Dasar"))
        self.label_2.setText(_translate("Dialog", "Nama Bahan Dasar"))
        self.label_3.setText(_translate("Dialog", "Kuantitas"))



    def InsertData(self):

        url = 'http://localhost:8000/bahan-dasar'

        body = {
            "id": self.lineEdit.text(),
            "nama": self.lineEdit_2.text(),
            "kuantitas": self.lineEdit_3.text()
            }

        try :
            requests.post(url, json=body)
            QtWidgets.QMessageBox.about(self, 'Connection', 'success')

        except :
            QtWidgets.QMessageBox.about(self, 'Connection', "Failed")
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

# Database test