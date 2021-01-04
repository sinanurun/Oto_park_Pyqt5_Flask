from park_ekleme_ui import Ui_Form as Park_Ekleme_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys
import datetime

class Park_Ekleme(QWidget,Park_Ekleme_Ui):
    def __init__(self):
        super(Park_Ekleme,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.arac_ekle_btn.clicked.connect(self.farac_ekle)

        aboneler = session.query(Abone).filter(Abone.abone_durum==0).all()
        #self.abone_bilgisi[0] Ali nin idsi 8 . [1]veli 15 addItem(abone.abone_adi_soyadi)
        self.abone_idleri=[0] #=> 8 =>89   [1] 15

        for abone, sayi in zip(aboneler,range(len(aboneler))):
            self.abone_bilgisi.addItem(abone.abone_adi_soyadi,abone.abone_id)
            self.abone_idleri.append(abone.abone_id)


        self.arac_idleri=[]

        araclar = session.query(Arackatsayilari).all()
        for arac, sayi in zip(araclar,range(len(araclar))):
            self.arac_bilgisi.addItem(arac.arac_adi,arac.arac_id)
            self.arac_idleri.append(arac.arac_id)


    # araç park ekleme işlemi fonksiyonu
    def farac_ekle(self):
        plaka_bilgisi = self.plaka_bilgisi.text()
        park_giris = datetime.datetime.now()

        abone_id = self.abone_bilgisi.currentData()
        arac_id = self.arac_bilgisi.currentData()
        park_durum = 0

        # aboneyi veri tabanına ekleme işlemi kontrol ve dönütü
        try:
            park = Park(plaka_bilgisi=plaka_bilgisi,park_giris=park_giris,abone_id=abone_id,arac_id=arac_id,park_durum=park_durum)
            session.add(park)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Park Ekleme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Park Ekleme Hatalı")
            dialog.show()
