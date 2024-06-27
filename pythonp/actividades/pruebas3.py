'''
numeros= [1,2,3,4]
numeros2=[]
for i in numeros:
    numeros2.append(i *2)


numeros3=list(map(lambda i:i*2,numeros))
print(numeros)
print(numeros2)
print(numeros3)

numeros11= [1,2,3,4]
numeros22=[5,6,7]
print(numeros11)
print(numeros22)

resultado= list(map(lambda x,y:x+y,numeros11,numeros22))
print(resultado)
#aqui es otra actividad
items=[
    {
        'producto':'camisa',
        'precio':100,
      
    },
    {
        'producto':'pantalones',
        'precio':200
    },
    {
        'producto':'tenis',
        'precio':200
    }
]

precios=list(map(lambda item:item['precio'],items))
print(precios)

def impuestosadd(item):
    nuevoitem=item.copy()
    nuevoitem['impuestos']=  nuevoitem['precio']*.19
    return  nuevoitem

nueva_lista=list(map(impuestosadd, items))
print('nueva lista')
print(nueva_lista)
print('vieja lista')
print(items)

#filtro/filter
people = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]
print('lista normal')
print(people)
new_people=list(filter(lambda item:item['age']>20, people ))
print('lista actualizada/filter')
print(new_people)
print(len(new_people))


#reduce
import functools

number=[1,2,3,4,5]

def accum(counter,item):
    print('counter',counter)
    print('item',item)
    return counter + item
result=functools.reduce(accum,number)
result=functools.reduce(lambda counter,item:counter+item,number)
print(result)


#modulos 
import sys
print(sys.path)

import re
text='numero es 2345678921, el numero de pais es 57,otro numero es 3'

Result=re.findall('[0-9]+',text)

print(Result)

import time
#expresion hora compuesta
timestamp=time.time()
print(timestamp)

#expresion hora legible
local=time.localtime()
Result=time.asctime(local)
print(Result)


import collections

numbers=[1,2,2,3,4,2,5,1,8]
counter=collections.Counter(numbers)
print(counter)
'''
