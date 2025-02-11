
class Calisan:
    zam_orani=1.1
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=(isim+soyisim).lower()+ "@sirket.com"

    def Bilgileri_Goster(self):
        return "ad: {} soyad: {} maas: {} email: {} ".format(self.isim,self.soyisim,self.maas,self.email)

calisan1=Calisan("ALİ","KARAKAŞ",5000)
calisan2=Calisan("BURAK","UZUN",6000)

print(calisan2.isim,calisan2.soyisim,calisan2.maas)
print(calisan1.email)

class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas,bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil=bildigi_dil
        
    zam_orani=1.2
    def Bilgileri_Goster(self):
        return "ad: {} soyad: {} maas: {} email: {} dil: {} ".format(self.isim,self.soyisim,self.maas,self.email,self.bildigi_dil)
    def Dilini_Soyle(self):
        return f"bildigim dil: {self.bildigi_dil}"

yazilimci1=Yazilimci("İREM","SARBOGA",6000,"python")
yazilimci2=Yazilimci("GULAN","AKYEL",7000,"java")
    
print(yazilimci1.email)
print(yazilimci2.isim)
print(calisan2.zam_orani)
print(yazilimci1.zam_orani)
print(yazilimci1.Bilgileri_Goster())
print(yazilimci2.Bilgileri_Goster())
print(calisan2.Bilgileri_Goster())
print("ben İREM"+ yazilimci1.Dilini_Soyle())



