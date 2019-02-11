"""
matbaa makinesi olack
dergi üretimi yapacak
mürekkebi ve sarjı var
mürekep ve şarj bitince kullanılamayacak
her 20 çalışmada bir dergi ortaya çıkacak
henüz yeni dergi çıkmadıysa yüzde kaçının tamamlandığını göstrecek
yeni dergi çıktığında ona isim verebilecek
her adımda kullanıcıya sorulacak sarj mı doldurmak istiyorsun mürekkep mi yoksa devam mı etmek istiyorsun
"""
import time
class makine():
    def __init__(self):
        self.devir=0
        self.murekkep=100
        self.sarj=100
        self.dergiler=[]

    def calıs(self):
        if(self.murekkep<=0):
            print("mürekkep yetersiz!!!")
            time.sleep(2)
        elif(self.sarj<=0):
            print("şarj yetersiz!!")
            time.sleep(2)
        else:
            self.devir += 1
            if(self.murekkep<3):
                self.murekkep=0
            else:
                self.murekkep -= 3

            if (self.sarj < 6):
                self.sarj = 0
            else:
                self.sarj -= 6

            print("makine çalışıyor lütfen bekleyin..")
            time.sleep(0.5)
        if(self.devir==20):
            self.devir=0
            self.yeniDergi()

    def yeniDergi(self):
         print("yeni dergi çıktı :)")
         a=input("derginin ismi ne olsun:")
         self.dergiler.append(a)
         time.sleep(2)

    def sarjdoldur(self):
        if(self.sarj<=100):
            self.sarj +=10
            print("şarj dolduruldu. mevcut şarj-->",self.sarj)
            time.sleep(2)

    def murekkepdoldur(self):
        if(self.murekkep<=100):
            self.murekkep += 10
            print("mürekkep dolduruldu. mevcut mürekkep-->",self.murekkep)
            time.sleep(2)

    def mevcutdurum(self):
        print("****makinenin mevcut durumu****")
        print("kalan mürekkep:",self.murekkep)
        print("kalan şarj:",self.sarj)
        print("toplam çıkarılan dergi sayisi:",len(self.dergiler))
        if(len(self.dergiler)>0):
            print("çıkarılan dergiler:")
            for i in self.dergiler:
                print(i)
        print("yeni çıkacak derginin %",self.devir*5,"kısmı tamamlandı")
        time.sleep(4)


makine1=makine()

print("matbaamıza hoşgeldiniz")
while True:
    print("-"*15)
    print("makineyi çalıştırmak için ->>1\n"
          "mevcut durumu öğrenmek için ->>2\n"
          "şarjı doldurmka için ->>3\n"
          "mürekkep doldurmak için ->>4\n"
          "çıkış yapmak için ->>5")
    komut=input()
    if(komut=="1"):
        makine1.calıs()
    elif(komut=="2"):
        makine1.mevcutdurum()
    elif(komut=="3"):
        makine1.sarjdoldur()
    elif(komut=="4"):
        makine1.murekkepdoldur()
    elif(komut=="5"):
        exit()
    else:
        print("geçerli bir işlem grinizi")



























