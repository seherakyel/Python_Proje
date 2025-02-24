

#Kullanıcının görev ekleyebileceği, listeleyebileceği, güncelleyebileceği ve tamamlanan görevleri işaretleyebileceği basit 
#bir komut satırı (CLI) uygulaması.

gorevler_listesi=[
    {"ad": "alisveris yap", "tamamlandi": False},
    {"ad": "faturalari ode", "tamamlandi": True},
    {"ad": "kod yazmayi ogren", "tamamlandi": False},
    {"ad": "arkadaslarla bulus", "tamamlandi": False},
    {"ad": "evi temizle", "tamamlandi": True}
]

def gorev_ekle():
   yeni_gorev=input("eklemek istediginiz gorevin adini yazin ")
   gorevler_listesi.append({"ad":yeni_gorev,"tamamlandi":False})
   print(f"{yeni_gorev}basariyla eklendi ")
   print(gorevler_listesi)
   
def gorev_listele():
    print("<<<<<Gorev Listesi>>>>>")
    for i,gorev in enumerate(gorevler_listesi,start=1):
        if gorev["tamamlandi"]:
            durum = "Tamamlandii"
        else:
            durum = "Devam Ediyorr"
        print(f"{i}) {gorev['ad']} - {durum}")
  
def gorev_tamamla():
    print(gorevler_listesi)
    tamamlama=input("tamamlamak istedigin gorevin adi :")
    for gorevler in gorevler_listesi:# gorev_listesi nin içindeki her elemanı sırayla al bu elemanı geçici olarak gorevler isimli değişkene ata
        if gorevler["ad"]==tamamlama:
            gorevler["tamamlandi"]=True
    print(gorevler_listesi)
   
def gorev_sil():
    print(gorevler_listesi)
    sil = input("silmek istediginiz görevin adi: ")
    silindi = False  # Görevin silinip silinmediğini kontrol eder
    for i, gorev in enumerate(gorevler_listesi[:]):
        if gorev["ad"] == sil:
            del gorevler_listesi[i]
            silindi = True
    if silindi:
        print(f"'{sil}' adli gorev artik listede yok.")
    else:
        print(f"'{sil}' adli gorev zaten listede yok.")

def ana_menu():

    while True:
        print("""GOREV UYGULAMASI
            1.)gorevi ekle
            2.)gorevleri listele
            3.)gorevleri tamamla
            4.)gorevi sil
            5.)cikis """)
        
        secim=input("secim yapiniz : ")

        if secim=="1":
            gorev_ekle()
        elif secim=="2":
            gorev_listele()
        elif secim=="3":
            gorev_tamamla()
        elif secim=="4":
            gorev_sil()
        elif secim =="5":
            print("cikis yapiliyor...")
            break
        else:
            print("gecersiz secim yaptiniz")
ana_menu()
    