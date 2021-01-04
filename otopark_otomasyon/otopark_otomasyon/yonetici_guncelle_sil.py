from yonetici_guncelle_sil_ui import Ui_Form as Yonetici_Gs_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *

class Yonetici_Gs(QWidget,Yonetici_Gs_Ui):
    def __init__(self):
        super(Yonetici_Gs,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.yoneticiler = session.query(Yonetim).all()
        self.tableWidget.setRowCount(0)
        for yonetici,sira in zip(self.yoneticiler,range(len(self.yoneticiler))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira,0,QTableWidgetItem(yonetici.yonetici_adi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(yonetici.yonetici_tc))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(yonetici.yonetici_sifre))

            dcombo = QComboBox(self)
            self.durum = ["Aktif","Pasif"]
            for x in self.durum:
                dcombo.addItem(x)
            dcombo.setObjectName("d" + str(yonetici.yonetici_id))
            dcombo.setCurrentIndex(yonetici.yonetici_durum)

            self.tableWidget.setCellWidget(sira, 3, dcombo)

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(yonetici.yonetici_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 4, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s"+str(yonetici.yonetici_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 5, sil)
            self.sozluk[yonetici.yonetici_id] = [sira,dcombo]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen][1]
        print(sira,durum.currentIndex(),durum.objectName())
        try:
            session.query(Yonetim).filter(Yonetim.yonetici_id==gelen).update({
                Yonetim.yonetici_adi:self.tableWidget.item(sira,0).text(),
                Yonetim.yonetici_tc:self.tableWidget.item(sira,1).text(),
                Yonetim.yonetici_sifre:self.tableWidget.item(sira,2).text(),
                Yonetim.yonetici_durum:durum.currentIndex()
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