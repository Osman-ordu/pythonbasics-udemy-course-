

# website= "http://www.sadikturan.com"
# course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"


# # 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# result='Hello World'.strip()
# result=='Hello World'.lstrip() # sadece soldan silmek istersek LEFTSTRİP
# result='Hello World'.rstrip() # sadece sağdan silmek istersek RİGHTSTRİP metodunu kullanabiliriz.

# # 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

# result = website.lstrip('/:htp') #sadece soldan silmek için LEFT kısaltması L metodu
# result = website.strip('m.co:/htpw')

# # 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

# course = course.lower()
# print(course)


# # 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))

# result = website.count('a')
# result = website.count('www')

# # 5- 'website' www' ile başlayıp com ile bitiyormu?


# # 6- 'website' içinde '.com' ifadesi varmı?

# result = website.find('.com')
# result = website.index('.com')
# print(result)



# # 7- 'course' içindeki karakterlerin hepsi alfabetikmi? (isalpha,isdigit)

# result = course.isalpha()
# result = course.isdigit()

# print(result)

# # 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# result = 'contents'.center(50,'*')


# # 9- 'course' karakter dizisindeki tüm boşluk karakterlerini  '-' ile değiştirelim.

# result = course.replace(' ','-')
# print(result)

# # 10- 'Hello World' olan karakter dizisinde'ki "World"ü değiştirip "there" yapın.

# result = 'Hello World'.replace('World','there')
# print(result)