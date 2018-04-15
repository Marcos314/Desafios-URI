'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.'''
n = float(input())
if 0 <= n <= 1000000.00:
    print("NOTAS:") 
    a = n//100
    print('{:.0f} nota(s) de R$ 100.00'.format(a))
    a1 = n % 100
    b = a1//50
    print('{:.0f} nota(s) de R$ 50.00'.format(b))
    a2 = a1 % 50
    c = a2//20
    print('{:.0f} nota(s) de R$ 20.00'.format(c))
    a3 = a2 % 20
    d = a3 //10
    print('{:.0f} nota(s) de R$ 10.00'.format(d))
    a4 = a3 % 10
    e = a4 //5
    print('{:.0f} nota(s) de R$ 5.00'.format(e))
    a5 = a4 % 5
    f = a5 // 2
    print('{:.0f} nota(s) de R$ 2.00'.format(f))
    print('MOEDAS:')   
    a6 = a5 % 2
    g = a6 // 1
    print('{:.0f} moeda(s) de R$ 1.00'.format(g))
    a7 = a6 % 1
    h = a7 // 0.5
    print('{:.0f} moeda(s) de R$ 0.50'.format(h))
    a8 = a7 % 0.5
    i = a8 // 0.25
    print('{:.0f} moeda(s) de R$ 0.25'.format(i))
    a9 = a8 % 0.25
    j = a9 // 0.10
    print('{:.0f} moeda(s) de R$ 0.10'.format(j))
    a10 = a9 % 0.10
    k = a10 // 0.05
    print('{:.0f} moeda(s) de R$ 0.05'.format(k))
    a11 = a10 % 0.05
    l = a11 / 0.01
    print('{:.0f} moeda(s) de R$ 0.01'.format(l))





