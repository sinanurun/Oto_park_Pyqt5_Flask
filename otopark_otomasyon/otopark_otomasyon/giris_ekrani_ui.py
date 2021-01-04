# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_ekrani.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_giris_ekrani(object):
    def setupUi(self, giris_ekrani):
        giris_ekrani.setObjectName("giris_ekrani")
        giris_ekrani.resize(424, 310)
        self.label = QtWidgets.QLabel(giris_ekrani)
        self.label.setGeometry(QtCore.QRect(70, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(giris_ekrani)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.tcno = QtWidgets.QLineEdit(giris_ekrani)
        self.tcno.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.tcno.setObjectName("tcno")
        self.sifre = QtWidgets.QLineEdit(giris_ekrani)
        self.sifre.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre.setObjectName("sifre")
        self.g_butonu = QtWidgets.QPushButton(giris_ekrani)
        self.g_butonu.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.g_butonu.setObjectName("g_butonu")
        self.hatali_giris = QtWidgets.QLabel(giris_ekrani)
        self.hatali_giris.setGeometry(QtCore.QRect(76, 200, 251, 51))
        self.hatali_giris.setObjectName("hatali_giris")
        self.label_3 = QtWidgets.QLabel(giris_ekrani)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(giris_ekrani)
        QtCore.QMetaObject.connectSlotsByName(giris_ekrani)

    def retranslateUi(self, giris_ekrani):
        _translate = QtCore.QCoreApplication.translate
        giris_ekrani.setWindowTitle(_translate("giris_ekrani", "Giriş Ekranı"))
        self.label.setText(_translate("giris_ekrani", "TC No"))
        self.label_2.setText(_translate("giris_ekrani", "Şifre"))
        self.g_butonu.setText(_translate("giris_ekrani", "Giriş"))
        self.hatali_giris.setText(_translate("giris_ekrani", "Giriş Hatalı Tekrar Deneyiniz"))
        self.label_3.setText(_translate("giris_ekrani", "OTOPARK YÖNETİM SİSTEMİ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    giris_ekrani = QtWidgets.QWidget()
    ui = Ui_giris_ekrani()
    ui.setupUi(giris_ekrani)
    giris_ekrani.show()
    sys.exit(app.exec_())

