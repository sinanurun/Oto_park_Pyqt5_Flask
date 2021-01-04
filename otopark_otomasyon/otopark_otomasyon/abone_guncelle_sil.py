from abone_guncelle_sil_ui import Ui_Form as Abone_Gs_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *

class Abone_Gs(QWidget,Abone_Gs_Ui):
    def __init__(self):
        super(Abone_Gs,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.aboneler = session.query(Abone).all()
        self.tableWidget.setRowCount(0)
        for abone, sira in zip(self.aboneler, range(len(self.aboneler))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira, 0, QTableWidgetItem(abone.abone_adi_soyadi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(abone.abone_tel))
            self.tableWidget.setItem(sira, 2, QTableWidgetItem(str(abone.abone_katsayisi)))
            dcombo = QComboBox(self)
            self.durum = ["Aktif", "Pasif"]
            for x in self.durum:
                dcombo.addItem(x)
            dcombo.setObjectName("d" + str(abone.abone_durum))
            dcombo.setCurrentIndex(abone.abone_durum)

            self.tableWidget.setCellWidget(sira, 3, dcombo)

            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(abone.abone_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 4, guncelle)

            sil = QPushButton(self)
            sil.setObjectName("s" + str(abone.abone_id))
            sil.setText("Sil")
            sil.clicked.connect(self.fsil)

            self.tableWidget.setCellWidget(sira, 5, sil)
            self.sozluk[abone.abone_id] = [sira, dcombo]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen][1]
        print(sira, durum.currentIndex(), durum.objectName())
        try:
            session.query(Abone).filter(Abone.abone_id == gelen).update({
                Abone.abone_adi_soyadi: self.tableWidget.item(sira, 0).text(),
                Abone.abone_tel: self.tableWidget.item(sira, 1).text(),
               Abone.abone_katsayisi: float(self.tableWidget.item(sira, 2).text()),
                Abone.abone_durum: durum.currentIndex()
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

    def fsil(self):
        try:
            gelen = self.sender()
            gelen = int(gelen.objectName()[1:])
            session.query(Abone).filter(Abone.abone_id == gelen).delete()
            session.commit()
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarılı")
            dialog.show()
        except:
            dialog = QMessageBox(self)
            islem = QLabel(dialog, text="Silme Başarısız")
            dialog.show()
        self.ftablo()
