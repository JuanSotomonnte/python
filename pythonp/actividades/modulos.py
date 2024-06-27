def poblacion():
    keys=['Colombia','Bolivia']
    Values=[300,400]
    return keys,Values

def poblacionpais(datos,pais):
    resultado=list(filter(lambda item:item['country']==pais,datos))
    return resultado