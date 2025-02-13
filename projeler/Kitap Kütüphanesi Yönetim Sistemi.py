

book1={"name":"1984","total":5,"category":"political"}
book2={"name":"Fareler ve Insanlar","total":2,"category":"tragedy"}
book3={"name":"Seker Portakali","total":0,"category":"fiction"}

books = {
    "book1": book1,
    "book2": book2,
    "book3": book3
}

while True:
    print("1:kitap ekle veya arttir")
    print("2:kitap cikar veya azalt")
    print("3:kitaplari listele")
    print("4:kitap ara")

    vote=input("secim yapin : ")

    if vote=="1":
        book_name1=input("eklemek istediginiz kitabin adini girin :")
        if book_name1 in books:
            books[book_name1]["total"] += 1
        else:
            category=input("kitabin kategorisini girin :")
            total=int(input("kitap adedini girin :"))
            books[book_name1] = {"name": book_name1, "total": total, "category": category}
            print("guncel kitap listesi :", books)

    elif vote=="2":
        book_name2=input("cikarmak istedigin kitap adini girin : ")
        book_total=int(input("cikarmak istedigin kitap adedi girin : "))
        category=input("kitabin kategorisini girin :")
        if book_name2 in books and total>book_total:
            books[book_name2]["total"]-=book_total 
            print("guncel kitap listesi :", books)

        else:
            print("cikarmak istedigin kitap zaten yok ")


        

            

           
    
    
    
