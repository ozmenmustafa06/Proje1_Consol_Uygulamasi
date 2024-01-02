def hmmenu():
    print("╔════════════════╗")
    print("║ HESAP MAKİNESİ ║")
    print("║                ║")
    print("║ 1-Toplama (+)  ║")
    print("║ 2-Çıkarma (-)  ║")
    print("║ 3-Çarpma  (*)  ║")
    print("║ 4-Bölme   (/)  ║")
    print("║                ║")
    print("╚════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki karakteri yazınız:")
    sayi1=int(input("Lütfen 1. sayıyı giriniz."))
    sayi2=int(input("Lütfen 2. sayıyı giriniz."))
    if secim=="1":
        print(sayi1+sayi2)
        hmmenu()
    if secim=="2":
        print(sayi1-sayi2)
        hmmenu()
    if secim=="3":
        print(sayi1*sayi2)
        hmmenu()
    if secim=="4":
        print(sayi1/sayi2)
        hmmenu()
