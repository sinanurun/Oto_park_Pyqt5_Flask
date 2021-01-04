from uye_guncelle_sil_ui import Ui_Form as Uye_Gs_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *
from PyQt5 import QtCore
from datetime import datetime
import sys

class Uye_Gs(QWidget,Uye_Gs_Ui):
    def __init__(self):
        super(Uye_Gs,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.uyeler = session.query(Uye).all()
        self.tableWidget.setRowCount(0)
        for uye,sira in zip(self.uyeler,range(len(self.uyeler))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira,0,QTableWidgetItem(uye.uye_adi_soyadi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(uye.uye_tc))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(uye.uye_sifre))
            self.tableWidget.setItem(sira, 3, QTableWidgetItem(uye.uye_tel))
            self.tableWidget.setItem(sira, 4, QTableWidgetItem(uye.uye_adres))
            self.tableWidget.setItem(sira, 5, QTableWidgetItem(uye.uye_notu))

            egitmen_listesi = session.query(Egitmen).filter(Egitmen.egitmen_durum == 0).all()
            self.edurum = {}
            ecombo = QComboBox(self)
            for x, y in zip(egitmen_listesi, range(len(egitmen_listesi))):
                ecombo.addItem(x.egitmen_adi_soyadi)
                self.edurum[y] = x.egitmen_id
                if uye.egitmen_id == x.egitmen_id:
                    secili_egitmen = x.egitmen_adi_soyadi
            ecombo.setObjectName("e" + str(uye.uye_id))
            ecombo.setCurrentText(secili_egitmen)
            self.tableWidget.setCellWidget(sira, 6, ecombo)

            utarih = QDateEdit(self)
            date_object = datetime.strptime(uye.uye_tarihi, '%d.%m.%Y').date()
            utarih.setDate(date_object)
            utarih.setCalendarPopup(True)
            utarih.setObjectName("utarih" + str(uye.uye_id))
            self.tableWidget.setCellWidget(sira, 7, utarih)

            dcombo = QComboBox(self)
            self.durum = ["Aktif","Pasif"]
            for x in self.durum:
                dcombo.addItem(x)
            dcombo.setObjectName("d" + str(uye.uye_id))
            dcombo.setCurrentIndex(uye.uye_durum)
            self.tableWidget.setCellWidget(sira, 8, dcombo)

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(uye.uye_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)
            self.tableWidget.setCellWidget(sira, 9, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s"+str(uye.uye_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 10, sil)
            self.sozluk[uye.uye_id] = [sira,ecombo,utarih,dcombo]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        egitmen = self.sozluk[gelen][1]
        tarih = self.sozluk[gelen][2]
        durum = self.sozluk[gelen][3]
        # print(sira,durum.currentIndex(),durum.objectName())
        try:
            session.query(Uye).filter(Uye.uye_id==gelen).update({
                Uye.uye_adi_soyadi:self.tableWidget.item(sira,0).text(),
                Uye.uye_tc:self.tableWidget.item(sira,1).text(),
                Uye.uye_sifre:self.tableWidget.item(sira,2).text(),
                Uye.uye_tel:self.tableWidget.item(sira,3).text(),
                Uye.uye_adres: self.tableWidget.item(sira, 4).text(),
                Uye.uye_notu: self.tableWidget.item(sira, 5).text(),
                Uye.egitmen_id:self.edurum[egitmen.currentIndex()],
                Uye.uye_tarihi:tarih.text(),
                Uye.uye_durum:durum.currentIndex(),

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
            session.query(Yonetim).filter(Yonetim.yonetici_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.ftablo()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Uye_Gs()
    pencere.show()
    sys.exit(app.exec_())
