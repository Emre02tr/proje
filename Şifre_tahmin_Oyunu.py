import random

tutulan_sayi = random.randint(1,1000)
deneme_sayisi = 0 
max_hak = 7

print("Sayı tahmin oyununa hoş geldiniz!")
print(f"{max_hak} hakkınız var. 1 ile 1000 arasında bir sayı tahmin edin.")

while deneme_sayisi < max_hak:
    try:
        tahmin = int(input("İle 10000 arasında bir sayı tahmin edin:"))
    except ValueError:
        print("Gecersiz giriş. Lütfen bir tam sayı giriniz.")
        continue 

    deneme_sayisi +=1
    kalan_hak = max_hak - deneme_sayisi

    if tahmin < tutulan_sayi:
        print("Daha yüksek bir sayı deneyin.")
    elif tahmin > tutulan_sayi:
        print("Daha düşük bir sayı deneyin.")
    else: 
        print(f"Tebrikler!{deneme_sayisi}denemede doğru tahmin ettiniz.")
        break
    print(f"Kalan hakkınız: {kalan_hak}")

    if deneme_sayisi == max_hak and tahmin != tutulan_sayi:
        print(f"Hakkınız bitti. Tutulan sayı {tutulan_sayi} idi.")

        

