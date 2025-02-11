
# 01 list comprehension ile yazılmadan önce sayıları yazdırma
numbers=[1,2,3,4,5,6,7,8,9]
list=[]
for number in numbers:
    list.append(number)
print(list)

     # list comprehension ile yazılması 
list1=[number for number in numbers]
print(list1)



# 02 verilen listedeki çift rakamlardan bir liste oluşturalım
list2=[]
for number in numbers:
    if number%2==0:
        list2.append(number)
print(list2)

     # list comprehension ile yazılması 
list3=[number for number in numbers if number%2==0]
print(list3)



# 03 verilen listedeki çift rakamların karelerinden oluşan bir liste oluşturalım
list4=[]
for number in numbers:
    if number%2==0:
        list4.append(number**2)
print(list4)

      # list comprehension ile yazılması 
list5=[number*number for number in numbers if number%2==0]
print(list5)



# 04 verilen listedeki 4 ten büyük sayıların karelerinden oluşan bir liste oluşturalım
list6=[]
for number in numbers:
    if number>4 and number%2==0:
        list6.append(number*number)
print(list6)

       # list comprehension ile yazılması 
list7=[number**2 for number in numbers if number>4 and number%2==0]
print(list7)



# 05 (1,a),(1,b),(1,c),(1,d),(2,a),(2,b),(2,c),(2,d)...biçiminde ikililerden oluşan bir liste
numbers=[1,2,3,4]
letters="abcd"
list8=[]
for number in numbers:
    for letter in letters:
        list8.append((number,letter))
print(list8)

      # list comprehension ile yazılması 
list9=[(number,letter) for number in numbers for letter in letters]
print(list9)



# 06 birinci listede bulunup ikinci listede bulunmayan rakamların karesinden oluşan bir liste oluşturalım
list10=[1,2,3,4,5,6,7,8,9]
list11=[2,3,6,9,5]
list12=[]
for i in list10:
    if i not in list11:
        list12.append(i*i)
print(list12)

       
       
       # list comprehension ile yazılması 
list13=[i*i for i in list10 if i not in list11]
print(list13)



# 07 verilen listeden elemanları tek tek alan [1,2,3,4,5,6,7,8,9,10,11,12] biçiminde liste oluşturalım
list_=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list2=[]
for i in list_:
    for j in i:
        list2.append(j)
print(list2)

        # list comprehension ile yazılması 
liste=[j for i in list_ for j in i]
print(liste)



