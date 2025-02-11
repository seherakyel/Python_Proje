
# try bloğunun içindeki kod herhangi bir hata almadı o yüzden except bloğunu atlayıp kaldığı yerden 
# devam eder
try:
    a=5
    b=8
    c=a/b
except:
    print("bir hata oluştu")
print(a,b,c,sep="-")



try:
    a=10
    b=50
    c=a/b
    d=x
except: # hata varsa except bloğunu içindeki yazılıp devam eder aynı şekilde 
    print("bir hata oluştu")
    print("hatayi düzelten kodlar çalismali ")
print(a,b,c,sep="*")



try:
    k=6
    l=5
    m=k/l
    n=3
    isim="Ali"
    karakter=isim[10]
except ZeroDivisionError:
    print("paydada sifir olmamamli")
except NameError:
    print("degisken daha önce tanimlanmamis")
except IndexError:
    print("böyle bir index bulunmuyor")
except Exception: # herhangi bir hata oluştuğunda çalışacaktır
    print("bilinmeyen hata olustu")
else: # hata olmadığında çalışır 
    print("else bloğu çalişiyor")
finally: # hata var veya yok her türlü çalışır
    print("finally bloğu çalişiyor")




