renkler=["siyah","beyaz","sarı","mavi","yeşil"]
print(renkler)
print(renkler[1]) # 0=siyah,1=beyaz,2=sarı,3=mavi,4=yeşil
print(renkler[0])
print(renkler[2:]) # 2.indexten başlayıp sona kadar
print(renkler[1:4]) # 1.index dahil olmakla birlikte 4.indexe kadar yalnız 4.index dahil değil 
print(renkler[::2]) # 0.index dahil ve 2 şer  gider


renkler.append("gri") # renkler listesine yazılan rengi de sona ekler 
print(renkler)
renkler.insert(0,"mor") # 0.indexe mor rengini yerleştirir
print(renkler)
renkler.remove("sarı") # yazdığı rengi listeden siler 
print(renkler)
renkler2=["turuncu","kırmızı"]
#renkler.append(renkler2)
#print(renkler)
renkler.extend(renkler2)
print(renkler)
renkler.pop() # en son elemanı siler
print(renkler)
renkler.reverse() # listeyi ters çalıştırır
print(renkler)
renkler.sort() # stringli yapıları alfabetik sıralar intli yapıları büyükten küçüğe sıralar
print(renkler)
# listenin en son hali > renkler=["beyaz","gri","mavi","mor","siyah","turuncu","yeşil"]
sayilar=[1,2,39,4,3,7,8]
print(min(renkler)) # alfabetik olarak önce gelen
print(min(sayilar)) # en küçük sayıyı 
print(max(sayilar)) # en büyük sayıyı
print(sum(sayilar)) # listedeki sayıların toplamı
print(list(enumerate(renkler))) # enumerate(0,'beyaz'),(1,'gri'),(2,'mavi'),(3,'mor'),(4,'siyah'),(5,'turuncu'),(6'yeşil') şeklinde listeler
print(list(enumerate(renkler,start=4)))
print("mor" in renkler) # renkler listesinde mor var mı varsa true yoksa false olur
a=" - ".join(renkler) # " " içindeki karakteri renklerin arasına alır 
print(a)
b=" * ".join(renkler)
print(b)
renkler2=a.split(" - ") # - gördüğü yerden bölmek istedi
print(renkler2)
renkler3=a.split("ma")
print(renkler3) # ma yı gördüğü yerden böldü






