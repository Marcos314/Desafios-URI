while True:
	try:
		entrada = int(input()) 
	except:
		break

	
	p = []  #array para guardar os elementos da flagPilha
	f = []	#array para guardar os elementos da fila
	fp = []	#array para guardar os elementos da fila de prioridade
	
	flagPilha=True
	flagFila=True
	flagFP=True

	aux = 0
	for i in range(entrada):
		operacao, n = input().split() #operação realizada pela estrut sacola e um numero int 
		if int(operacao) == 1: #se a opção escolhida foi 1 insere na estrutura sacola
			#inserções na pilha, fila e fila de prioridade
			p.append(int(n))
			aux+=1
			f.append(int(n))
			#print(f)
			fp.append(int(n))
			
			fp.sort(reverse=True) #caso for fila de prioridade ja ordena do maior pro menor, sendo o maior numero com mais prioridade
			#print(fp)			  #obs: lembrar q n imprime o 5 pq o mesmo foi retirado pela operação 2
		
		else:					  # operação 2
			
			if p[aux-1] == int(n) and flagPilha == True: #verificar se a pilha esta vazia pois aux tem q ser ao menos 1, ou seja, deve ter entrado ao menos uma vez no laço anterior
				aux-=1
				del p[aux]			#remove o elemento do topo da pilha
			else: flagPilha=False		
		
			'''na fila e fila de prioridade o primeiro elemento inserido é o primeiro que será retirado FIFO'''
			if f[0] == int(n) and flagFila == True:  #verifica se o primeiro elemento é igual ao elemento a ser retirado, pois a remoção de uma fila acontece a partir do primeiro elemento recebido
				del f[0]				
			else: flagFila=False		#caso o elemento a ser retirado ñ for igual ao primeiro elemento inserido então ñ é uma fila
		
			#mesmo caso da fila
			if fp[0] == int(n) and flagFP == True: 
				del fp[0]
			else: flagFP=False
	
	if (flagPilha == True and flagFila == True) or (flagPilha == True and flagFP == True) or (flagFila == True and flagFP == True): print("not sure") #nesse caso pode ser mais de uma das estruturas
	#se alguma das estruturas não for true ela será a estrutura a ser impressa
	elif flagPilha: print("stack")
	elif flagFila: print("queue")
	elif flagFP: print("priority queue")	
	else: print("impossible")	#se nenhum estrutura foi aceita ñ é possivel ser nenhuma das estruturas
'''
6
1 1
1 2
1 3
2 1
2 2
2 3
6
1 1
1 2
1 3
2 3
2 2
2 1
2
1 1
2 2
4
1 2
1 1
2 1
2 2
7
1 2
1 5
1 1
1 3
2 5
1 4
2 4
'''