# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eski_parklar.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 20, 740, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 790, 431))
        self.tableWidget.setMaximumSize(QtCore.QSize(790, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(97)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.toplu_sil_btn = QtWidgets.QPushButton(Form)
        self.toplu_sil_btn.setGeometry(QtCore.QRect(240, 520, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toplu_sil_btn.setFont(font)
        self.toplu_sil_btn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.toplu_sil_btn.setObjectName("toplu_sil_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eski Park Güncelleme ve Silme Ekranı"))
        self.label.setText(_translate("Form", "Eski Park İşlemlerine Hoş Geldiniz"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Plaka"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Park Giriş"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Park Çıkış"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Süre"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tutar"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Abone Bilgisi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Araç Bilgisi"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Zaman Bilgisi"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Park Durumu"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Sil"))
        self.toplu_sil_btn.setText(_translate("Form", "Toplu Silme Butonu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

