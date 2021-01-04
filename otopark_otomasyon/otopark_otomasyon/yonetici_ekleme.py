from yonetici_ekleme_ui import Ui_Form as Yonetici_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *

# yönetici ekleme sayfası için
class Yonetici_Ekleme(QWidget,Yonetici_Ekleme_Ui):
    def __init__(self):
        super(Yonetici_Ekleme,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.fyonetici_ekle)

    # yönetici ekleme işlemi fonksiyonu
    def fyonetici_ekle(self):
        y_adi = self.yonetici_adi.text()
        y_tc = self.yonetici_tcno.text()
        y_sifre = self.yonetici_sifre.text()
        y_durum = self.yonetici_durum.currentIndex()

        # yöneticiyi veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            yonetici = Yonetim(yonetici_adi=y_adi,yonetici_tc=y_tc,
                               yonetici_sifre=y_sifre,yonetici_durum=y_durum)
            session.add(yonetici)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Yönetici Ekleme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Yönetici Ekleme Hatalı")
            dialog.show()
