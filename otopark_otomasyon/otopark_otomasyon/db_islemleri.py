from orm_db import *
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class Yonetici():
    def __init__(self):
        pass

    def faracekle(self):
        yeniabone = Abone()
    def farac_sil(self):
        pass

try:
    if session.query(BirimZaman).count() == 0:
        brmzmn = BirimZaman(birimzaman_id=1,birimzaman_adi="1 Saat Ücreti", birimzaman_tutari=1)
        session.add(brmzmn)
        session.commit()
    if session.query(Yonetim).count() == 0:
        yntm = Yonetim(yonetici_id=1, yonetici_adi="Yönetici", yonetici_tc="123",
                       yonetici_sifre="123",yonetici_durum=0)
        session.add(yntm)
        session.commit()
except:
    pass



def yonetici_girisi(yonetici_tc,yonetici_sifre):
    ygirisi = session.query(Yonetim).filter(Yonetim.yonetici_tc==yonetici_tc, Yonetim.yonetici_sifre==yonetici_sifre).first()
    if ygirisi.yonetici_durum == 0:
        return True
    else:
        return False

def fkapasite_miktari():
    kapasite = session.query(Kapasite).first()
    return kapasite.kapesite_miktari