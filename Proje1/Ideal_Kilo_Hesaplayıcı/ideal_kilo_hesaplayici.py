import sys

def ikhmenu():
    print("╔═════════════════════════════════╗")
    print("║     İDEAL KİLO HESAPLAYICI      ║")
    print("║                                 ║")
    print("║  1- Vücut Kitle İndeksi'ne      ║")
    print("║     Göre İdeal Kilo Hesaplama   ║")
    print("║  2- Broca Formülü İle           ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  3- Erkekler İçin               ║")
    print("║     Hamwi Formülü İle           ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  4- Kadınlar İçin               ║")
    print("║     Hamwi Formülü İle           ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  5- Erkekler İçin               ║")
    print("║     Divine Formülü İle          ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  6- Kadınlar İçin               ║")
    print("║     Divine Formülü İle          ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  7- Erkekler İçin               ║")
    print("║     Miller Formülü İle          ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  8- Kadınlar İçin               ║")
    print("║     Miller Formülü İle          ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║  9- Erkekler İçin               ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 10- Kadınlar İçin               ║")
    print("║     Robinson Formülü İle        ║")
    print("║     İdeal Kilo Hesaplama        ║")
    print("║ 11- Kilo Durumu Değerlendirme   ║")
    print("║ 12- İdeal Kilo Hesaplayarak     ║")
    print("║     Kilo Durumu Değerlendirmesi ║")
    print("║ 13- Ana Menü                    ║")
    print("║ 14- Çıkış                       ║")
    print("║                                 ║")
    print("╚═════════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)
        print(f"Vücud kitle endeksiniz {vki} kg/m2, ideal kilonuz {ik} kg'dır.")
        ikhmenu()
    elif secim=="2":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=(boy-100)-((boy-150)/4)
        print(f"Broca formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="3":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*1.063-114
        print(f"Hamwi formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="4":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*0.866-86.5
        print(f"Hamwi formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="5":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=50+(2.3/2.54)*(boy-152.4)
        print(f"Divine formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="6":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=45.5+(2.3/2.54)*(boy-152.4)
        print(f"Divine formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="7":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*0.555-28.4
        print(f"Miller formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="8":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*0.535-28.5
        print(f"Miller formülüne göre ideal kilonuz: {ik}")
        ikhmenu()
    elif secim=="9":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*0.748-62
        print(ik)
    elif secim=="10":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik=boy*0.67-53
        print(ik)
    elif secim=="11":
        boy=12
        print(boy)



ikhmenu()
