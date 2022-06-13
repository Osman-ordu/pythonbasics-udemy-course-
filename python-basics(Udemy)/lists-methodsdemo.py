# names = ['Ali', 'Yağmur','Hakan','Deniz']
# years = [1998,2000,1998,1987]

# # 1- "Cenk" ismini listenin sonuna ekleyiniz.

# names.append('Cenk')

# # 2- "Sena" değerini listenin başına ekleyiniz.

# names.insert(0,'Sena')

# # 3- "Deniz" ismini listeden siliniz.

# names.remove('Deniz')
#                   # names.pop() # listenin en sonundan bir eleman siler komut vermediğimizde

# # 4- "Ali" listenin bir elemanımıdır?

# result = 'Ali' in names
# print(result)

# # ?- Cenk isminin indeksi nedir?
 
# index = names.index('Cenk')
# print(index)
# # 5-  Liste elemanlarını ters çevirin? 

# names.reverse()
# print(names)
# # 6-  Liste elemanlarını alfabetik olarak sıralayın.

# names.sort()
# print(names)

# # 7-  years listesini rakamsal büyüklüğe göre sıralayın.

# years.sort()
# print(years)

# # 8-  str = "Chevrolet,Dacia" karakter dizisini listeye çevirin.

# str = "Chevrolet,Dacia"
# result = str.split(',')
# print(result)

# # 9-  years dizisinin en büyük ve en küçük elemanı nedir.

# max = max(years)
# min = min(years)
# print(max, min)
# # 10- years dizisinde kaç tane 1998 değeri vardır.

# print(years.count(1998))

# # 11- years elemanlarını ters çevirin.

# years.reverse
# print(years)

# # 12- years dizisinin tüm elemanlarını siliniz.

# years.clear()
# print(years)
# # 13- kullanıcıdan alacağınız 3 marka bilgisini listede saklayınız.

# markalar = []

# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# print(markalar)