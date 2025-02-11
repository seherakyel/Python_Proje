

from datetime import date
class kisi:
    zam_orani=1.1
    kisi_sayisi=0
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        kisi.kisi_sayisi +=1
    
    def bilgileri_soyle(self):
        return f"ad:{self.isim} yas:{self.yas}"
    
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi
    
    @classmethod
    def string_ile_olustur(cls,str):
        isim,yas=str.split("-")
        return cls(isim,yas)
    
    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        return cls(isim,date.today().year_dogum_yili)
    
    # kisi1=kisi("ali",20)
    # kisi2=kisi("veli",45)
    kisi3=kisi3.string_ile_olustur("ayse-25")
    kisi4=kisi4.dogum_yili_ile_olustur("elif"1990)



        
 