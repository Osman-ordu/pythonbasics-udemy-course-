# # 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdir(kelime, adet):
#     print(kelime*adet)

# yazdir('merhaba\n',10)    

# # 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye alalım.

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste  

# result=listeyeCevir(10,20,30,'merhaba')

# print(result)

# # 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulalım.



# def asalSayilaribul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
# sayi1=int(input('İLK SAYİYİ GİRİNİZ: '))
# sayi2=int(input('İKİNCİ SAYİYİ GİRİNİZ: '))


# asalSayilaribul(sayi1, sayi2)


# # 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde yazalım. 

# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2,sayi):
#         if (sayi % i ==0 ):
#             tamBolenler.append(i)

#     return tamBolenler

# print(tamBolenleriBul(20))    