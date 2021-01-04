from abone_ekleme_ui import Ui_Form as Abone_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Abone_Ekleme(QWidget,Abone_Ekleme_Ui):
    def __init__(self):
        super(Abone_Ekleme,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.abone_ekle_btn.clicked.connect(self.fabone_ekle)

    # Abone ekleme işlemi fonksiyonu
    def fabone_ekle(self):
        a_adi_soyadi = self.abone_adi_soyadi.text()
        a_telefon = self.abone_tel.text()
        a_katsayisi = float(self.abone_katsayisi.text())
        a_durum = self.abone_durum.currentIndex()

        # aboneyi veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            abone = Abone(abone_adi_soyadi=a_adi_soyadi,abone_tel=a_telefon,abone_katsayisi=a_katsayisi,abone_durum=a_durum)
            session.add(abone)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Abone Ekleme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Abone Ekleme Hatalı")
            dialog.show()
