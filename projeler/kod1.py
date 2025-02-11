
#Proje de kullanıcı 3 tane değer girecek 1 2 3 diye 
#1 girerse kullanıcının listesindeki görevler terminale yazılacak
#2 girerse görev listesine görev eklicek
#3 girerse görev listesinden ismini veya indexini verdiği görev silinecek

gorev_listesi=[]

while True:
    print("1:gorevleri goster")
    print("2:gorev ekle")
    print("3:gorevi sil")

    secim=input("secim yap :")

    if secim=="1":
        if not gorev_listesi:
            print("gorev listeniz bos")
        else:
            print("gorev listeleniyor")
            for index, gorev in enumerate(gorev_listesi):#bu fonksiyon o listenin elemanlarını her biri bir indeks ve eleman çifti olacak şekilde döndürür
             print(f"{index}: {gorev}")
        print("Güncel görev listesi:", gorev_listesi)

    elif secim=="2":
       eklemek_istedigin_gorev=input("eklemek istedigin gorevin adini girin :")
       gorev_listesi.append(eklemek_istedigin_gorev)
       print("Görev listesine eklendi:", gorev_listesi)
    
    elif secim=="3":
       silmek_istedigin_gorev=input("silmek istedigin gorevin adini girin :")
       if silmek_istedigin_gorev in gorev_listesi:
         gorev_listesi.remove(silmek_istedigin_gorev)
         print("Görev listesine eklendi:", gorev_listesi)
       else:
         print("silmek istedigin görev bulunamadi !")

    elif secim=="q":
         print("program solandiriliyor...")
         break

    else:
        print("gecersiz secim yaptiniz !")

