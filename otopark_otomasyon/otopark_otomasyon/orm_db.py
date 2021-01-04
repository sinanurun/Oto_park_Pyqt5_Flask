"""
bu bölümde orm yapısı kullanılarak db iş ve işlemleri gerçekleştirilmektedir.
tablo tanımları vb işlmler

"""
# from sqlalchemy import Column, ForeignKey, Integer, String # yerine * da olabilirdi
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  #tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()

# Yönetim işlemleri için db orm yapısı
class Yonetim(Base):
    #tablo adı
    __tablename__ = 'yonetim'
    #tablo sutunları ve özellikleri varsa da ilişkileri
    yonetici_id = Column(Integer, unique= True, primary_key=True, autoincrement=True)
    yonetici_adi = Column(String(10), nullable=False)
    yonetici_tc = Column(String(11), unique=True)
    yonetici_sifre = Column(String(10), nullable=False)
    yonetici_durum = Column(Integer, default=1)

# abone ile ilgili orm için nesne yapısı
class Abone(Base):
    __tablename__ = 'abone'
    abone_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    abone_adi_soyadi = Column(String(100))
    abone_tel = Column(String(15))
    abone_katsayisi = Column(Float)
    abone_durum = Column(Integer, default=1)

class Abonearaclar(Base):
    __tablename__ = 'abone_araclar'
    abone_arac_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    abone_arac_plaka = Column(String(12))


# zaman için gerekli orm yapısı
class BirimZaman(Base):
    __tablename__ = 'birimzaman'
    birimzaman_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    birimzaman_adi = Column(String(40))
    birimzaman_tutari = Column(Float)


class Kapasite(Base):
    __tablename__ = 'kapasite'
    kapasite_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    kapasite_miktari = Column(Float)#240

# zamansal katsayı işlemleri için db orm yapısı
class Zamankatsayilari(Base):
    __tablename__ = 'zamankatsayilari'
    zaman_id = Column(Integer,unique=True, primary_key=True, autoincrement= True)
    zaman_adi = Column(String(40))
    zaman_baslangic = Column(Float)
    zaman_bitis = Column(Float)
    zaman_carpani = Column(Float)

# araç katsayı işlemleri için db orm yapısı
class Arackatsayilari(Base):
    __tablename__ = 'arackatsayilari'
    arac_id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    arac_adi = Column(String(40))
    arac_katsayisi = Column(Float)
    arac_kapasite = Column(Float)


# park işlemleri için db orm yapısı
class Park(Base):
    #tablo adı
    __tablename__ = 'park'
    #tablo sutunları ve özellikleri varsa da ilişkileri
    park_id = Column(Integer, unique= True, primary_key=True, autoincrement=True)
    plaka_bilgisi = Column(String(10), nullable=False)
    park_giris = Column(DateTime)
    park_cikis = Column(DateTime)
    park_sure = Column(Integer)
    park_tutar = Column(Float)
    abone_id = Column(Integer, ForeignKey('abone.abone_id'))
    aboneid = relationship(Abone, foreign_keys=[abone_id])
    arac_id = Column(Integer, ForeignKey('arackatsayilari.arac_id'))
    aracid = relationship(Arackatsayilari, foreign_keys=[arac_id])
    zaman_id = Column(Integer, ForeignKey('zamankatsayilari.zaman_id'))
    zamanid = relationship(Zamankatsayilari, foreign_keys=[zaman_id])
    park_durum = Column(Integer, default=1)

# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///otopark_db.sqlite',connect_args={"check_same_thread": False})

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)

