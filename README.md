
islemler =[]
bakiye = 1000

def dosyaya_yaz(metin):
    with open("islem_gecmisi.txt","a",encoding="utf-8") as dosya:
        dosya.write(metin + "\n")


def para_yatir(bakiye):
    try:
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz:"))
        if miktar <= 0:
            print("Lütfen pozitif bir miktar giriniz.")
            return bakiye
        bakiye += miktar
        print(f"{miktar} TL yatırıldı. Güncel bakiyeniz: {bakiye} TL")

        islemler.append(f"{miktar} TL yatırıldı. Güncel bakiyeniz: {bakiye} TL")
        dosyaya_yaz(f"{miktar} TL yatırıldı.")

        return bakiye
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")
    return bakiye

def para_cek(bakiye):
    try:
        miktar = float(input("Çekmek istediğiniz miktarı giriniz:"))
        if miktar <=0:
            print("Lütfen pozitif bir miktar giriniz.")
            return bakiye
        
        if miktar > bakiye:
            print("Yetersiz bakiye.")
            return bakiye
        
        bakiye -= miktar

        print(f"{miktar}tl çekildi. Güncel bakiyeniz: {bakiye}TL")

        islemler.append(f"{miktar} TL çekildi. Güncel bakiyeniz: {bakiye} TL")
        dosyaya_yaz(f"{miktar}TL çekildi.")
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer giriniz.")
        return bakiye
def bakiye_goster(bakiye):
        print(f"Güncel bakiyeniz:{bakiye}TL")
        return bakiye
def islem_gecmisi_goster():
    if not islemler:
        print("Henüz yapılmış bir işlem yok.")
    else:
        print("İşlem Geçmişi:")
        for islem in islemler:
            print(islem)
def dosyadan_oku():
    try:
        with open("islem_gecmisi.txt","r",encoding="utf-8") as dosya:
            print("Dosyadaki İşlem geçmişi:")
            print(dosya.read())
    except FileNotFoundError:
        print("Henüz işlem geçmiş dosyası bulunamadı.")


while True:
    print("\n -----Banka Menüsü -----")
    print("1 - Para yatırma")
    print("2 - Para çekme")
    print("3 - Bakiye sorgulama")
    print("4 - Çıkış")
    print("5 - İşlem geçmişi gösterme")
    print("6 - Dosyadan işlem geçmişi oku")

    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1/2/3/4/5/6)")

    if secim == "1":
        bakiye = para_yatir(bakiye)

    elif secim == "2":
        bakiye = para_cek(bakiye)

    elif secim == "3":
        bakiye = bakiye_goster(bakiye)
    
    elif secim == "5":
        islem_gecmisi_goster()

    elif secim == "6":
        dosyadan_oku()

    elif secim == "4":
        print("İyi günler.")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")




