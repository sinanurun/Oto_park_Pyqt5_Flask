from birimzaman_guncelle_sil_ui import Ui_Form as Birimzaman_Gs_Ui
from PyQt5.QtWidgets import *
from db_islemleri import *

class Birimzaman_Gs(QWidget,Birimzaman_Gs_Ui):
    def __init__(self):
        super(Birimzaman_Gs,self).__init__()
        self.fbaslangic()

    def fbaslangic(self):
        self.setupUi(self)
        self.ftablo()

    def ftablo(self):
        self.sozluk = {}
        self.bzaman = session.query(BirimZaman).all()
        self.tableWidget.setRowCount(0)
        for zaman, sira in zip(self.bzaman, range(len(self.bzaman))):
            self.tableWidget.insertRow(sira)
            self.tableWidget.setItem(sira, 0, QTableWidgetItem(zaman.birimzaman_adi))
            self.tableWidget.setItem(sira, 1, QTableWidgetItem(str(zaman.birimzaman_tutari)))


            guncelle = QPushButton(self)
            guncelle.setObjectName("g" + str(zaman.birimzaman_id))
            guncelle.setText("Güncelle")
            guncelle.clicked.connect(self.fguncelle)

            self.tableWidget.setCellWidget(sira, 2, guncelle)


            self.sozluk[zaman.birimzaman_id] = [sira]

    def fguncelle(self):
        gelen = self.sender()
        gelen = int(gelen.objectName()[1:])
        sira = self.sozluk[gelen][0]
        durum = self.sozluk[gelen]
        try:
            session.query(BirimZaman).filter(BirimZaman.birimzaman_id== gelen).update({
               BirimZaman.birimzaman_tutari: float(self.tableWidget.item(sira, 1).text()),
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

