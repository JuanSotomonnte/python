lista=[23,213,12,34,5,41,4]
for i in lista:
    print(i)
tupla=('juan','koala','arroz')
for i in tupla:
    print(i)

diccionario={
    'name':'Juan',
    'Precio':100,
    'stock':20
}
for i in diccionario:
    print('parte uno')
    print(i,'=>',diccionario[i])

    for i , value in diccionario.items():
        print('parte dos')
        print(i,'=>',value)

diccionarios=[
    {
     'name':'Juan',
     'edad':34
    },
    {
    'name':'koala',
    'edad':31
    },
    {
    'name':'lucas',
    'edad':12
    }
]

for i in diccionarios:
        print('name =>',i['name'])
   
