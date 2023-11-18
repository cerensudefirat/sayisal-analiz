import math
x_baslangic=2

for i in range(0,4):
    f=4*(math.e**(-0.5*x_baslangic))-x_baslangic
    f_turev=-2*(math.e**(-0.5*x_baslangic))-1
    x_baslangic=x_baslangic-(f/f_turev)
    print(i+1,".iterasyon sonucu= ",x_baslangic)