liste=[]
devamMi=True
while devamMi:
    sayi=int(input("sayi giriniz : "))
    if sayi==0:
        devamMi=False
    else:    
        liste.append(sayi)
        print(liste)

top=0
for eleman in liste: # listenin 0.elemanı ,1.elemanı diye gider
    print(eleman)
    top=top+eleman
print(top)

print("ort : ",top/len(liste))



 
    


