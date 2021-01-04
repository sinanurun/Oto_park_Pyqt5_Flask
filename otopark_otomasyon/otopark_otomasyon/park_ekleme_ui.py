# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'park_ekleme.ui'
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
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 130, 461, 103))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.plakaBilgisiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.plakaBilgisiLabel.setObjectName("plakaBilgisiLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.plakaBilgisiLabel)
        self.plaka_bilgisi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.plaka_bilgisi.setObjectName("plaka_bilgisi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plaka_bilgisi)
        self.aboneBilgisiLabel_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.aboneBilgisiLabel_2.setObjectName("aboneBilgisiLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.aboneBilgisiLabel_2)
        self.abone_bilgisi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.abone_bilgisi.setObjectName("abone_bilgisi")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.abone_bilgisi)
        self.araTipiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.araTipiLabel.setObjectName("araTipiLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.araTipiLabel)
        self.arac_bilgisi = QtWidgets.QComboBox(self.formLayoutWidget)
        self.arac_bilgisi.setObjectName("arac_bilgisi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.arac_bilgisi)
        self.arac_ekle_btn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.arac_ekle_btn.setObjectName("arac_ekle_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.arac_ekle_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Araç Park Ekleme Ekranı"))
        self.label.setText(_translate("Form", "Yeni Araç Park Ekleme Formu"))
        self.plakaBilgisiLabel.setText(_translate("Form", "Plaka Bilgisi"))
        self.aboneBilgisiLabel_2.setText(_translate("Form", "Abone Bilgisi"))
        self.araTipiLabel.setText(_translate("Form", "Araç Tipi"))
        self.arac_ekle_btn.setText(_translate("Form", "Araç Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

