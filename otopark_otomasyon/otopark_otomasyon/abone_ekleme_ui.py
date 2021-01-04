# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abone_ekleme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 110, 531, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.yNeticiAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiAdLabel.setObjectName("yNeticiAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.yNeticiAdLabel)
        self.abone_adi_soyadi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.abone_adi_soyadi.setObjectName("abone_adi_soyadi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.abone_adi_soyadi)
        self.eItmenTelefonLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eItmenTelefonLabel.setObjectName("eItmenTelefonLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.eItmenTelefonLabel)
        self.abone_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.abone_tel.setObjectName("abone_tel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.abone_tel)
        self.eItmenAdresLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.eItmenAdresLabel.setObjectName("eItmenAdresLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.eItmenAdresLabel)
        self.abone_katsayisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.abone_katsayisi.setObjectName("abone_katsayisi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.abone_katsayisi)
        self.yNeticiDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiDurumuLabel.setObjectName("yNeticiDurumuLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yNeticiDurumuLabel)
        self.abone_durum = QtWidgets.QComboBox(self.formLayoutWidget)
        self.abone_durum.setObjectName("abone_durum")
        self.abone_durum.addItem("")
        self.abone_durum.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.abone_durum)
        self.yelikBitiTarihiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yelikBitiTarihiLabel.setText("")
        self.yelikBitiTarihiLabel.setObjectName("yelikBitiTarihiLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yelikBitiTarihiLabel)
        self.abone_ekle_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.abone_ekle_btn.setObjectName("abone_ekle_btn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.abone_ekle_btn)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 740, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Abone Ekleme Ekranı"))
        self.yNeticiAdLabel.setText(_translate("Form", "Abone Adı Soyadı"))
        self.eItmenTelefonLabel.setText(_translate("Form", "Abone Telefon"))
        self.eItmenAdresLabel.setText(_translate("Form", "Abone Katsayısı"))
        self.yNeticiDurumuLabel.setText(_translate("Form", "Abone Durumu"))
        self.abone_durum.setItemText(0, _translate("Form", "Aktif"))
        self.abone_durum.setItemText(1, _translate("Form", "Pasif"))
        self.abone_ekle_btn.setText(_translate("Form", "Abone Ekle"))
        self.label.setText(_translate("Form", "Yeni Abone Ekleme Formu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

