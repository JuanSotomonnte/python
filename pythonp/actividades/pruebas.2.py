'''
set_countries={'colombia', 'mexico','bolivia'}
print(set_countries)

set_numeros={1,2,3,4,5,88}
print(set_numeros)
 
set_string=set('hola')
print(set_string)

set_tuplas=set(('abc', 'djv','poc'))
print(set_tuplas)

set_array=set([1,2,3,45,6,3,2])
print(set_array)
'''

set_countries={'Colombia', 'Mexico','Bolivia'}
set_countries2={'Bolivia','Peru'}

#union
#forma 1
print('=== UNION ===')
set_c=set_countries.union(set_countries2)
print(set_c)

# forma 2
print(set_countries| set_countries2)

#interseccion
print('=== INTERSECCION ===')
#forma 1
set_c=set_countries.intersection(set_countries2)
print(set_c)

#forma 2
print(set_countries&set_countries2)

#diferencias
print('=== DIFERENCIAS ===')
#forma 1
set_c=set_countries.difference(set_countries2)
print(set_c)

#forma2
print(set_countries-set_countries2)


#diferencia simetrica
#forma1
print('=== DIFERENCIAS SIMETRICAS ===')

set_c=set_countries.symmetric_difference(set_countries2)
print(set_c)

#forma2
print(set_countries^set_countries2)