from uye_ekleme_ui import Ui_Form as Uye_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Uye_Ekleme(QWidget,Uye_Ekleme_Ui):
    def __init__(self):
        super(Uye_Ekleme,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.uyelik_tarihi.setDateTime(QtCore.QDateTime.currentDateTime())

        egitmen_listesi = session.query(Egitmen).filter(Egitmen.egitmen_durum == 0).all()
        self.durum = {}
        for x, y in zip(egitmen_listesi,range(len(egitmen_listesi))):
            self.egitmen.addItem(x.egitmen_adi_soyadi)
            self.durum[y] = x.egitmen_id

        self.uye_ekle_btn.clicked.connect(self.fuye_ekle)

    # Üye ekleme işlemi fonksiyonu
    def fuye_ekle(self):
        pass
        u_adi_soyadi = self.uye_adi_soyadi.text()
        u_tc = self.uye_tc.text()
        u_sifre = self.uye_sifre.text()
        u_telefon = self.uye_tel.text()
        u_adres = self.uye_adres.text()
        u_notu = self.uye_notu.text()
        u_durum = self.uye_durum.currentIndex()
        u_egitmen = self.durum[self.egitmen.currentIndex()]
        u_tarih = self.uyelik_tarihi.text()


        # üye veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            uye = Uye(uye_adi_soyadi=u_adi_soyadi,uye_tc=u_tc,uye_sifre=u_sifre,
                      uye_tel=u_telefon,uye_adres=u_adres,uye_notu=u_notu,
                      uye_durum=u_durum,egitmen_id=u_egitmen,uye_tarihi=u_tarih)
            session.add(uye)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Üye Ekleme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Üye Ekleme Hatalı")
            dialog.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Uye_Ekleme()
    pencere.show()
    sys.exit(app.exec_())