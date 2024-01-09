import sys

def ikhmenu():
    kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
    boy=int(input("Lütfen boyunuzu giriniz (CM):"))
    boy2=boy/100
    print("╔════════════════════════════════╗")
    print("║     İDEAL KİLO HESAPLAYICI     ║")
    print("║                                ║")
    print("║ 1- Vücut Kitle İndeksi'ne      ║")
    print("║    Göre İdeal Kilo Hesaplama   ║")
    print("║ 2- Broca Formülü İle           ║")
    print("║    İdeal Kilo Hesaplama        ║")
    print("║ 3- Erkekler İçin               ║")
    print("║    Hamwi Formülü İle           ║")
    print("║    İdeal Kilo Hesaplama        ║")
    print("║ 4- Kadınlar İçin               ║")
    print("║    Hamwi Formülü İle           ║")
    print("║    İdeal Kilo Hesaplama        ║")
    print("║ 5- Kilo Durumu Değerlendirme   ║")
    print("║ 6- İdeal Kilo Hesaplayarak     ║")
    print("║    Kilo Durumu Değerlendirmesi ║")
    print("║ 7- Ana Menü                    ║")
    print("║ 8- Çıkış                       ║")
    print("║                                ║")
    print("╚════════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        vki= kilo/(boy2*boy2)
        ik= vki*(boy2*2)
        print(f"Vücud kitle endeksiniz {vki} kg/m2, ideal kilonuz {ik} kg'dır.")
        ikhmenu()
    elif secim=="2":
        ik=(boy-100)-((boy-150)/4)
        print(ik)
        ikhmenu()
    elif secim=="3":
        ik=48+2.7*(boy-60)
        print(ik)

ikhmenu()
