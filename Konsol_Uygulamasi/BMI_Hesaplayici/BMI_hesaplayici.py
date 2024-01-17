import sys
import time

def bmimenu():
    print("╔════════════════════════════╗")
    print("║      BMI HESAPLAYICI       ║")
    print("║                            ║")
    print("║ 1- BMI Nedir?              ║")
    print("║ 2- BMI Ne İçin Hesaplanır? ║")
    print("║ 3- BMI Nasıl Hesaplanır    ║")
    print("║ 4- BMI Hesaplama           ║")
    print("║ 5- Ana Menü                ║")
    print("║ 6- Çıkış                   ║")
    print("║                            ║")
    print("╚════════════════════════════╝")
    print()
    secim=input("Lütfen seçiminizin başındaki sayıyı yazınız:")
    if secim=="1":
        print("VÜCUT KİTLE ENDEKSİ NEDİR?")
        print()
        print('''Vücut kitle endeksi (VKE), yetişkin bir bireyin kilosunun boyuna göre oranının ölçülmesi ile kişinin ideal kiloda olup olmadığını gösteren bir parametredir. İngilizcede "Body Mass Index (BMI)" şeklinde, Türkçe'de ise "Vücut Kitle Endeksi (VKE)" olarak ifade edilir. Kişilerin kolay ulaşabileceği ve cinsiyet, yaş, ırk ayrımı yapılmadan toplumdaki her bireye aynı şekilde uygulanabileceği için en yaygın olarak kullanılan boy-kilo parametresidir.''')
        print()
        print('''Matematiksel olarak kişinin kilosunun boyunun karesine bölünmesi ile vücut kitle endeksi bulunur. Bu ölçümle kişinin olması gereken kilo aralığı tayin edilebilir. Diyet planı uygulamak için yeterli bir ölçüm olmasa da vücut kitle endeksi, kişinin yaşına ve boyuna göre uygun bir kiloda olup olmadığına dair genel bir fikir verebilir.''')
        bmimenu()
    elif secim=="2":
        print("VÜCUT KİTLE ENDEKSİ NE İÇİN HESAPLANIR?")
        print()
        print('''Vücut kitle endeksi kişinin boyuna göre olması gereken kilo aralığını gösterdiği için bu değerin altında veya üstünde olması durumunda kişinin uygun kiloya gelmesi için yardımcı olmaktadır. Düşük VKE değerinde sağlıklı bir şekilde kilo alımı gerçekleştirilerek uygun kiloya erişilmelidir. Yüksek VKE değerinde ise spor ve diyetle sağlıklı kilo aralığına erişilmelidir.''')
        print()
        print('''Yine de kişinin sadece vücut kitle endeksine bakarak yeme düzeninde radikal değişiklikler yapması önerilmez. Kişinin sağlığı bir bütün olarak düşünülmelidir, bu sebeple tek bir parametreye göre hareket etmek doğru olmaz. Özellikle beslenme düzeni ve spor, kişiye özel ve uzman eşliğinde planlanmalıdır. Yağlanmayla yüksek vücut kitle endeksi değerleri paralellik göstereceğinden, kişinin beslenme düzeninde değişiklik yapmadan önce doktora ya da uzman diyetisyene başvurması tavsiye edilir.''')
        print()
        print('''Ayrıca vücut kitle endeksi kalp krizi, diyabet kanser gibi hastalıkların risk durumu hesaplaması için de kullanılmaktadır.''')
        bmimenu()
    elif secim=="3":
        print("BMI NASIL HESAPLANIR?")
        print()
        print('''Vücut kitle endeksi hesaplama, herkesin yapabileceği basit bir matematik işlemiyle mümkündür. Bunun için öncelikle kişinin boy ve ağırlık değerleri doğru bir şekilde ölçülmelidir. Ardından kişinin kilogram cinsinden kilosu, metre cinsinden boyun karesine bölünerek VKE hesaplanır. Formülü kilo/(metre)² olarak ifade edilebilir.''')
        print()
        print('''Örneğin 1.70 metre boyunda ve 80 kilogram ağırlığında bir bireyin vücut kitle endeksi hesaplanırken 80/(1.70×1.70) = 27,681 olarak hesaplanır.''')
        print()
        print('''1.50 metre boyunda ve 90 kilogram ağırlığında bir kişinin vücut kitle endeksi ise 90/(1.50)² = 40 bulunur.''')
        print()
        print('''Özellikle çocuk ve gençlik çağındaki bireylerde, ölçüm sonucunda çıkan değerler iki kişi arasında aynı olsa da bu iki kişi arasında tamamen farklı sağlık koşulları bulunabilir (obezite vb.). Bu sebeple bu yaşlarda yapılan VKE ölçümlerinin değerlendirilmesi uzman doktorlar tarafından yapılmalıdır.''')
        bmimenu()
    elif secim=="4":
        kilo=int(input("Lütfen kilonuzu giriniz (KG):"))
        boy=int(input("Lütfen boyunuzu giriniz (CM):"))
        vki=kilo/(boy2*boy2)
        boy2=boy/100
        print(f"Vücut kitle endeksiniz {vki} kg/m2'dir.")
        bmimenu()
    elif secim=="5":
        print("Ana Menü'ye dönülüyor.")
        return
    elif secim=="6":
        print("Program 3 saniye içinde kapatılacak.")
        time.sleep(3)
        sys.exit(0)
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")
        bmimenu()
