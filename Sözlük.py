kisi={"isim":"ali","yas":20,"cinsiyet":"erkek","hobiler":["tiyatro","sinema","dizi izlemek"]}
print(kisi)
print(kisi["isim"])
print(kisi["hobiler"])
kisi["isim"]="ahmet" # isim anahtarının değerini değiştirdi aliyken ahmet oldu
print(kisi)
kisi.update({"isim":"cemil","yas":34}) # birden fazla değişiklik yapmak için 
print(kisi)
kisi["id"]=1234 # kisi sözlüğüne "id" anahtarının değeriyle beraber ekler
print(kisi)
del kisi["cinsiyet"] # sözlükten cinsiyet anahatrını değeriyle beraber sildi
print(kisi)


print(kisi.keys()) # sadece anahtarları gösterir
print(kisi.values()) # sadece değerleri gösterir
print(kisi.items()) # anathar ve değer çiftini beraber yazar
print(kisi.get("isim")) # isim anahtarına karşılık gelen değeri yazar 
print(kisi.get("soyad")) # soyad anahtarı bulunmadğı için değeri yazmaz ama hata da vermez none döndürür
print(kisi.get("soyad","bulunamadı")) # soyada karşlık gelen değer olmadığı için get metodunun 
#2.parametresi olan bulunamadı nı döndürür