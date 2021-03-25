import sqlite3 as lite

conn = lite.connect("main.db")
c = conn.cursor()
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='rotalar' ''')
if c.fetchone()[0] == 1:
    pass
else:
    print("Tablo yok, oluşturuluyor.")
    c.execute("""CREATE TABLE rotalar (
    ad text,
    soyad text,
    plaka text,
    kalkis text,
    varis text
    )""")
    print("Tablo oluşturuldu.")


def RotaGor():
    c.execute("SELECT rowid, * FROM rotalar")
    rotalist = c.fetchall()
    for rota in rotalist:
        print(rota)

def rotaEkle(ad,  soyad,  plaka,  kalkis,  varis):
    conn.execute("""
    INSERT INTO rotalar VALUES (?,?,?,?,?)
    """), [(ad, soyad, plaka, kalkis, varis)]
    conn.commit()
    print("Bilgiler kaydedildi.")

def secim():
    print("""
        1- Kayıtlı Rotaları Görüntüle
        2- Yeni Rota Ekle
        3- Çıkış
        """)
    inputsecim = input("Hoşgeldiniz, yapmak istediğiniz işlemi seçiniz:")
    if inputsecim == "1":
        RotaGor()

    if inputsecim == "2":
        ad = str(input("Sürücünün Adını Giriniz:"))
        soyad = str(input("Sürücünün Soyadını Giriniz:"))
        plaka = str(input("Sürücünün Plakasını Giriniz:"))
        kalkis = str(input("Sürücünün Kalkış Yerini Giriniz:"))
        varis = str(input("Sürücünün Varış Yerini Giriniz:"))
        rotaEkle(ad, soyad, plaka, kalkis, varis)

    if inputsecim == "3":
        print("ÇIKIŞ YAPILDI.")
        conn.commit()
        conn.close()
        cikisFlag = 1
        return cikisFlag


def main():
    while True:
        cikisFlag = secim()
        if cikisFlag == 1:
            break
        



        


main()