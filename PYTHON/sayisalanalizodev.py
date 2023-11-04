import math
x=0
hesaplanan=math.cos(x)-math.sin(x)*(math.pi/5-x)
print("1. TERİMİNİN KESME HATASI ")
print("HESAPLANAN DEĞER: ",hesaplanan)
gercek=math.cos(math.pi/5)
print("GERÇEK DEĞER: ",gercek)
kesme1=gercek-hesaplanan
print("KESME HATASI: ",kesme1)
print("********************************")
print("2. TERİMİNİN KESME HATASI ")
hesaplanan1=math.cos(x)-math.sin(x)*(math.pi/5-x)-(math.cos(x)*(math.pi/5-x)*(math.pi/5-x))/2
print("HESAPLANAN DEĞER: ",hesaplanan1)
gercek1=math.cos(math.pi/5)
print("GERÇEK DEĞER: ",gercek1)
kesme2=gercek1-hesaplanan1
print("KESME HATASI: ",kesme2)