try:
    print(0/0)
    assert 1!=1,'uno no es igual a uno'
    edad=10
    if edad >18:
        raise Exception('no es posible la entrada de menores de edad')
except ZeroDivisionError as error:
   print(error)
except AssertionError as error:
   print(error)
except Exception as error:
   print(error)

print('hola')