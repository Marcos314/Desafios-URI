from math import sqrt
lista = input().split(' ')
x1 = float(lista[0])
y1 = float(lista[1])
lista2 = input().split(' ')
x2 =float(lista2[0])
y2 = float(lista2[1])
distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
print('{:.4f}'.format(distancia))