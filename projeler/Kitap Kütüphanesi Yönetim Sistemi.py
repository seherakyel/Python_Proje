
books = {
    "book1": {"name": "1984", "total": 5, "category": "political"},
    "book2": {"name": "Fareler ve Insanlar", "total": 2, "category": "tragedy"},
    "book3": {"name": "Seker Portakali", "total": 0, "category": "fiction"},
    "book4": {"name": "Kurk Mantolu Madonna", "total": 3, "category": "romance"},
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

        book_key = None  
        for i in books:  
            if books[i]["name"] == book_name2:  
                book_key = i
                break  

        if book_key in books and books[book_key]["total"] > book_total:
            books[book_key]["total"]-=book_total 
            print("guncel kitap listesi :", books)

        else:
            print("cikarmak istedigin kitap zaten yok ")

    elif vote=="3":
        print("kitap listesi :", books)
    
    elif vote=="4":
        book_name3=input("aramak istediginiz kitabin adini girin :")
        for i in books:
            if books[i]["name"] == book_name3:
                print("kitap adi :", books[i]["name"])
                print("kitap adedi :", books[i]["total"])
                print("kitap kategorisi :", books[i]["category"])
                break
        else:
            print("kitap bulunamadi")