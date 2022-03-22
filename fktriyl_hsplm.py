x=1
a=int(input("Faktöriyeli Alınması İçin Sayı Giriniz= "))
if a<0:
    cevap=input("Girilen Sayı Negatif Bir Sayı Pozitife Çevirmek İçin e Basınız= ")
    if cevap=="e":
        a=a*-1
        for i in range(1,a+1):
            x=x*i
        print(x)
    else:
        print("Sayınız Negatif Olduğu İçin Hesaplayamam Üzgünüm :( ")
else:
    for i in range(1,a+1):
        x=x*i
    print(x)
