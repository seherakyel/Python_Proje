isim="Ahmet"
for harf in isim:
      print(harf)

demet=(1,2,3,4,5,6,)
for sayi in demet:
    print(sayi)


for i in range(0,10): # range(0,10) ifadesi 0 dan 10 a kadar(10 dahil değil) sayıları gösterir 
    print(i)


for k in range (1,17,2): # ilk aralık:başlangıç değeri(dahil) ikinci aralık:son değer(dahil değil) 
# #üçüncü aralık:artış değeridir
    print(k)


sonuc=1
for i in range(0,10):
     sonuc*=2  # aynı zamanda sonuc=sonuc*2 demek de oluyor
     print(sonuc) 


liste1=["a","b","c"]
liste2=[1,2,3]
for harf in liste1:
    for rakam in liste2: # bunun içindeki bittiğinde yukarı çıkılır ve yeni değer alınır
        print(harf,rakam)


Liste=[1,2,3,4,5,6,7,8,9]
for i in Liste:
      if i==3:
         continue # print("3'ü atladik")
print(i)


Liste1=[10,20,30,40,50,60,70,80,90]
for k in Liste1:
    if k==50:
        break  # print("50 ve 50'den sonrası yok")
    print(k)


Liste=range(100)
for i in Liste:
    if i%3 !=0:
        continue
    print(i)


for k in Liste:
    if k==8:
        break
    print(k)


x=2
while x<10:
     print(x)
     x +=1 # x=x+1


x=2
y=3
while x+y<1000:
   print(x,y)
   x +=2 # x=x+2
   y +=2 # y=y+2


 #i=1
 #while True:
 #   print(i)
 #     i +=1 # i=i+1
  #   if i==1000:
  #       break


i=1
while True:
    if i%2==0:
        i +=1
        continue
    print(i)
    i +=1
    if i==1000:
        break
        







  

