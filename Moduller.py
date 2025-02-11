
# sqrt=karekok
# fabs=mutlak değer
# factorial=faktöriyel

# import math
# sonuc=math.fabs(-96)
# print(int(sonuc))


# from math import factorial,sqrt
# sonuc1=factorial(5)
# sonuc2=sqrt(81)
# print(sonuc1)
# print(sonuc2)


# from math import *
# sonuc3=factorial()
# sonuc4=fabs()
# sonuc5=sqrt()


# def cember_cevresi(r):
#     return 2*3.14*r
# def daire_alani(r):
#     return 3.14*r*r



       # RANDOM MODÜLÜ
import random 
# for i in range(10):
#     print(random.random())  # 0 ve 1 arsında 10 tane rasgele sayı üretiyor

# for i in range(9):
#     print(random.uniform(10,30))  # 10 ve 30 arasında 9 tane rastgele sayı üretiyor

# for i in range(8):
#     print(random.randint(1,5))  # burda hem üst hem de alt sınırlar dahildir ratgele tam sayı üretiyor

# for i in range(10):
#     print(random.randrange(1,10,2))  # 1 den 10 a (10 dahil değil) 2 şer 2 şer artırarak rast üretir



# liste=["siyah","beyaz","mavi","yesil","gri","turuncu"]
# print(random.choice(liste)) # rastgele bir renk seçer
# print(random.sample(liste,3)) # rastgele 3 tane renk seçer
# print(random.shuffle(liste)) # none çıktısını verir bunu daha farklı şeilde kullanacaz

# random.shuffle(liste) # listedeki renklerin yerlerini değiştiriyor
# print(liste)



# zarlar={1:0,2:0,3:0,4:0,5:0,6:0}
# for i in range(100):
#     zar=random.randint(1,6)
#     zarlar[zar]+=1

# for zar in zarlar:
#     print(f"{zar} gelme olasiligi :{zarlar[zar]/100}")



# alti_alti=0
# deneme_sayisi=0
# while True:
#     deneme_sayisi +=1
#     zar1=random.randint(1,6)
#     zar2=random.randint(1,6)
#     if zar1==6 and zar2==6 :
#         alti_alti +=1
#     if alti_alti==10:
#         print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atildi")






       # TİME MODÜLÜ
# import time
# zaman=time.time()
# print(zaman)


# baslangic=time.time()
# liste=[]
# for i in range(100000):
#     liste.append(i)
# bitis=time.time()
# print(bitis-baslangic)


# zaman1=time.ctime(10000000)
# print(zaman1)


# zaman2=time.localtime()
# print(zaman2)


# print("program baslatildi...")
# zaman3=time.sleep(13) # 13 saniye uyuma haline geçer
# print(zaman3)
# print("program sona erdi...")


# zaman4=time.asctime() # çıktıda hic bişey vermez 
# print(zaman4)

# zaman5=time.localtime()
# zaman6=time.asctime(zaman5)
# print(zaman6)


# zaman7=time.strftime(%d:%m)
# print(zaman7)
       




       # DATETİME MODÜLÜ 
from datetime import date  # tarih işlemleri için kullanılır
bugun=date.today()  # tarih yıl-ay-gün diye yazılır
print(bugun)
print(bugun.day)
print(bugun.month)
print(bugun.year)
print(bugun.weekday())  # haftanın ilk gününü sıfır(0) ile başlatır 
print(bugun.isoweekday())  # haftanın ilk gününü bir(1) ile başlatır 

gecmis_tarih=date(2015,8,13)
print(gecmis_tarih)
print(gecmis_tarih.weekday())  # haftanun kaçıncı günü olduğunu gösterir

ne_kadar_gecmis=bugun-gecmis_tarih
print(ne_kadar_gecmis)


from datetime import datetime  # hem tarih hem de zaman işlemleri için kullanılır
suan=datetime.now()
print(suan)
print(suan.year)
print(suan.month)
print(suan.day)
print(suan.hour)
print(suan.minute)
print(suan.second)
print(suan.ctime())  # tarihi saati yazar
print(suan.date())  # sadece tarih yazar
print(suan.time())  # sadece zamanı yazar
print(suan.date().month)  # tarihten sadece ayı yazar

print(bugun.strftime("%d/%m/%Y"))  # gün-ay-yıl şeklinde yazar
print(suan.strftime("%d/%m/%Y/%A"))

print(datetime.strftime(bugun,"%d*%m*%Y"))
print(suan.strftime("%d:%m:%Y"))


from datetime import timedelta  #  zaman farklarını temsil eder
suan1=datetime.now()
tdelta=timedelta(days=7,hours=5,seconds=56)
print(suan1+tdelta)
print(suan1-tdelta)


#örnekk
pazar_sayisi=0
for yil in range(1901,2001):
    for ay in range(1,13):
        if datetime(yil,ay,1).weekday()==6:
          pazar_sayisi +=1
print(pazar_sayisi)