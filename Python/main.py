print("kodlamaio")
baslik = "taşıt kredisi"
print(baslik)
#string => metinsel ifade
baslik = "ihtiyaç kredisi"
print(baslik)
#int, integer => tam sayı
vade = 36 # int, integer
ekVade = 6
vade2 = "36" # string

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => true veya false
yukselisteMi = False

# matematiksel operatörler
# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and

# or => veya
# and => ve
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2) 
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapıları
# if else
sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
# condition

#indent
if sayi1 <= sayi2:
    print("sayi 1 sayi 2'den küçüktür")
#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("iki sayı eşittir")
#eğer if ve else if bloklarından hiçbirine girmez ise
else:
    print("sayi 1 sayi 2'den büyüktür")


print("***************************")

#indent
if sayi1 <= sayi2:
    print("sayi 1 sayi 2'den küçüktür")
#eğer if bloğuna girmez ise
if sayi1 == sayi2:
    print("iki sayı eşittir")
#eğer if ve else if bloklarından hiçbirine girmez ise
else:
    print("sayi 1 sayi 2'den büyüktür")


print("burası if bloğunun dışıdır.")



