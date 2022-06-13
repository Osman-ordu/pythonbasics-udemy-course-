# # Bankamatik uygulaması (geliştirilebilir) 

# SadikHesap = {
#     'ad':'Sadık Turan',
#     'hesapNo':'13245678',
#     'bakiye': 3000,
#     'ekhesap': 2000
# }

# AliHesap = {
#     'ad':'Ali Turan',
#     'hesapNo':'12345678',
#     'bakiye': 2000,
#     'ekhesap': 1000
# }

# def paraCek(hesap, miktar):
#     print(f"Merhaba{hesap['ad']}")

#     if hesap['bakiye'] >= miktar:
#         hesap['bakiye'] -= miktar 
#         print('paranızı alabilirsiniz...')
#         bakiyeSorgula(SadikHesap, 2000)
#     else:
#         toplam = hesap['bakiye'] + hesap ['ekhesap']

#         if (toplam >= miktar):
#             ekHesapKullanimi = input ('ek hesap kullanilsinmi (e/h) ')
#             if ekHesapKullanimi == 'e':

#                 ekhesapKullanilacakMiktar = miktar - hesap
#                 hesap['bakiye'] = 0
#                 hesap['ekHesap'] -= ekhesapKullanilacakMiktar
#                 print('paranızı alabilirsiniz.')
#                 bakiyeSorgula(SadikHesap, 2000) 
#             else:
#                 print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadir..")     
#         else:
#             print('üzgünüz bakiye yetersiz.')
#             bakiyeSorgula(SadikHesap, 2000)

# def bakiyeSorgula(hesap):
#     print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise  {hesap['ekHesap']} TL bulunmaktadır." )


# (paraCek(SadikHesap, 3000))

# print('******************')

# (paraCek(SadikHesap, 3000))














