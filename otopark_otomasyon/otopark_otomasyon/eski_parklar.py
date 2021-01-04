from eski_parklar_ui import Ui_Form as Eski_parklar_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
from datetime import datetime
import sys

class Eski_Parklar(QWidget,Eski_parklar_Ui):
    def __init__(self):
        super(Eski_Parklar,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.toplu_sil_btn.clicked.connect(self.ftoplu_sil)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.parklar = session.query(Park).filter(Park.park_durum==1).all()
        self.tableWidget.setRowCount(0)
        for park,sira in zip(self.parklar,range(len(self.parklar))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira,0,QTableWidgetItem(park.plaka_bilgisi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(str(park.park_giris)))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(str(park.park_cikis)))
            self.tableWidget.setItem(sira, 3, QTableWidgetItem(str(park.park_sure)))
            self.tableWidget.setItem(sira, 4, QTableWidgetItem(str(park.park_tutar)))
            self.tableWidget.setItem(sira, 5, QTableWidgetItem(park.aboneid.abone_adi_soyadi))
            self.tableWidget.setItem(sira, 6, QTableWidgetItem(park.aracid.arac_adi))
            self.tableWidget.setItem(sira, 7, QTableWidgetItem(park.zamanid.zaman_adi))




            dcombo = QComboBox(self)
            self.durum = ["Aktif","Pasif"]
            for x in self.durum:
                dcombo.addItem(x)
            dcombo.setObjectName("d" + str(park.park_id))
            dcombo.setCurrentIndex(park.park_durum)
            self.tableWidget.setCellWidget(sira, 8, dcombo)

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(park.park_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(sira, 9, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s"+str(park.park_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 10, sil)
            self.sozluk[park.park_id] = [sira,dcombo]

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen][1]
        # print(sira,durum.currentIndex(),durum.objectName())
        try:
            session.query(Park).filter(Park.park_id==gelen).update({
                Park.park_durum:durum.currentIndex(),
            },synchronize_session=False)
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="İşlem Başarısız")
            dialog.show()
        self.ftablo()

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Park).filter(Park.park_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.ftablo()

    def ftoplu_sil(self):
        try:

            session.query(Park).filter(Park.park_durum == 1).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Toplu Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Toplu Silme Başarısız")
            dialog.show()
        self.ftablo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Uye_Gs()
    pencere.show()
    sys.exit(app.exec_())
