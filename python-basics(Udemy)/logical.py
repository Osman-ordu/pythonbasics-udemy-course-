# # 1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz?

# girilen_sayi=int(input('Bir Sayı Giriniz: '))
# if girilen_sayi < 100 and girilen_sayi > 0:
#     print('GİRMİŞ OLDUĞUNUZ SAYI SIFIR 100 ARASINDA BİR SAYIDIR')

# elif girilen_sayi > 100 or girilen_sayi < 0:
#     print('GİRMİŞ OLDUĞUNUZ SAYI SIFIR 100 ARASINDA DEGİLDİR')

# # 2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz?

# pozitifciftsayı=int(input('Bir sayi giriniz: '))

# result =(pozitifciftsayı > 0) and (pozitifciftsayı ==0) or (pozitifciftsayı % 2==0)
 
# print(f'girilen değer pozitif çift sayıdır: {result}')


# # 3-Email ve parola bilgileri ile giriş kontrolü yapınız?

# email= ('osmnord@gmail.com')
# parola= ('sadece1')

# kullanıcıemail=(input('Email adresinizi giriniz: '))
# kullanıcıparola=(input('Parola giriniz: '))

# form= (kullanıcıemail == email) and (kullanıcıparola==parola)

# print(f'girilen parola bilgisi: {form} ')

# # 4-Girilen 3 sayıyı büyüklük olarak karşılaştırınız?

# a=int(input('SAYI1: '))
# b=int(input('SAYI2: '))
# c=int(input('SAYI3: '))

# a > b and a > c
# b > a and b > c
# c > a and c > b

# result = (c > a) and (c > b)

# print(f'c en büyük sayıdır: {result}')

# # 5-Kullanıcıdan 2 vize (½60) ve final (½40) notunu alıp ortalama hesaplayınız?
#    # ****Eğer ortalama 50 ve üstündeyse geçti , değilse kaldı yazdırın.****

# #<<<<<<<<    -       -        -          -           -          -        -         >>>>>>>>   
#      #       A) Eğer ortalama 50 olsa bile final notu en az 50 olmalıdır.!!!!!!!!!!
#      #       B) Finalden 70 alındığında ortalamanın önemi olmasın.!!!!!!!!!!


# vize1=float(input('vize 1 : '))
# vize2=float(input('vize 2 : '))
# final=float(input('final : '))

# ortalama= ((vize1+vize2)//2)*0.6 + (final*0.4)
# result = (ortalama>=50) and (final>=50) # bizden istenilen koşul bir
# result = (ortalama>=50) or (final>=70) # bizden istenilen koşul iki
# print(f'Öğrencinin ortalaması: {ortalama} Dersten geçme durumu:{result}')


# # 6-Kişinin ad , kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    # ****formül (kilo/boy uzunluğunun karesi)****
#         # Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#         # 0-18.4 => Zayıf
#         # 18.5-24.9 => Normal
#         # 25.0-29.9 => Fazla kilolu
#         # 30.0-34.9 => Şişman (obez) 
        
# name = input('NAME: ')
# kg = float(input('KG: '))
# hg = float(input('HG: '))

# index = (kg) / (hg ** 2)
# zayıf = (index>=0) and (index <= 18.4)
# normal =(index >= 18.5) and (index <=24.9)
# fazla_kilolu =(index >= 25.0) and (index<=29.9)
# sisman_obezite=(index >= 30.0) and (index<=36.9)

# print(f' {name} KİLO ENDEKSİN: {index} DEĞERLENDİRMEN ZAYIF: {zayıf}')
# print(f' {name} KİLO ENDEKSİN: {index} DEĞERLENDİRMEN NORMAL: {normal}')
# print(f' {name} KİLO ENDEKSİN: {index} DEĞERLENDİRMEN FAZLA KİLOLU: {fazla_kilolu}')
# print(f' {name} KİLO ENDEKSİN: {index} DEĞERLENDİRMEN ŞİŞMAN OBEZİTE: {sisman_obezite}')





