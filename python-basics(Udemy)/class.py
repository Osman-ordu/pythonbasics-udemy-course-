# # class

# # class Person:
# #    # class  attributes
# #   address = 'no information'
# #    # constructor (yapıcı metod)
# #   def __init__(self, name ,year):                             # __init__ metodu
    
# #      # object attributes

# #      self.name = name
# #      self.year = year
# #      print('init metodu calisti')

# #    # instance methods . example**
# #   def intro(self):
# #     print('Hello There. I am '+ self.name)

# #   # instance methods. example**
# #   def calculateAge(self):
# #     return 2021 - self.year  

# # # object , instance 
# # p1 = Person('ali', 1990)
# # p2 = Person('yagmur',1995)

# # p1.intro()
# # p2.intro()

# # print(f'adım: {p1.name} yaşım: {p1.calculateAge()}')
# # print(f'adım: {p2.name} yaşım: {p2.calculateAge()}')
# # print(p1)
# # print(p2)

# class Circle:
#   # class object attribute
#   pi = 3.14

#   def __init__(self, yaricap=1):
#     self.yaricap = yaricap

#   def cevre_hesapla(self):
  
#     return 2*self.pi * self.yaricap
  

#   def alan_hesapla(self):
#     return self.pi * (self.yaricap**2)


# c1= Circle() # yaricap =1
# c2= Circle (5)   


  
# print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla}")
# print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla}")