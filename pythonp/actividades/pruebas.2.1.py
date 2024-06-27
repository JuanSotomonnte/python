'''
dict={}

for i in range(1,11):
    dict[i]=i*2

print(dict)

#forma2
dictv2={i:i*2 for i in range (1,11)}
print(dictv2)

import random

set_countries=['Colombia', 'Mexico','Bolivia','Peru']
polacion={}
for i in set_countries:
    polacion[i]=random.randint(1,100)

print(polacion)


poblacion={i: random.randint(1,100) for i in set_countries}
print(poblacion)


nombres=['nico','julieta','Juan']
edad=[12,23,41]
print(list(zip(nombres,edad)))


nuevo_dict={nombres:edad for (nombres, edad) in zip (nombres,edad)}

print(nuevo_dict)

import random

set_countries=['Colombia', 'Mexico','Bolivia','Peru']
poblacion={i: random.randint(1,100) for i in set_countries}
print(poblacion)

resultado={set_countries:poblacion for (set_countries,poblacion)in poblacion.items() if poblacion>5 }
print(resultado)



texto='Hola, desarrollo'
unico={c:c.count for c in texto if c in'aeiou'}
print(unico)

file = open ('.//text.txt')
print(file.read())

print(file.readline())
'''
with open ('.//text.txt','r+') as file:
  for line in file:
    print(line)
    file.write('holaaaaaaaaaaa\n')
