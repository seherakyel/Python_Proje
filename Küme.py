#TUPLES(DEMET)
demet=("sari","mavi","yesil","kirmizi","siyah")
print(demet)
print(len(demet))
print(demet[2])
print(demet[0])



#SET(KÜME)
kume={"sari","mavi","yesil","kirmizi","siyah","gri"}
print(kume)
print(len(kume))
#print(kume[3]) > bunu bu şekilde yazamayız kümelerde indeksleme yoktur çünkü kümeler sıralı değildir
kume.add("pembe") # rengi kümeye rastgele ekler
print(kume)
kume.remove("sari") # sariyi kümeden çıkarır 
print(kume)
kume.discard("turuncu") # discard da rengi kümeden çıkarır removeden farkı çıkarmak istediği
# renk kümede olmasa bile kümenin son halini yazar
print(kume)


kume1={1,2,3,4,5}
kume2={1,2,3,6,7}
print(kume1.intersection(kume2)) # kume1 ve kume2 nin kesişimini ifde eder
print(kume1.union(kume2)) # kume1 ve kume2 nin birleşimini ifade eder
print(kume1.difference(kume2)) # kume1 de olup kume2 de olmayan
print(kume2.difference(kume1)) # kume2 de olup kume1 de olmayan
print(1 in kume1) # kume1 de 1 elemanı var mı varsa true yoksa false
print(8 in kume2.union(kume1)) # kume1 ve kume2 nin birleşiminde 8 var mı varsa true yoksa false

python=set("PYTHON")
print(python)

###NOT
bosListe1=[]
bosListe2=list()

bosDemet1=()
bosDemet2=tuple()

bosKume1=set()
bosKume2={} # bu bos kume ifade etmez bi sözlüktür daha sonra işlenecek








