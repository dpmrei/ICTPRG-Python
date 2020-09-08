
x = 1
y = 15

lista = []

for i in range (15):
    calc = round (x/y,2)
    lista.append(calc)
    
    x = x+1
    y = y-1
    
print (lista)
total = sum(lista)
print (total)
