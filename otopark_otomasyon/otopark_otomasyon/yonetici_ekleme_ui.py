# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yonetici_ekleme.ui'
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
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 160, 411, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.yNeticiAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiAdLabel.setObjectName("yNeticiAdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.yNeticiAdLabel)
        self.yonetici_adi = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.yonetici_adi.setObjectName("yonetici_adi")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.yonetici_adi)
        self.yNeticiTCNoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiTCNoLabel.setObjectName("yNeticiTCNoLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.yNeticiTCNoLabel)
        self.yonetici_tcno = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.yonetici_tcno.setObjectName("yonetici_tcno")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yonetici_tcno)
        self.yNeticiIfreLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiIfreLabel.setObjectName("yNeticiIfreLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yNeticiIfreLabel)
        self.yonetici_sifre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.yonetici_sifre.setObjectName("yonetici_sifre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yonetici_sifre)
        self.yNeticiDurumuLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.yNeticiDurumuLabel.setObjectName("yNeticiDurumuLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yNeticiDurumuLabel)
        self.yonetici_durum = QtWidgets.QComboBox(self.formLayoutWidget)
        self.yonetici_durum.setObjectName("yonetici_durum")
        self.yonetici_durum.addItem("")
        self.yonetici_durum.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.yonetici_durum)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton)
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
        Form.setWindowTitle(_translate("Form", "Yönetici Ekleme Ekranı"))
        self.yNeticiAdLabel.setText(_translate("Form", "Yönetici Adı Soyadı"))
        self.yNeticiTCNoLabel.setText(_translate("Form", "Yönetici T.C. No "))
        self.yNeticiIfreLabel.setText(_translate("Form", "Yönetici Şifre"))
        self.yNeticiDurumuLabel.setText(_translate("Form", "Yönetici Durumu"))
        self.yonetici_durum.setItemText(0, _translate("Form", "Aktif"))
        self.yonetici_durum.setItemText(1, _translate("Form", "Pasif"))
        self.pushButton.setText(_translate("Form", "Yönetici Ekle"))
        self.label.setText(_translate("Form", "Yönetici Ekleme Formu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

