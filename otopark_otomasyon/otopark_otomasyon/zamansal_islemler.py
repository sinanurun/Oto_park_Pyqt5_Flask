from zamansal_islemler_ui import Ui_Form as Zamansal_Islemler_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Zamansal_Islemler(QWidget,Zamansal_Islemler_Ui):
    def __init__(self):
        super(Zamansal_Islemler,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.zaman_ekle_btn.clicked.connect(self.fzaman_ekle)
        self.ftablo()

    # zaman ekleme işlemi fonksiyonu
    def fzaman_ekle(self):
        yzaman_adi = self.zaman_adi.text()
        yzaman_baslangic  = float(self.zaman_baslangic.text())
        yzaman_bitis  = float(self.zaman_bitis.text())
        yzaman_katsayisi = float(self.zaman_carpani.text())


        # zamansal işlemi dbye ekleme işlemi kontrol ve dönütü
        try:
            zaman = Zamankatsayilari(zaman_adi=yzaman_adi,zaman_baslangic=yzaman_baslangic,zaman_bitis=yzaman_bitis,
                                     zaman_carpani=yzaman_katsayisi)
            session.add(zaman)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Zaman Ekleme Başarılı")
            dialog.show()

        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Zaman Ekleme Hatalı")
            dialog.show()
        self.ftablo()


    def ftablo(self):
        self.sozluk = {}
        self.zamanlar = session.query(Zamankatsayilari).all()
        self.tableWidget.setRowCount(0)
        for zaman, sira in zip(self.zamanlar, range(len(self.zamanlar))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira, 0, QTableWidgetItem(zaman.zaman_adi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(str(zaman.zaman_baslangic)))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(str(zaman.zaman_bitis)))
            self.tableWidget.setItem(sira, 3, QTableWidgetItem(str(zaman.zaman_carpani)))

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(zaman.zaman_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 4, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s" + str(zaman.zaman_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 5, sil)
            self.sozluk[zaman.zaman_id] = [sira]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen]
        try:
            session.query(Zamankatsayilari).filter(Zamankatsayilari.zaman_id == gelen).update({
                Zamankatsayilari.zaman_adi: self.tableWidget.item(sira, 0).text(),
                Zamankatsayilari.zaman_baslangic: float(self.tableWidget.item(sira, 1).text()),
                Zamankatsayilari.zaman_bitis: float(self.tableWidget.item(sira, 2).text()),
                Zamankatsayilari.zaman_carpani: float(self.tableWidget.item(sira, 3).text())
            }, synchronize_session=False)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarısız")
            dialog.show()
        self.fbaslangic()

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Zamankatsayilari).filter(Zamankatsayilari.zaman_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.fbaslangic()
