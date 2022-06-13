# # 1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# #    ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
# """
# name=input('name: ')
# age=int(input('age: '))
# college=input('college: ')


# if age>=18:
#     if (college=='lise') or (college=='üniversite'):
#         print(f'{name}ehliyet Alabilirsin.')
#     else:
#         print(f'{name}ehliyet alamazsın mezuniyet durumun yetersiz.')
# else:
#     print(f'{name} ehliyet alamazsın yaşın yaşın tutmuyor.')
# """
# # 2- Bir yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not bilgisini yazdırınız.
# #  0-24 => 0
# #  25-44=> 1
# #  45-54=> 2
# #  55-69=> 3
# #  70-84=> 4
# #  85-100=>5

# yazılı =float(input('yazılı:'))
# sözlü =float(input('sözlü: '))
# ortalama=(yazılı+sözlü)/2

# if(ortalama >=0) and (ortalama <=24):
#     print('not: 0')

# elif(ortalama >=25) and (ortalama <=44):
#     print('not: 1')

# elif(ortalama >=45) and (ortalama <=54):
#     print('not: 2')

# elif(ortalama >=55) and (ortalama <=69):
#     print('not: 3')

# elif(ortalama >=70) and (ortalama <=84):
#     print('not: 4')

# elif(ortalama >=85) and (ortalama <=100):
#     print('not: 5')

# else:
#     print('yanlış bilgi girdiniz..')
# # 3- Trafiğe çıkış tarihi alınan aracın servis zamanını aşağıdaki bilgilere göre sıralayınız.
# #   1.Bakım => 1.yıl
# #   2.Bakım => 2.yıl
# #   3.Bakım => 3.yıl
# # süre hesabını alınan gün ay yıl bilgisine gün bazlı hesaplayınız.
# # datetime modülünü kullanmanız gerekiyor.
# # (simdi) - (2018/8/1) => gün
#     import datetime

# tarih=input('aracınız hangi tarihte trafiğe çıktı: ')

# if days>=365:
#         print('1.Servis aralığı')
# elif (days>365) and (days<=365*2):
#         print('2.Servis aralığı')
# elif (days>365*2) and (days<=365*3):
#         print('3.Servis aralığı')
# elif (days>365*3) and (days<=365*4):
#         print('4.Servis aralığı')
# else:
#         print('hata!! yanlış bilgi girdiniz...')
