from arac_islemler_ui import Ui_Form as Arac_Islemler_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
import sys

class Arac_Islemler(QWidget,Arac_Islemler_Ui):
    def __init__(self):
        super(Arac_Islemler,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.arac_ekle_btn.clicked.connect(self.farac_ekle)
        self.ftablo()

    # arac ekleme işlemi fonksiyonu
    def farac_ekle(self):
        yarac_adi = self.arac_adi.text()
        yarac_katsayisi = float(self.arac_carpani.text())
        yarac_kapasite = float(self.arac_kapasite.text())


        # araç tipi işlemi dbye ekleme işlemi kontrol ve dönütü
        try:
            arac = Arackatsayilari(arac_adi=yarac_adi, arac_katsayisi=yarac_katsayisi,
                                   arac_kapasite=yarac_kapasite)
            session.add(arac)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Araç Tipi Ekleme Başarılı")
            dialog.show()

        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Araç Tipi Ekleme Ekleme Hatalı")
            dialog.show()
        self.ftablo()


    def ftablo(self):
        self.sozluk = {}
        self.araclar = session.query(Arackatsayilari).all()
        self.tableWidget.setRowCount(0)
        for arac, sira in zip(self.araclar, range(len(self.araclar))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira, 0, QTableWidgetItem(arac.arac_adi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(str(arac.arac_katsayisi)))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(str(arac.arac_kapasite)))


            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(arac.arac_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 3, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s" + str(arac.arac_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 4, sil)
            self.sozluk[arac.arac_id] = [sira]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen]
        try:
            session.query(Arackatsayilari).filter(Arackatsayilari.arac_id == gelen).update({
                Arackatsayilari.arac_adi: self.tableWidget.item(sira, 0).text(),
                Arackatsayilari.arac_katsayisi: float(self.tableWidget.item(sira, 1).text()),
                Arackatsayilari.arac_kapasite: float(self.tableWidget.item(sira, 2).text()),
            }, synchronize_session=False)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Güncelleme İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Güncelleme İşlemi Başarısız")
            dialog.show()
        self.fbaslangic()

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Arackatsayilari).filter(Arackatsayilari.arac_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme İşlemi Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme İşlemi Başarısız")
            dialog.show()
        self.fbaslangic()
