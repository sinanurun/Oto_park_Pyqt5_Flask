from giris_ekrani_ui import Ui_giris_ekrani
from PyQt5.QtWidgets import *
import sys
from db_islemleri import *
from anaekran import Anaekran

class GirisPenceresi(QWidget,Ui_giris_ekrani):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hatali_giris.setVisible(False)
        self.g_butonu.clicked.connect(self.kontrol)
    def kontrol(self):
        tcno = self.tcno.text()
        sifre = self.sifre.text()
        onay = yonetici_girisi(tcno, sifre)
        if onay == False:
            self.hatali_giris.setVisible(1)
        elif onay == True:
            self.hide()
            self.ype = Anaekran()
            self.ype.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GirisPenceresi()
    pencere.show()
    sys.exit(app.exec_())