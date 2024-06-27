def sumarang(min, max):
    print(min,max)
    sum=0
    for x in range(min,max):
        sum +=x
    return sum
resultado=sumarang(1,20)
print(resultado)
resultado2=sumarang(resultado,resultado*2)
print(resultado2)