"""x3+4x2-10=0 [1,2]"""
x_alt=1
x_ust=2
for i in range(0,4):
    f_alt=x_alt*x_alt*x_alt+4*x_alt*x_alt-10
    f_ust=x_ust*x_ust*x_ust+4*x_ust*x_ust-10
    print(x_alt,"=",f_alt,"\t",x_ust,"=",f_ust)
    x_kok=(x_alt+x_ust)/2
    f_kok=x_kok*x_kok*x_kok+4*x_kok*x_kok-10
    if f_alt*f_kok<0:
        x_ust=x_kok
    elif f_ust*f_kok<0:
        x_alt=x_kok
print("4. iterasyon sonucu kök ve değeri: ",x_kok,"=",f_kok)