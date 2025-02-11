

         #  INSTANCE VARİABLES
class calisan:
    def __init__(self,isim,maas):
        self.isim=isim
        self.maas=maas

calisan1=calisan("Ali",50000)
calisan2=calisan("Ahmet",3000)

print(calisan1.isim)
print(calisan2.maas)

print(calisan1.__dict__)
print(calisan2.__dict__)




         #  CLASS VARİABLES
# sinif değişkenlerine(class variables )nesne üzerinden de ulaşabilirim hem sınıfın kendisinden hem de 
# oluşturduğum değişkenler ve nesneler üzerinden de ulaşıyorum 
class calisan:
    zam_orani=1.1
    def __init__(self,isim,yas,maas):
        self.isim=isim
        self.yas=yas
        self.maas=maas

calisan1=calisan("Berkay",22,5000)
calisan2=calisan("Burak",21,7000)

calisan.zam_orani=1.5
print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)        

        




class calisan:
    zam_orani=1.1
    def __init__(self,isim,yas,maas):
        self.isim=isim
        self.yas=yas
        self.maas=maas

calisan1=calisan("Berkay",22,5000)
calisan2=calisan("Burak",21,7000)

calisan1.zam_orani=1.5
print(calisan.zam_orani)
print(calisan1.zam_orani)
print(calisan2.zam_orani)        
print(calisan1.__dict__)






class calisan:
    personel_sayisi=0
    def __init__(self,isim,maas):
        self.isim=isim 
        self.maas=maas 
        calisan.personel_sayisi+=1

print(calisan.personel_sayisi)
calisan1=calisan("Berk",8000)
print(calisan.personel_sayisi)
calisan2=calisan("Mert",2000)
print(calisan.personel_sayisi)