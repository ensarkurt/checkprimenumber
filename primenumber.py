
''' Burada Sayiyi aliyor '''
sayi = int(input("Bir Sayi Giriniz : "))


if(sayi>0):
    ''' Sayi 0 dan buyukse buraya giriyor '''

    ''' girilen sayiyi , 2 den baslayarak girilen sayi degerine kadar olan tum sayilara boluyor '''
    for i in range(2,sayi):
       if (sayi % i) == 0:
           print(str(sayi) + " Sayisi Bir Asal Sayi Degildir !")
           break
    else:
        print(str(sayi) + " Sayisi Bir Asal Sayidir !")

else:
    print(str(sayi) + " Sayisi 0 'dan Buyuk Degil !")

