# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arac_islemler.ui'
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 280, 771, 311))
        self.tableWidget.setMaximumSize(QtCore.QSize(790, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 110, 491, 129))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.zamanAralAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.zamanAralAdLabel.setObjectName("zamanAralAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.zamanAralAdLabel)
        self.arac_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.arac_adi.setObjectName("arac_adi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.arac_adi)
        self.zamanArpanEkleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.zamanArpanEkleLabel.setObjectName("zamanArpanEkleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.zamanArpanEkleLabel)
        self.arac_carpani = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.arac_carpani.setObjectName("arac_carpani")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.arac_carpani)
        self.araKapasitesiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.araKapasitesiLabel.setObjectName("araKapasitesiLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.araKapasitesiLabel)
        self.arac_kapasite = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.arac_kapasite.setObjectName("arac_kapasite")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.arac_kapasite)
        self.arac_ekle_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.arac_ekle_btn.setObjectName("arac_ekle_btn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.arac_ekle_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Araç Ekleme,  Güncelleme ve Silme Ekranı"))
        self.label.setText(_translate("Form", "Araç Ücret İşlemlerine Hoş Geldiniz"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Araç Tipi Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Çarpan Katsayısı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Araç Kapasitesi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Güncelle"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sil"))
        self.zamanAralAdLabel.setText(_translate("Form", "Zaman Araç Tipi Adı"))
        self.zamanArpanEkleLabel.setText(_translate("Form", "Zaman Çarpanı Ekle"))
        self.araKapasitesiLabel.setText(_translate("Form", "Araç Kapasitesi"))
        self.arac_ekle_btn.setText(_translate("Form", "Araç İşlemini Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

