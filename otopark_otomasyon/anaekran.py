from anaekran_ui import Ui_MainWindow as Anapencere_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from yonetici_ekleme import Yonetici_Ekleme
from yonetici_guncelle_sil import Yonetici_Gs
from uye_ekleme import Uye_Ekleme
from uye_guncelle_sil import Uye_Gs
from abone_guncelle_sil import Abone_Gs
from abone_ekleme import Abone_Ekleme
from birimzaman_guncelle_sil import Birimzaman_Gs
from zamansal_islemler import Zamansal_Islemler
from aracsal_islemler import Arac_Islemler
from park_ekleme import Park_Ekleme
from eski_parklar import Eski_Parklar
import datetime

# ana ekran girişi için
class Anaekran(QMainWindow, Anapencere_Ui):
    def __init__(self):
        super(Anaekran,self).__init__()
        self.fgiris()

    # menülerin aktivasyonu için
    def fgiris(self):
        self.setupUi(self)
        self.action_giris.triggered.connect(self.fgiris)
        self.action_yonetici_ekle.triggered.connect(self.fyonetici_ekle)
        self.action_yonetici_guncelle.triggered.connect(self.fyonetici_guncelle_sil)
        self.action_arac_girisi.triggered.connect(self.farac_girisi)
        self.action_arac_cikisi.triggered.connect(self.fgiris)
        self.action_eski_parklar.triggered.connect(self.feskiparklar)
        self.action_abone_Ekle.triggered.connect(self.fabone_ekle)
        self.action_abone_Sil.triggered.connect(self.fabone_sil)
        self.action_birim_zaman_tutari.triggered.connect(self.fbirim_zaman)
        self.action_zaman_katsayilari.triggered.connect(self.fzaman_katsayilari)
        self.action_arac_katsayilari.triggered.connect(self.farac_katsayilari)
        self.ucret = 0
        self.ftablo()

    def ftablo(self):

        park_listesi =session.query(Park).filter(Park.park_durum == 0).all()
        park_sayisi = session.query(Park).filter(Park.park_durum == 0).count()
        oran = int(park_sayisi/100)
        self.doluluk_orani.setText("%"+str(park_sayisi))
        self.tableWidget.setRowCount(park_sayisi)
        self.bilgi = {}
        for park, y in zip(park_listesi,range(park_sayisi)):
            self.tableWidget.setItem(y,0,QTableWidgetItem(park.plaka_bilgisi))
            self.tableWidget.setItem(y, 1, QTableWidgetItem(str(park.park_giris)))
            self.tableWidget.setItem(y, 2, QTableWidgetItem(park.aboneid.abone_adi_soyadi))
            self.tableWidget.setItem(y, 3, QTableWidgetItem(park.aracid.arac_adi))

            hesapla = QPushButton(self)
            hesapla.setText("Hesapla")
            hesapla.setObjectName("h"+str(park.park_id))

            hesapla.clicked.connect(self.fhesapla)
            self.tableWidget.setCellWidget(y, 4, hesapla)


            self.tableWidget.setItem(y, 5, QTableWidgetItem(str(park.park_tutar)))

            cikis = QPushButton(self)
            cikis.setText("Çıkış")
            cikis.setObjectName("c"+str(park.park_id))
            cikis.setEnabled(0)
            self.tableWidget.setCellWidget(y, 6, cikis)
            cikis.clicked.connect(self.fcikis)

            self.bilgi[park.park_id] = [y,hesapla,cikis]

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def fhesapla(self):
        gelen = self.sender()
        park_id = int(gelen.objectName()[1:])

        park =session.query(Park).filter(Park.park_id == park_id).first()

        self.suan = datetime.datetime.now()
        zaman_farki = int((self.suan - park.park_giris).seconds/3600)
        self.zaman_farki = zaman_farki
        try:
            zzaman_carpani = session.query(Zamankatsayilari).filter(Zamankatsayilari.zaman_baslangic<=zaman_farki,Zamankatsayilari.zaman_bitis>=zaman_farki).first()
            zaman_carpani = zzaman_carpani.zaman_carpani
            self.zaman_carpani = zaman_carpani.zaman_id
        except:
            zaman_carpani = zaman_farki
            id = session.query(Zamankatsayilari).first()
            self.zaman_carpani=id.zaman_id

        brm_ucret = session.query(BirimZaman).first().birimzaman_tutari
        ucret = zaman_carpani*park.aboneid.abone_katsayisi*park.aracid.arac_katsayisi*brm_ucret
        # self.ftablo()
        self.tableWidget.setItem(self.bilgi[park_id][0], 5, QTableWidgetItem(str(ucret)))
        self.bilgi[park_id][2].setEnabled(1)
        self.ucret = ucret

        return self.ucret

    def fcikis(self):
        gelen = self.sender()
        id = int(gelen.objectName()[1:])
        ucret = self.ucret
        try:
            session.query(Park).filter(Park.park_id==id).update({
                Park.park_durum:1,Park.park_cikis:self.suan,
                Park.park_sure:self.zaman_farki,
                Park.park_tutar:ucret,
                Park.zaman_id:self.zaman_carpani
            }, synchronize_session=False)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarısız")
            dialog.show()
        self.ftablo()



    # yönetici ekleme penceresinin getirilmesi için
    def fyonetici_ekle(self):
        self.setCentralWidget(Yonetici_Ekleme())

    # yonetici güncelleme ve silme işlemleri için
    def fyonetici_guncelle_sil(self):
        self.setCentralWidget(Yonetici_Gs())

    # arac girişi
    def farac_girisi(self):
        self.setCentralWidget(Park_Ekleme())

    # araç çıkış işlemleri için
    def feskiparklar(self):
        self.setCentralWidget(Eski_Parklar())

    # abonelik işlemleri
    def fabone_ekle(self):
        self.setCentralWidget(Abone_Ekleme())

    # abone silme işlemleri için
    def fabone_sil(self):
        self.setCentralWidget(Abone_Gs())

     # birim zaman işlemleri için
    def fbirim_zaman(self):
        self.setCentralWidget(Birimzaman_Gs())

      # zaman katsayı işlemleri için
    def fzaman_katsayilari(self):
        self.setCentralWidget(Zamansal_Islemler())

    # araç katsayı işlemleri için
    def farac_katsayilari(self):
        self.setCentralWidget(Arac_Islemler())
