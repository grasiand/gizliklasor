import os
Grasiand
print("""

KULLANICI GİRİŞ EKRANI
(Grasiand)

""")

sys_username = "istediginiz kullanici adi"
sys_password = "istediginiz sifre"

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
    os.system("start C:\\Users\\kullanici ismi\\gizlediğiniz klasor ismi")
