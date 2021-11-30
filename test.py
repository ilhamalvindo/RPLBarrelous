import sys
from PyQt6 import QtCore, QtGui, QtWidgets


from PyQt6.QtSql import QSqlDatabase
import psycopg2

class Window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.title ="TEST"
        self.top =200
        self.left = 300
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.button = QtWidgets.QPushButton('DB Connetion', self)
        self.button.setGeometry(100,100,200,50)
        self.button.clicked.connect(self.DB)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



    def DB(self):
        try:
            conn = psycopg2.connect(host="localhost", user="postgres", password="vestionarmy73", database="rpl_db")
            QtWidgets.QMessageBox.about(self, 'Connection', "Database Connected")
        except:
            QtWidgets.QMessageBox.about(self, 'Connection', 'Database ga konek gan')
            sys.exit(1)


App = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())


# def InsertData(self):
        # QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
        # db.setHostName("localhost")
        # db.setDatabaseName("db_rpl")
        # db.setUserName("postgres")
        # db.setPassword("vestionarmy73")
        # db.port(5432)
        # db.setDatabaseName("db_rpl.psql")

        # conn = psycopg2.connect(host="localhost", user="postgres", password="vestionarmy73", database="rpl_db")
        
        # with conn:
            
        #     cur = conn.cursor()
        #     tabel = 'bahanDasar'
        #     cur.execute("INSERT INTO {}(namaBahan, kuantitas, satuan)".format(tabel) +
        #                 "VALUES ('%s', '%s', '%s')" % (''.join(self.lineEdit.text()), 
        #                                                 ''.join(self.lineEdit_2.text()),
        #                                                 ''.join(self.lineEdit_3.text())))
            
        #     QtWidgets.QMessageBox.about(self, 'Connection', 'Data inserted succesfully')
        #     self.close()