

class calisan:
    def __init__(self,name,surname,age): # type: ignore
                self.name=name
                self.surname=surname
                self.age=age

calisan1=calisan("Ali","Veli",20)
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2=calisan("Seher","Akyel",19)
print(calisan2.name,calisan2.surname,calisan2.age)




class calisan:
    def __init__(self,name,surname,age): # type: ignore
                self.name=name
                self.surname=surname
                self.age=age
    def show_info(self):
            print(f"ad:{self.name}  soyad:{self.surname}  yaş:{self.age}")

calisan1=calisan("Ali","Veli",20)
# print(calisan1.name,calisan1.surname,calisan1.age)
calisan1.show_info()

calisan2=calisan("Seher","Akyel",19)
# print(calisan2.name,calisan2.surname,calisan2.age)
calisan2.show_info()





class urun:
        def __init__(self,ü_adi,ü_adedi="girilmedi",ü_fiyati=400):
                self.ü_adi=ü_adi
                self.ü_adedi=ü_adedi
                self.ü_fiyati=ü_fiyati
        def show_info(self):
                print(f"Ad:{self.ü_adi}  Adet:{self.ü_adedi}  Fiyat:{self.ü_fiyati}")
                
urun1=urun("girilmedi",64,560)
urun1.show_info()
urun2=urun("fasulye",82,450)
urun2.show_info()

                
                
         


    
