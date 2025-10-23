# hesap_makinesi.py
print("Basit Hesap Makinesi")
sayi1 = float(input("İlk sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")

if islem == "+":
    print(f"Sonuç: {sayi1 + sayi2}")
elif islem == "-":
    print(f"Sonuç: {sayi1 - sayi2}")
elif islem == "*":
    print(f"Sonuç: {sayi1 * sayi2}")
elif islem == "/":
    print(f"Sonuç: {sayi1 / sayi2}")
else:
    print("Geçersiz işlem!")
