numeros = [1,2,3,4,5,6,7,8,9,10]

#numeros=[7,5,8,10,15,1,4]

pares = list(filter(lambda x:x % 2==0,numeros))

print(pares) #output [2,4,6,8,10]

mayoracinco = list(filter(lambda x : x>5, numeros ))
mayoracinco.sort
print(mayoracinco) #output [2,4,6,8,10] #output []



