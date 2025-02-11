

book1={"1""name":"1984","total":5,"category":"political"}
book2={"name":"Fareler ve Insanlar","total":2,"category":"tragedy"}
book3={"name":"Seker Portakali","total":0,"category":"fiction"}

books = {
    "book1": book1,
    "book2": book2,
    "book3": book3
}
swi
while True:
    add_book=input("eklemek istedigin kitap")
    if add_book in books:
        print(f"{add_book} kitap zaten var")
    else:
        book_name=input("kitabin ismini girin")
        book_total=input("kitabin adetini girin")
        book_category=input("kitabin kategorisini girin")
        add_book={"name":book_name,"total":book_total,"category":book_category}
    
