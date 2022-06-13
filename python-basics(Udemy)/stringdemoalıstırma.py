# # website = 'http://www.sadikturan.com'
# # course = 'python kursu: Baştan sona python programlam rehberiniz (40 saat)'

# # 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?#

# # len(course)
# # print(len(course))
#  # cevap : 64

# # 2-'website içinden www karakterlerini alın.#

# # website[10:]
# # print(website[10:])

# # 3-'website içinden com karakterlerini alın.#

# # website[-3:]
# # print(website[:-3])

# # 4-'course' içinden ilk 15 ve son 15 karakterlerini alın.

# # result = course[0:15]
# # result = course[:15]
# # result = course[-15:]

# # 5-'course' ifadesindeki karakterleri tersten yazdırın.

# result ="course"
# print(result[::-1])
# """"
# s='12345'


# name, surname, age, job ="bora","yılmaz",32,"mühendis"


# # yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# # 'benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis.'

# # result ="benim adım "+ name+ " " + surname+ ", yaşım "+ str(age) + " ve mesleğim"+ mühendis
# result="benim adım {} {}, yaşım {} ve mesleğim {}".format(name,surname,age,job)
# result=f'benim adım {name} {surname}, yaşım {age} ve mesleğim {job}'

# # "hello world" ifadesindeki w harfini 'W' ile değiştirin.

# s ="hello world"
# s = s[0:6] + 'W'+s[-4:]
# s.replace('w','W')

# # yada .replace fonksyonunu kullanarak bunu kısayoldan yapabiliriz , bir karakter aratıp onun yerine yanındaki karakteri ekler.


# # abc ifadesini yan yana 3 defa yazdıralım.

# print(' abc '* 3)
# """