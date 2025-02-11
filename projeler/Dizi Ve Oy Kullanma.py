
#Bir sinema salonu, vizyondaki diziler için bir oylama sistemi geliştirmek istiyor
#Kullanıcılardan diziler hakkında oylar toplanacak ve en çok oylanan diziler listelenecek

series={"Breaking Bad":0,"Game Of Thrones":0,"Stranger Things":0,"Friends":0,"Prison Break":0}

while True:
    print("Dizi listesini goster : ",series)
    user=input("oy vermek istedigin dizi hangisi : ")

    if user in series:
        print(f"{user} oy vermek istedigi dizi:{series}")
        series[user]+=1
    elif user=="q":
        print("program sonlaniyor")
        break
    else:
        print("boyle bi dizi bulunamadi .")
