
def bilgi_ver():
    print("islem basarili")

bilgi_ver()



def selamlama(isim):
    print("merhaba" + isim)

selamlama(" Seher")



def topla(x,y):
    print(f"x+y = {x+y}")

topla(20,30)



def ortalma_hesapla(liste):
    toplam=sum(liste)
    adet=len(liste)
    ortalama=toplam/adet 
    print(f"ortalama : {ortalama}")

ortalma_hesapla([2,5,3,9,25,21,10])   



def buyuk_harfe_cevir(metin):
    metin=metin.upper()
    print(metin)

buyuk_harfe_cevir("asKOLwqA")



def selamlamak(mesaj,isim):
    print(f"{mesaj} {isim}")

selamlamak("Nasilsin","Seher")



def selamlamak(mesaj,isim="Anonim"): # burdaki anonim eğer parameterede isim verilmediğinde kullanılır
    print(f"{mesaj} {isim}")

selamlamak("naber")



def indirim_yap(fiyat,yuzde):
    indirim_miktari=fiyat*(yuzde/100)
    indirimli_fiyat=fiyat-indirim_miktari
    print(f"indirimli tutar:{indirimli_fiyat}")

indirim_yap(50,60)



def ortalama_hesapla(x,y):
    return (x+y)/2

a=ortalama_hesapla(2,6)
b=ortalama_hesapla(10,8)
print(a+b)



def buyuk_harfe_cevir(metin):
    return metin.upper()

fonk=buyuk_harfe_cevir
sonuc=fonk("AnnEm")
print(sonuc)    



