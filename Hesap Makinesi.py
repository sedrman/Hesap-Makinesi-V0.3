from math import sqrt
print("""
1.Toplama      yapmak için (toplama)      veya (1) Yazın +
2.Çıkarma      yapmak için (çıkarma)      veya (2) Yazın -
3.Çarpma       yapmak için (çarpma)       veya (3) Yazın x
4.Bölme        yapmak için (bölme)        veya (4) Yazın ÷
5.Üs Alma      yapmak için (üs alma)      veya (5) Yazın ^
6.Mod alma     yapmak için (mod alma)     veya (6) Yazın %
7.Karekök alma yapmak için (karekök alma) veya (7) Yazın √
""")
islem=input("İşleminizi Yazınız: ")
if  islem==("toplama") or islem==("1") or islem==("Toplama"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)+int(y))
    print(" ")
    print(x,"+",y,"=",z)

elif  islem==("çıkarma") or islem==("2") or islem==("Çıkarma"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)-int(y))
    print(" ")
    print(x,"-",y,"=",z)
    
elif  islem==("çarpma") or islem==("3") or islem==("Çarpma"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)*int(y))
    print(" ")
    print(x,"x",y,"=",z)
    
elif  islem==("bölme") or islem==("4") or islem==("Bölme"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)/int(y))
    print(" ")
    print(x,"÷",y,"=",z)

elif  islem==("üs alma") or islem==("5") or islem==("Üs alma") or islem==("Üs") or  islem==("üs") or islem==("Üs Alma"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)**int(y))
    print(" ")
    print(x,"^",y,"=",z)

elif  islem==("mod alma") or islem==("6") or islem==("Mod alma") or islem==("Mod") or  islem==("mod") or islem==("Mod Alma"):
    x=input("1. Sayıyı Giriniz: ")
    y=input("2. Sayıyı Giriniz: ")
    z=(int(x)%int(y))
    print(" ")
    print(x,"%",y,"=",z)

elif  islem==("karekök alma") or islem==("7") or islem==("Karekök alma") or islem==("karekök") or islem==("Karkök") or islem==("kare") or islem==("Kare"):
    x=input("Sayıyı Giriniz: ")
    z=sqrt(int(x))
    print(" ")
    print("√",x,"=",z)

else:
    print(" ")
    print("Lütfen Geçerli bir İşlem Giriniz")
    exit(0)
print(" ")
input("Çıkmak İçin Herhangi Bir Tuşa Basın: ")