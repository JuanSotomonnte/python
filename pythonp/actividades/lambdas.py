def increment(z):
    return z+1
incrementv2=lambda z:z+1

respuesta=increment(10)
print(11)

respuesta=incrementv2(20)
print(respuesta)

nombre_completo=lambda name,last_name:f'el nombre completo es {name.title()} {last_name.title()}'

text=nombre_completo('Juan','Sotomonte Cortes')
print(text)