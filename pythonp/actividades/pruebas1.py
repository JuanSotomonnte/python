diccionario={}
print(type(diccionario))
diccionario={
    'nombre':"adasdasdasd",
    'avion':'aiosjdioasjdiasj',
    'last_name':'apellido',
    'edad':23
}
print(diccionario)

print(diccionario['edad'])
print(diccionario['last_name'])
print(diccionario.get('unvalor'))

print('avion' in diccionario)
print('propio' in diccionario)

diccionario['nombre']='Juan'
diccionario['avion']='Avianca'
diccionario['last_name']='Sotomonte'
print(diccionario)
