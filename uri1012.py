'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. '''

lista = input().split(' ')
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])

areatriangulo = (a*c)/2
areacirculo = (3.14159)*(c**2)
areatrapezio = ((a+b)*c)/2
areaquadrado = b**2
arearetangulo = a*b
print('TRIANGULO: {:.3f}'.format(areatriangulo))
print('CIRCULO: {:.3f}'.format(areacirculo))
print('TRAPEZIO: {:.3f}'.format(areatrapezio))
print('QUADRADO: {:.3f}'.format(areaquadrado))
print('RETANGULO: {:.3f}'.format(arearetangulo))

