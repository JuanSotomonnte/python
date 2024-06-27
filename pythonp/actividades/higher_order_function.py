def increment(x):
    return x+1
incrementv2=lambda x:x+1

def hof(x,function):
    return x+ function(x)

hof2=lambda x, function:x+function(x)

result=hof(2,increment)
print(result)

result=hof2(2,incrementv2)
print(result)