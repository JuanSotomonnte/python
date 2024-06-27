import modulos
datos= [
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

def run():
    keys,values=modulos.poblacion()
    print(keys,values)
country=input('Escribe tu Pais : ')
result=modulos.poblacionpais(datos,country)
print(result)
print(len(result))

if __name__=='__main__':
    run()