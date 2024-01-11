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
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)
        print(f"Vücut kitle endeksiniz {vki} kg/m2, ideal kilonuz {int(ik)} kg'dır.")
        ikhmenu()
    elif secim=="2":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)
        print(f"Broca formülüne göre ideal kilonuz: {int(ik2)}")
        ikhmenu()
    elif secim=="3":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik3=boy*1.063-114
        print(f"Erkekler için Hamwi formülüne göre ideal kilonuz: {int(ik3)}")
        ikhmenu()
    elif secim=="4":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik4=boy*0.866-86.5
        print(f"Kadınlar için Hamwi formülüne göre ideal kilonuz: {int(ik4)}")
        ikhmenu()
    elif secim=="5":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik5=50+(2.3/2.54)*(boy-152.4)
        print(f"Erkekler için Divine formülüne göre ideal kilonuz: {int(ik5)}")
        ikhmenu()
    elif secim=="6":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik6=45.5+(2.3/2.54)*(boy-152.4)
        print(f"Kadınlar için Divine formülüne göre ideal kilonuz: {int(ik6)}")
        ikhmenu()
    elif secim=="7":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik7=boy*0.555-28.4
        print(f"Erkekler için Miller formülüne göre ideal kilonuz: {int(ik7)}")
        ikhmenu()
    elif secim=="8":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik8=boy*0.535-28.5
        print(f"Kadınlar için Miller formülüne göre ideal kilonuz: {int(ik8)}")
        ikhmenu()
    elif secim=="9":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik9=boy*0.748-62
        print(f"Erkekler için Robinson formülüne göre ideal kilonuz: {int(ik9)}")
        ikhmenu()
    elif secim=="10":
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        boy2=boy/100
        ik10=boy*0.67-53
        print(f"Kadınlar için Robinson formülüne göre ideal kilonuz: {int(ik10)}")
        ikhmenu()
    elif secim=="11":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))

        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)

        if kilo>ik:
            print("Vücut kitle endeksine göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Vücut kitle endeksine göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Vücut kitle endeksine göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)

        if kilo>ik2:
            print("Broca formülüne göre kilonuz", int(kilo - ik2), "kg fazla.")
        elif kilo<ik2:
            print("Broca formülüne göre kilonuz", int(ik2 - kilo), "kg az.")
        else:
            print("Broca formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik3=boy*1.063-114

        if kilo>ik3:
            print("Erkekler için Hamwi formülüne göre kilonuz", int(kilo - ik3), "kg fazla.")
        elif kilo<ik3:
            print("Erkekler için Hamwi formülüne göre kilonuz", int(ik3 - kilo), "kg az.")
        else:
            print("Erkekler için Hamwi formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik4=boy*0.866-86.5

        if kilo>ik4:
            print("Kadınlar için Hamwi formülüne göre kilonuz", int(kilo - ik4), "kg fazla.")
        elif kilo<ik4:
            print("Kadınlar için Hamwi formülüne göre kilonuz", int(ik4 - kilo), "kg az.")
        else:
            print("Kadınlar için Hamwi formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik5=50+(2.3/2.54)*(boy-152.4)

        if kilo>ik5:
            print("Erkekler için Divine formülüne göre kilonuz", int(kilo - ik5), "kg fazla.")
        elif kilo<ik5:
            print("Erkekler için Divine formülüne göre kilonuz", int(ik5 - kilo), "kg az.")
        else:
            print("Erkekler için Divine formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik6=45.5+(2.3/2.54)*(boy-152.4)

        if kilo>ik6:
            print("Kadınlar için Divine formülüne göre kilonuz", int(kilo - ik6), "kg fazla.")
        elif kilo<ik6:
            print("Kadınlar için Divine formülüne göre kilonuz", int(ik6 - kilo), "kg az.")
        else:
            print("Kadınlar için Divine formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik7=boy*0.555-28.4

        if kilo>ik7:
            print("Erkekler için Miller formülüne göre kilonuz", int(kilo - ik7), "kg fazla.")
        elif kilo<ik7:
            print("Erkekler için Miller formülüne göre kilonuz", int(ik7 - kilo), "kg az.")
        else:
            print("Erkekler için Miller formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik8=boy*0.535-28.5

        if kilo>ik8:
            print("Kadınlar için Miller formülüne göre kilonuz", int(kilo - ik8), "kg fazla.")
        elif kilo<ik8:
            print("Kadınlar için Miller formülüne göre kilonuz", int(ik8 - kilo), "kg az.")
        else:
            print("Kadınlar için Miller formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik9=boy*0.748-62

        if kilo>ik9:
            print("Erkekler için Robinson formülüne göre kilonuz", int(kilo - ik9), "kg fazla.")
        elif kilo<ik9:
            print("Erkekler için Robinson formülüne göre kilonuz", int(ik9 - kilo), "kg az.")
        else:
            print("Erkekler için Robinson formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik10=boy*0.67-53

        if kilo>ik10:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(kilo - ik10), "kg fazla.")
        elif kilo<ik10:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(ik10 - kilo), "kg az.")
        else:
            print("Kadınlar için Robinson formülüne göre kilonuz tam yerinde.")
            ikhmenu()
    elif secim=="12":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))

        boy2=boy/100
        vki=kilo/(boy2*boy2)
        ik=vki*(boy2*2)

        print(f"Vücut kitle endeksiniz {vki} kg/m2, ideal kilonuz {int(ik)} kg'dır.")

        if kilo>ik:
            print("Vücut kitle endeksine göre kilonuz", int(kilo - ik), "kg fazla.")
        elif kilo<ik:
            print("Vücut kitle endeksine göre kilonuz", int(ik - kilo), "kg az.")
        else:
            print("Vücut kitle endeksine göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik2=(boy-100)-((boy-150)/4)

        print(f"Broca formülüne göre ideal kilonuz: {int(ik2)}")

        if kilo>ik2:
            print("Broca formülüne göre kilonuz", int(kilo - ik2), "kg fazla.")
        elif kilo<ik2:
            print("Broca formülüne göre kilonuz", int(ik2 - kilo), "kg az.")
        else:
            print("Broca formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik3=boy*1.063-114

        print(f"Erkekler için Hamwi formülüne göre ideal kilonuz: {int(ik3)}")

        if kilo>ik3:
            print("Erkekler için Hamwi formülüne göre kilonuz", int(kilo - ik3), "kg fazla.")
        elif kilo<ik3:
            print("Erkekler için Hamwi formülüne göre kilonuz", int(ik3 - kilo), "kg az.")
        else:
            print("Erkekler için Hamwi formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik4=boy*0.866-86.5

        print(f"Kadınlar için Hamwi formülüne göre ideal kilonuz: {int(ik4)}")

        if kilo>ik4:
            print("Kadınlar için Hamwi formülüne göre kilonuz", int(kilo - ik4), "kg fazla.")
        elif kilo<ik4:
            print("Kadınlar için Hamwi formülüne göre kilonuz", int(ik4 - kilo), "kg az.")
        else:
            print("Kadınlar için Hamwi formülüne göre kilonuz tam yerinde.")
        
        boy2=boy/100
        ik5=50+(2.3/2.54)*(boy-152.4)

        print(f"Erkekler için Divine formülüne göre ideal kilonuz: {int(ik5)}")

        if kilo>ik5:
            print("Erkekler için Divine formülüne göre kilonuz", int(kilo - ik5), "kg fazla.")
        elif kilo<ik5:
            print("Erkekler için Divine formülüne göre kilonuz", int(ik5 - kilo), "kg az.")
        else:
            print("Erkekler için Divine formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik6=45.5+(2.3/2.54)*(boy-152.4)

        print(f"Kadınlar için Divine formülüne göre ideal kilonuz: {int(ik6)}")

        if kilo>ik6:
            print("Kadınlar için Divine formülüne göre kilonuz", int(kilo - ik6), "kg fazla.")
        elif kilo<ik6:
            print("Kadınlar için Divine formülüne göre kilonuz", int(ik6 - kilo), "kg az.")
        else:
            print("Kadınlar için Divine formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik7=boy*0.555-28.4

        print(f"Erkekler için Miller formülüne göre ideal kilonuz: {int(ik7)}")

        if kilo>ik7:
            print("Erkekler için Miller formülüne göre kilonuz", int(kilo - ik7), "kg fazla.")
        elif kilo<ik7:
            print("Erkekler için Miller formülüne göre kilonuz", int(ik7 - kilo), "kg az.")
        else:
            print("Erkekler için Miller formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik8=boy*0.535-28.5

        print(f"Kadınlar için Miller formülüne göre ideal kilonuz: {int(ik8)}")

        if kilo>ik8:
            print("Kadınlar için Miller formülüne göre kilonuz", int(kilo - ik8), "kg fazla.")
        elif kilo<ik8:
            print("Kadınlar için Miller formülüne göre kilonuz", int(ik8 - kilo), "kg az.")
        else:
            print("Kadınlar için Miller formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik9=boy*0.748-62

        print(f"Erkekler için Robinson formülüne göre ideal kilonuz: {int(ik9)}")

        if kilo>ik9:
            print("Erkekler için Robinson formülüne göre kilonuz", int(kilo - ik9), "kg fazla.")
        elif kilo<ik9:
            print("Erkekler için Robinson formülüne göre kilonuz", int(ik9 - kilo), "kg az.")
        else:
            print("Erkekler için Robinson formülüne göre kilonuz tam yerinde.")

        boy2=boy/100
        ik10=boy*0.67-53

        print(f"Kadınlar için Robinson formülüne göre ideal kilonuz: {int(ik10)}")

        if kilo>ik10:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(kilo - ik10), "kg fazla.")
        elif kilo<ik10:
            print("Kadınlar için Robinson formülüne göre kilonuz", int(ik10 - kilo), "kg az.")
        else:
            print("Kadınlar için Robinson formülüne göre kilonuz tam yerinde.")
        ikhmenu()
    elif secim=="13":
        print("Ana Menü'ye dönülüyor.")
        return
    elif secim=="14":
        print("Programdan çıkılıyor.")
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        ikhmenu()
