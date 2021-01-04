# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'egitmen_guncelle_sil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 740, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(5, 110, 790, 431))
        self.tableWidget.setMaximumSize(QtCore.QSize(790, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(97)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eğitmen Güncelleme ve Silme Ekranı"))
        self.label.setText(_translate("Form", "Temel Eğitmen İşlemlerine Hoş Geldiniz"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Adı Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "TC No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Şifre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Telefon"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Adres"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Durumu"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

