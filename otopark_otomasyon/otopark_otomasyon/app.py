from flask import *
from db_islemleri import *
import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
kullanici = {}


# @app.route('/')
# def index():
#     return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def index():
    park_sayisi = session.query(Park).filter(Park.park_durum == 0).count()
    print(park_sayisi)
    try:
        if request.method == 'POST':
            bilgiler = request.form.to_dict()
            arac_plaka = bilgiler['plaka_bilgisi']
            print(arac_plaka)
            tutar = hesapla(arac_plaka)
            print(tutar)
            return render_template("index.html",oran=park_sayisi,ucret=tutar)

        return render_template("index.html",oran=park_sayisi)
    except:
        return redirect(url_for('/', oran=park_sayisi))
    return redirect(url_for('/'))

def hesapla(plaka):
    park = session.query(Park).filter(Park.plaka_bilgisi==plaka).first()

    # park = session.query(Park).filter(Park.park_id == park_id).first()

    suan = datetime.datetime.now()
    zaman_farki = int((suan - park.park_giris).seconds / 3600)
    zaman_farki = zaman_farki
    try:
        zzaman_carpani = session.query(Zamankatsayilari).filter(Zamankatsayilari.zaman_baslangic <= zaman_farki,
                                                                Zamankatsayilari.zaman_bitis >= zaman_farki).first()
        zaman_carpani = zzaman_carpani.zaman_carpani
        zaman_carpani = zaman_carpani.zaman_id
    except:
        zaman_carpani = zaman_farki
        id = session.query(Zamankatsayilari).first()
        zaman_carpani = id.zaman_id

    brm_ucret = session.query(BirimZaman).first().birimzaman_tutari
    ucret = zaman_carpani * park.aboneid.abone_katsayisi * park.aracid.arac_katsayisi * brm_ucret
    return ucret

if __name__ == '__main__':
    app.run(debug=True)
