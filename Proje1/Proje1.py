import Hesap_Makinesi.Hesap_makinesi

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
    print("║ 11- Çıkış(E)         ║")
    print("║                      ║")
    print("╚══════════════════════╝")
    print()
    print("Seçiminizin başındaki karakteri yazınız:")
    secim=input()
    if secim=="1":
        Hesap_Makinesi.Hesap_makinesi.hmmenu()
        anamenu()
    if secim=="2":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="3":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="4":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="5":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="6":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="7":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="8":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="9":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="10":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    if secim=="11":
        print("Çok yakında kullanıma sunulacak.")
        anamenu()
    else:
        anamenu()

anamenu()
