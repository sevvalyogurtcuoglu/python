# 1->toplama 2-<çıkarma 3->çarpma 4->faktöreiyel

# 1 ile 4 araında random sayı üretilecek

import random
import time
import math
skor=0
while True:
    islem=random.randint(1,4)
    print(islem)
    time.sleep(2)
    if islem==1:
        print("toplama")
        ilksayi=random.randint(1,20)
        ikincisayi=random.randint(1,20)
        print(ilksayi, "ile", ikincisayi,"toplamlarını giriniz" )
        sonuc=int(input("cevap:"))

        if(sonuc==ilksayi+ikincisayi):
            print("tebriks")
            skor=skor+1
            print("skornuz:", skor)
            time.sleep(2)
        else:
            print("yanlışşş doğrusu:",ilksayi+ikincisayi)
            skor=skor-3
            print("skornuz:", skor)
            time.sleep(2)
    elif islem==2:
        print("çıkarma")
        ilksayi=random.randint(1,20)
        ikincisayi=random.randint(1,20)
        print("sayılarınız:",ilksayi, "-", ikincisayi)
        sonuc=int(input("cevap:"))
        if (sonuc == ilksayi - ikincisayi):
            print("tebriks")
            skor = skor + 1
            print("skornuz:", skor)
            time.sleep(2)
        else:
            print("yanlışşş doğrusu:", ilksayi - ikincisayi)
            skor = skor - 3
            print("skornuz:", skor)
            time.sleep(2)

    elif islem==3:
        print("çarpma")
        ilksayi = random.randint(1, 5)
        ikincisayi = random.randint(1, 5)
        print("sayılarınız:", ilksayi, "*", ikincisayi)
        sonuc = int(input("cevap:"))
        if (sonuc == ilksayi * ikincisayi):
            print("tebriks")
            skor = skor + 1
            print("skornuz:", skor)
            time.sleep(2)
        else:
            print("yanlışşş doğrusu:", ilksayi * ikincisayi)
            skor = skor - 3
            print("skornuz:", skor)
            time.sleep(2)
    else:
        print("faktöriyel")
        ilksayi=random.randint(1,5)
        print(ilksayi,"faktöriyelini hesplauınız")
        sonuc=int(input("cevap:"))
        if(sonuc==math.factorial(ilksayi)):
            print("tebriks")
            skor = skor + 1
            print("skornuz:", skor)
            time.sleep(2)
        else:
            print("yanlişşşşşşşşş doğrusu:",math.factorial(ilksayi))
            skor = skor - 3
            print("skornuz:",skor)
    if(skor<=0):
       print("hakkınız bitti")
       exit()