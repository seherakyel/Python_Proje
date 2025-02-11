x = 10
y = 10
if x == y:
    print("x = y'dir")
else:
    print("x != y'dir")
    

a = 5
b = 7
if a == b:
    print("a = b")
if a < b:
    print("a < b")


renk="pembe"
if renk=="beyaz":
   print("beyaz")
elif renk=="sari":
   print("sari")
elif renk=="mavi":
   print("mavi")
else:
   print("hicbiri")


k=5
m=8
n=10
if k<n or m>k: # or=veya kosullardan herhangi biri doğru olduğunda (k<n or m>k) true tanımını alır 
    print("kosul dogru")
else:
    print("kosul yanlis")


v=50
q=8
d=10
if v<q and q<d : # and=ve kosullardan herhangi biri değeri yanlış olduğunda (v<q and q<d) false tanımını alır
    print("kosul dogru")
else:
    print("kosul yanlis")


t=41
p=3
if not t==p: # t ve p birbirne eşit olmadığı için (41!=3 ) bu doğru kabul edilir
    print("kosul doğru")
else:
    print("kosul yanlis")


Liste=[1,2,3,4,5,6,7,8,9]
c=4
if c in Liste: # c listede var mı diyor varsa true kabul edilir içindeki yazılır
    print("listede var")
else:
    print("listede yok")




    