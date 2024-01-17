import sys
import time

def notmenu():
    ad=input("Adınız nedir?")
    vize=int(input("Lütfen vize notunuzu giriniz."))
    final=int(input("Lütfen final notunuzu giriniz."))
    proje=int(input("Lütfen proje notunuzu giriniz."))
    odev=int(input("Lütfen ödev notunuzu giriniz."))
    ortalama=(vize+final+proje+odev)/4
    print("╔═════════════════════╗")
    print("║   NOT HESAPLAYICI   ║")
    print("║                     ║")
    print("║ 1-Ortalama Hesaplama║")
    print("║ 2-Durum Bildirimi   ║")
    print("║ 3-Not Analizi       ║")
    print("║ 4-Ana Menü          ║")
    print("║ 5-Çıkış             ║")
    print("║                     ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        print(f"Merhaba {ad} ortalaman:",ortalama)
        notmenu()
    elif secim=="2":
        if ortalama<50:print(f"Üzgünüm {ad} kaldın.")
        else:print(f"Tebrikler {ad} geçtin.")
        notmenu()
    elif secim=="3":
        if vize>85:print(f"{ad} vizen çok güzel, finaldede aynı performansı sergile. AFERİN.")
        elif vize>70:print(f"{ad} vizen güzel geçmiş anlaşılan.")
        elif vize>50:print(f"{ad} vizeyi geçmişsin.")
        else:print(f"Üzgünüm {ad}, vizeyi geçemedin ama üzülme daha sıkı çalışırsan finalde geçebilirsin.")

        if final>85:print(f"{ad} finalin çok güzel geçmiş anlaşılan. AFERİN.")
        elif final>70:print(f"{ad} finalin güzel geçmiş anlaşılan.")
        elif final>50:print(f"{ad} finali geçmişsin.")
        else:print(f"Üzgünüm {ad}, finalde biraz çuvalladın.")

        if proje>85:print(f"{ad} projelerini çok güzel yapmışsın anlaşılan. AFERİN.")
        elif proje>70:print(f"{ad} projelerini güzel yapmışsın anlaşılan.")
        elif proje>50:print(f"{ad} projelerin tam öğretmenin istediği gibi değil anlaşılan ama geçirmiş öğretmenin.")
        else:print(f"{ad} projelerden kalmışsın bundan sonra daha dikkatli olmalısın.")

        if odev>85:print(f"{ad} ödevlerini çok güzel yapmışsın anlaşılan. AFERİN.")
        elif odev>70:print(f"{ad} ödevlerini güzel yapmışsın anlaşılan.")
        elif odev>50:print(f"{ad} ödevlerin tam öğretmenin istediği gibi değil anlaşılan ama geçmişsin.")
        else:print(f"{ad} ödevlerden kalmışsın daha sıkı çalışman lazım.")

        if ortalama>85:print(f"TEBRİKLER {ad}, sınıfı takdir alarak geçtin.")
        elif ortalama>70:print(f"TEBRİKLER {ad}, sınıfı teşekkür alarak geçtin.")
        elif ortalama>50:print(f"TEBRİKLER {ad}, sınıfı geçtin.")
        else:print(f"Üzgünüm {ad}, sınıfı geçemedin ama üzülme seneye daha sıkı çalışır geçersin geçemediklerini.")
        notmenu()
    elif secim=="4":
        print("Ana Menü'ye dönülüyor.")
        return
    elif secim=="5":
        print("Program 3 saniye içinde kapatılacak.")
        time.sleep(3)
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        notmenu()
