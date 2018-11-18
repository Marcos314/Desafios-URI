

n = int(input()) #número de codigos a serem inseridos
#n = 0
entrada = 0
list = []


#while(n != ''):	
#	n = int(input())	
for i in range(n):
    cod = input()
    list.append(cod) #inserir o codigo digitado dentro da lista

    if len(list) == n:
        list.sort()
        aux = "\n".join(list)

        print(aux)
	        

	      


'''
3
1233
0015
0100
7
0752
1110
0001
6322
8000
6321
0000
'''