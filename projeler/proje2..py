
   # Ekrandan alınan bir sayının asal olup olmadığını kontrol eden bir program yazınınz
# sayi=int(input("bi sayi gitiniz : "))
# devamMi:True
# for i in range(2,sayi):
#     if sayi%i==0:
#         devamMi=False
#         break

#     if devamMi==True:
#       print(f"{sayi} sayisi asaldir")
#     else:
#        (f"{sayi} sayisi asal degilidir")



   # Ekranda alınan bir sayının kaç tane pozitif böleni olduğunu bulan bir prog yazınız
# sayi=int(input("bir sayi giriniz : "))
# bölen_sayisi=0
# for i in range(1,sayi+1):
#    if sayi%i==0:
#       bölen_sayisi+=1
# print(f"{sayi} sayisinin {bölen_sayisi} tane bölen sayisi vardir")
      
   
   
   # Ekranda okunan bir sayının rakamları toplamını hesaplayan bir prog yazınız
# sayi1=int(input("bir sayi giriniz : "))
# toplam=0
# gecici_sayi=sayi1
# while gecici_sayi !=0 :
#    basamak=gecici_sayi%10
#    toplam +=basamak
#    gecici_sayi //=10
# print("rakamlar toplamı : " toplam)



   # Ekranda peşpeşe okunan 5 sayının en küçüğü ve en büyüğünü yazdıran prog yazınız 
# list=[]
# for i in range(5):
#    sayi2=int(input("sayi gir : "))
#    list.append(sayi2)
# print("en buyuk : ",{max(list)})
# print("en kucuk : ", {min(list)})



   # Ekranda okunan bir sayının herhangi bir sayunın karesi olup olmadığını kontrol eden prog yazınız
# sayi3=int(input("sayi giriniz : "))
# karekok=sayi3**0,5
# if karekok.is_integer():
#    print("tamkare dir")
# else:
#    print(" tamkare değildir")



   # Ekranda okunan bir metin hangi hangi harfin kaç tane kullanıldığını gösteren bir prog yazınız
# metin=input("bir metin giriniz : ")
# sözlük=dict()
# for harf in metin :
#     if harf in sözlük:
#         sözlük[harf]+=1
#     else:
#         sözlük[harf]=1

# for harf,adet in sözlük.items():
#     print(harf,adet)



# Ekranda okunan bir metinde a harflerini büyük yazan bir prog yazınız
# metin1=input("bir metin giriniz : ")
# metin2=" "
# for harf in metin1 :
#     if harf=="a":
#         metin2 +="A"
#     else:
#         metin2 +=harf
# print(metin2)



# ilk 10,000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter 
# prime_list=list()
# prime_list.append(2)
# sayi=3
# while  len(prime_list) < 10000:
#     prime=True
#     for i in range(2,int(sayi**0.5)+1):
#        if sayi%i==0:
#            prime=False
#            break
#        if prime:
#            prime_list.append(sayi)
#            if len(prime_list)==10000:
#                break
#            sayi+=1
# liste2=[]
# for prime in prime_list:
#     strprime=str(prime)
#     if strprime.startswith("3") and strprime.endswith("7"):
#         liste2.append(prime)
# print(liste2)
# print(len(liste2))



# 3 basamaklı sayıların kaç tanesi rakamlarının küplernin toplamına eşittir
# liste=[]
# for sayi in range(100,1000):
#     toplam=0
#     gecici_sayi=sayi
#     while gecici_sayi!=0:
#         basamak=gecici_sayi%10
#         toplam+=basamak**3
#         gecici_sayi//=10
#     if toplam==sayi:
#      liste.append(sayi)
# print(liste)
# print(len(liste))



 # ilk 100 fibonacci sayı dizisini yazınız(while ile)
# fibonacci_list=[]
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# index=2

# while True:
#     fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#     index+=1
#     if len(fibonacci_list)==100:
#         break
    
# print(fibonacci_list)



# 100 basamkalı ilk fibonacci sayısını ekrana yazınız 
# fibonacci_list=[]
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# index=2

# while True:
#     fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#     terim=fibonacci_list[index-2]+fibonacci_list[index-1]
#     if len(str(terim))==100:
#         print(terim)
#         print(index)
#         break
#     index+=1   




     # Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python  Örneği
# toplam=0
# sayi1=int(input("sayi1 i giriniz : "))
# sayi2=int(input("sayi2 i giriniz : "))
# for i in range(sayi1+1,sayi2):
#     toplam +=i
# print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))
 
     
    
         


