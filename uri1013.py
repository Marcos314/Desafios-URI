lista = input().split(' ')
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

MaiorAB = (a+b+abs(a-b))/2


print('{:.0f} eh o maior'.format(MaiorAB))