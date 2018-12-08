
yes = []
no = []
entrada = input().split(" ")
while (entrada[0] != "FIM"):  # condição de parada EOF
   
    if(entrada[1] == "YES"): 
        if(entrada[0] not in (yes)): 
          yes.append(entrada[0]) #adiciona o nome(index 0) no array yes, caso ele ainda n esteja add
          #print("\n" + entrada[1] + "\n") #teste
    if(entrada[1] == "NO"):
        if(entrada[0] not in (no)):
          no.append(entrada[0])       
    entrada = input().split(" ")

i = 0
nome = ""

for j in range(len(yes)): #escolha do vencedor, verifica o tamanho da string
  if len(yes[j]) > i:
    nome = yes[j]       #atribui a maior string a variavel nome
    i = len(yes[j])

yes.sort()    #colocar em ordem alfabética
no.sort()

for i in range(len(yes)): #mostrar os nomes cujas escolhas foram yes e no respectivamente. 
  print(yes[i])
for i in range(len(no)):
  print(no[i])


print("\nAmigo do Habay:\n" + nome)


'''
index 0 - 1 (nome - opcao)
Joao NO
Carlos YES
Abner NO
Samuel YES
Ricardo NO
Abhay YES
Samuel YES
Andres YES
Roberto NO
Carlos YES
Samuel YES
Samuel YES
Abhay YES
Aline YES
Andres YES
FIM
'''