"""
                                          \\\\\  S   O   R   U   -    C   E   V   A   P   //////
"""
x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z değerlerinin toplamının farkı nedir?


sayi1 = int(input('1.sayi: '))
sayi2 = int(input('2.sayi: '))
moddemo = x + y + z
toplamın_farki =(sayi1*sayi2)-(int(moddemo))
print(toplamın_farki)

# 2- y'nin x'e kalansız bölümünü hesaplayınız?

result = x // y
print(result)


# 3- (x,y,z) toplamının mod 3'ü nedir?

moddemo = x+y+z
result = moddemo % 3
print(result)


# 4- y'nin x. kuvvetini hesaplayınız?

kuvvet = y**x
print(kuvvet)

# 5- x, *y, z = numbers işlemine göre z'nin küpünü hesaplayınız?


x, *y, z = numbers
result = z**3
print(result)




# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

x, *y, z = numbers
print(y)

# Y değerleri şunlardır = [5 7 10]

result = y[0] + y[1] + y[2]
print(result)