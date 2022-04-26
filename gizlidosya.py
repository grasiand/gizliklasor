__author__      = "Grasiand"
import os

print("""

KULLANICI GİRİŞ EKRANI
(Grasiand)

""")

sys_username = "Grasiand"
sys_password = "Grasiand"

kullanici_adi = input("Kullanıcı Adını Giriniz: ")
sifre = input("Şifre'yi Giriniz: ")

if (kullanici_adi == sys_username) and (sifre != sys_password):
    print("Şifre yanlış..")

elif (kullanici_adi != sys_username) and (sifre == sys_password):
    print("Kullanıcı adı yanlış..")

elif (kullanici_adi != sys_username) and (sifre != sys_password):
    print("Kullanıcı adı ve şifre yanlış..")
else:
    print("Giriş yapıldı!")
    os.system("start C:\\Users\\Kullanıcı ismi\\gizlediğiniz klasor ismi")
