#1.soru
ad = input("Adınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))
boy = float(input("Boyunuzu giriniz : "))

print(f"Merhaba {ad}, {yas} yaşındasınız ve boyunuz {boy} metredir.")

#2.soru
matematik = int(input("Matematik notunu giriniz: "))
fizik = int(input("Fizik notunu giriniz: "))
kimya = int(input("Kimya notunu giriniz: "))

ortalama = (matematik + fizik + kimya) / 3
print(f"Not ortalamanız: {ortalama}")

#3.soru
metin = "Veri Bilimi"

print("İlk karakter:", metin[0])
print("Son karakter:", metin[-1])
print("Uzunluk:", len(metin))
print("Ters çevrilmiş:", metin[::-1])

#4.soru
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)
print("Bölüm:", sayi1 / sayi2)
print("Mod:", sayi1 % sayi2)

#5.soru
ortalama = float(input("Ortalamanızı giriniz: "))

if ortalama > 50:
    print("Geçti")
else:
    print("Kaldı")