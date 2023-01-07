# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2 as db

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(808, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InOfficeLabel = QtWidgets.QLabel(self.centralwidget)
        self.InOfficeLabel.setGeometry(QtCore.QRect(110, 0, 67, 17))
        self.InOfficeLabel.setObjectName("InOfficeLabel")
        self.SickLabel = QtWidgets.QLabel(self.centralwidget)
        self.SickLabel.setGeometry(QtCore.QRect(370, 0, 67, 17))
        self.SickLabel.setObjectName("SickLabel")
        self.VacationLabel = QtWidgets.QLabel(self.centralwidget)
        self.VacationLabel.setGeometry(QtCore.QRect(610, 0, 67, 17))
        self.VacationLabel.setObjectName("VacationLabel")
        self.UnosSatiGroupView = QtWidgets.QGroupBox(self.centralwidget)
        self.UnosSatiGroupView.setEnabled(False)
        self.UnosSatiGroupView.setGeometry(QtCore.QRect(10, 280, 391, 111))
        self.UnosSatiGroupView.setObjectName("UnosSatiGroupView")
        self.UnesiSateButton = QtWidgets.QPushButton(self.UnosSatiGroupView)
        self.UnesiSateButton.setGeometry(QtCore.QRect(140, 80, 89, 25))
        self.UnesiSateButton.setObjectName("UnesiSateButton")
        self.splitter_3 = QtWidgets.QSplitter(self.UnosSatiGroupView)
        self.splitter_3.setGeometry(QtCore.QRect(20, 40, 167, 26))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.DatumLabel = QtWidgets.QLabel(self.splitter_3)
        self.DatumLabel.setObjectName("DatumLabel")
        self.DatumdateEdit = QtWidgets.QDateEdit(self.splitter_3)
        self.DatumdateEdit.setObjectName("DatumdateEdit")
        self.splitter_4 = QtWidgets.QSplitter(self.UnosSatiGroupView)
        self.splitter_4.setGeometry(QtCore.QRect(200, 40, 170, 26))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.SatiLabel = QtWidgets.QLabel(self.splitter_4)
        self.SatiLabel.setObjectName("SatiLabel")
        self.SatiSpinBox = QtWidgets.QDoubleSpinBox(self.splitter_4)
        self.SatiSpinBox.setObjectName("SatiSpinBox")
        self.BolovanjeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BolovanjeGroupBox.setEnabled(False)
        self.BolovanjeGroupBox.setGeometry(QtCore.QRect(430, 220, 341, 111))
        self.BolovanjeGroupBox.setObjectName("BolovanjeGroupBox")
        self.UnesiBolovanjeButton = QtWidgets.QPushButton(self.BolovanjeGroupBox)
        self.UnesiBolovanjeButton.setGeometry(QtCore.QRect(100, 70, 131, 25))
        self.UnesiBolovanjeButton.setObjectName("UnesiBolovanjeButton")
        
        self.UnesiBolovanjeButton.clicked.connect(self.unesiBolovanje)

        self.splitter_6 = QtWidgets.QSplitter(self.BolovanjeGroupBox)
        self.splitter_6.setGeometry(QtCore.QRect(10, 30, 142, 26))
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.BolovanjeOdLabel = QtWidgets.QLabel(self.splitter_6)
        self.BolovanjeOdLabel.setObjectName("BolovanjeOdLabel")
        self.BolovanjeOdDate = QtWidgets.QDateEdit(self.splitter_6)
        self.BolovanjeOdDate.setObjectName("BolovanjeOdDate")
        self.splitter_7 = QtWidgets.QSplitter(self.BolovanjeGroupBox)
        self.splitter_7.setGeometry(QtCore.QRect(170, 30, 141, 26))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.BolovanjeDoLabel = QtWidgets.QLabel(self.splitter_7)
        self.BolovanjeDoLabel.setObjectName("BolovanjeDoLabel")
        self.BolovanjeDoDate = QtWidgets.QDateEdit(self.splitter_7)
        self.BolovanjeDoDate.setObjectName("BolovanjeDoDate")
        self.GodisnjiGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GodisnjiGroupBox.setEnabled(False)
        self.GodisnjiGroupBox.setGeometry(QtCore.QRect(430, 350, 341, 111))
        self.GodisnjiGroupBox.setObjectName("GodisnjiGroupBox")
        self.UnesiGodisnjiButton = QtWidgets.QPushButton(self.GodisnjiGroupBox)
        self.UnesiGodisnjiButton.setGeometry(QtCore.QRect(110, 70, 111, 25))
        self.UnesiGodisnjiButton.setObjectName("UnesiGodisnjiButton")
        self.splitter_8 = QtWidgets.QSplitter(self.GodisnjiGroupBox)
        self.splitter_8.setGeometry(QtCore.QRect(10, 30, 142, 26))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.GodisnjiOdDateLabel = QtWidgets.QLabel(self.splitter_8)
        self.GodisnjiOdDateLabel.setObjectName("GodisnjiOdDateLabel")
        self.GodisnjiOdDate = QtWidgets.QDateEdit(self.splitter_8)
        self.GodisnjiOdDate.setObjectName("GodisnjiOdDate")
        self.splitter_9 = QtWidgets.QSplitter(self.GodisnjiGroupBox)
        self.splitter_9.setGeometry(QtCore.QRect(170, 30, 141, 26))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.GodisnjiDoDateLabel = QtWidgets.QLabel(self.splitter_9)
        self.GodisnjiDoDateLabel.setObjectName("GodisnjiDoDateLabel")
        self.GodisnjiDoDate = QtWidgets.QDateEdit(self.splitter_9)
        self.GodisnjiDoDate.setObjectName("GodisnjiDoDate")
        self.LoginGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.LoginGroupBox.setGeometry(QtCore.QRect(20, 410, 321, 131))
        self.LoginGroupBox.setObjectName("LoginGroupBox")
        self.usernameField = QtWidgets.QLineEdit(self.LoginGroupBox)
        self.usernameField.setGeometry(QtCore.QRect(90, 30, 113, 25))
        self.usernameField.setInputMask("")
        self.usernameField.setText("")
        self.usernameField.setObjectName("usernameField")
        self.passwordField = QtWidgets.QLineEdit(self.LoginGroupBox)
        self.passwordField.setGeometry(QtCore.QRect(90, 60, 113, 25))
        self.passwordField.setInputMask("")
        self.passwordField.setText("")
        self.passwordField.setObjectName("passwordField")
        self.LoginButton = QtWidgets.QPushButton(self.LoginGroupBox)
        self.LoginButton.setGeometry(QtCore.QRect(100, 90, 89, 25))
        self.LoginButton.setObjectName("LoginButton")
########################################################################################3333
        self.LoginButton.clicked.connect(self.login)

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 768, 192))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.InOfficeListWidget = QtWidgets.QListWidget(self.splitter)
        self.InOfficeListWidget.setEnabled(False)
        self.InOfficeListWidget.setObjectName("InOfficeListWidget")
        self.SickListWidget = QtWidgets.QListWidget(self.splitter)
        self.SickListWidget.setEnabled(False)
        self.SickListWidget.setObjectName("SickListWidget")
        self.VacationListWidget = QtWidgets.QListWidget(self.splitter)
        self.VacationListWidget.setEnabled(False)
        self.VacationListWidget.setObjectName("VacationListWidget")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 220, 167, 17))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.UkupnoSatiLabel = QtWidgets.QLabel(self.splitter_2)
        self.UkupnoSatiLabel.setObjectName("UkupnoSatiLabel")
        self.BrojSatiLabel = QtWidgets.QLabel(self.splitter_2)
        self.BrojSatiLabel.setObjectName("BrojSatiLabel")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setGeometry(QtCore.QRect(20, 240, 79, 17))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.ZaIsplatuLabel = QtWidgets.QLabel(self.splitter_5)
        self.ZaIsplatuLabel.setObjectName("ZaIsplatuLabel")
        self.BrojZaIsplatuLabel = QtWidgets.QLabel(self.splitter_5)
        self.BrojZaIsplatuLabel.setObjectName("BrojZaIsplatuLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InOfficeLabel.setText(_translate("MainWindow", "In Office"))
        self.SickLabel.setText(_translate("MainWindow", "Sick"))
        self.VacationLabel.setText(_translate("MainWindow", "Vacation"))
        self.UnosSatiGroupView.setTitle(_translate("MainWindow", "Unesi sate"))
        self.UnesiSateButton.setText(_translate("MainWindow", "Unesi sate"))
        self.DatumLabel.setText(_translate("MainWindow", "Datum:"))
        self.SatiLabel.setText(_translate("MainWindow", "Odrađeno sati:"))
        self.BolovanjeGroupBox.setTitle(_translate("MainWindow", "Unesi bolovanje"))
        self.UnesiBolovanjeButton.setText(_translate("MainWindow", "Unesi bolovanje"))
        self.BolovanjeOdLabel.setText(_translate("MainWindow", "Od:"))
        self.BolovanjeDoLabel.setText(_translate("MainWindow", "Do:"))
        self.GodisnjiGroupBox.setTitle(_translate("MainWindow", "Unesi godisnji"))
        self.UnesiGodisnjiButton.setText(_translate("MainWindow", "Unesi godisnji"))
        self.GodisnjiOdDateLabel.setText(_translate("MainWindow", "Od:"))
        self.GodisnjiDoDateLabel.setText(_translate("MainWindow", "Do:"))
        self.LoginGroupBox.setTitle(_translate("MainWindow", "Login"))
        self.usernameField.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordField.setPlaceholderText(_translate("MainWindow", "Password"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.UkupnoSatiLabel.setText(_translate("MainWindow", "Ukupno odrađeno sati: "))
        self.BrojSatiLabel.setText(_translate("MainWindow", "0"))
        self.ZaIsplatuLabel.setText(_translate("MainWindow", "Za isplatu:"))
        self.BrojZaIsplatuLabel.setText(_translate("MainWindow", "0"))

    def executeQuery(self, query):
        conn = db.connect(database='postgres', user='postgres', password = 'postgres', host='127.0.0.1', port='5432')
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    
    def executeQueryInsert(self, query):
        conn = db.connect(database='postgres', user='postgres', password = 'postgres', host='127.0.0.1', port='5432')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Inserted")
        return 

    def login(self):
        username = self.usernameField.text()
        password = self.passwordField.text()
        result = self.executeQuery("""select ime_i_prezime, lozinka from zaposlenik where ime_i_prezime = '{0}' and lozinka = '{1}';""".
        format(username, password))

        print(result)
        if result is not None and result[0][0] == username and result[0][1]:
            self.unlockApp()


    def clearQuerryResult(self, querryResult):
    
        cleared = []
        for x in querryResult:
            for y in x:
                cleared.append(y)
        return cleared

    def populateListViews(self):
        self.InOfficeListWidget.clear()
        self.SickListWidget.clear()
        self.VacationListWidget.clear()

        inoffice = self.executeQuery("select ime_i_prezime from zaposlenik where idstatus = 1;")
        InOffice = self.clearQuerryResult(inoffice)
        sick = self.executeQuery('select ime_i_prezime from zaposlenik where idstatus = 4;')
        Sick = self.clearQuerryResult(sick)
        vacation = self.executeQuery("select ime_i_prezime from zaposlenik where idstatus = 3;")
        Vacation = self.clearQuerryResult(vacation)
        self.InOfficeListWidget.addItems(InOffice)
        self.SickListWidget.addItems(Sick)
        self.VacationListWidget.addItems(Vacation)


    def unlockApp(self):
        self.LoginGroupBox.setEnabled(0)
        self.GodisnjiGroupBox.setEnabled(1)
        self.BolovanjeGroupBox.setEnabled(1)
        self.UnosSatiGroupView.setEnabled(1)
        self.populateListViews()

    def unesiBolovanje(self):
        datumOd = (self.BolovanjeOdDate.date().toPyDate()).strftime("%d-%m-%Y")
        datumDo = self.BolovanjeDoDate.date().toPyDate().strftime("%d-%m-%Y")

        getUserID = self.executeQuery("select zaposlenikid from zaposlenik where ime_i_prezime = '{}';".format(self.usernameField.text()))
        userID = getUserID[0][0]
        result = self.executeQueryInsert("insert into bolovanje (zaposlenikid, pocetak, kraj) values ({0}, '{1}'::DATE,'{2}'::DATE);".
        format(userID, datumOd, datumDo))
        print(result)

        self.populateListViews()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
