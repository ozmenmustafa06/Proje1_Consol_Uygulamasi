import Hesap_Makinesi.Hesap_makinesi
import Not_Hesaplama.Not_hesaplama
import sys

def anamenu():
    print("╔══════════════════════╗")
    print("║     PYTHON PROJE     ║")
    print("║                      ║")
    print("║ 1- Hesap Makinesi    ║")
    print("║ 2- Oyunlar           ║")
    print("║ 3- Şekil Çizdirme    ║")
    print("║ 4- Takvim            ║")
    print("║ 5- Ritmik Sayma      ║")
    print("║ 6- Not Hesaplama     ║")
    print("║ 7- Çarpım Tablosu    ║")
    print("║ 8- BMI Hesaplama     ║")
    print("║ 9- Döviz Uygulaması  ║")
    print("║ 10- Sıcaklık Çevirme ║")
    print("║ 11- Çıkış            ║")
    print("║                      ║")
    print("╚══════════════════════╝")
    print()
    print("Lütfen seçiminizin başındaki sayıyı yazınız:")
    secim=input()
    if secim=="1":
        Hesap_Makinesi.Hesap_makinesi.hmmenu()
        anamenu()
    elif secim=="2":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="3":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="4":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="5":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="6":
        Not_Hesaplama.Not_hesaplama.notmenu()
        anamenu()
    elif secim=="7":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="8":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="9":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="10":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    elif secim=="11":
        print("Programdan çıkılıyor.")
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        anamenu()

anamenu()
