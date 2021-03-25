import sqlite3 as lite
import sys

#conn = lite.connect("main.db")
c = conn.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='customers' ''')

if c.fetchone()[0] == 1:
    print('Table exist.')

else:
    print("Tablo yok, oluşturuluyor.")
    c.execute("""CREATE TABLE customers (
    ad text,
    soyad text,
    plaka text,
    kalkış_yeri text,
    varış_yeri text
    )""")
    print("Tablo oluşturuldu.")



#c.execute("""INSERT INTO customers VALUES(
#'Emre',
#'Sağır',
#'23 dl 434',
#'ankara',
#'bursa'
# )""")

c.execute("DELETE from customers WHERE rowid = 6")


c.execute("SELECT rowid, * FROM customers") #rowid ile numarasını da alıyorsun satırın.
                                            #* ile de diğer bütün bilgileri.


müşteriList = c.fetchall()
for müşteri in müşteriList:
    print(müşteri)
for müşteri in müşteriList:
    print(müşteri[2])

conn.commit()
conn.close()









#secenekler = """
#1- Kayıtlı Rotaları Görüntüle
#2- Yeni Rota Ekle
#3- Çıkış
#"""
#while True:
#    print(secenekler)
#    secim = input("Hoşgeldiniz, yapmak istediğiniz işlemi seçiniz:")
#    if secim == "1":
#        pass
#    if secim == "2":
#        pass
#    if secim == "3":
#        break
