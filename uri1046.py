hi,hf = input().split(" ")

hi = int(hi)
hf = int(hf)

if hi<hf and hi>=1 and 0<=hf<=24:
	tot=hf-hi
	print("O JOGO DUROU {} HORA(S)".format(tot))
elif hi>hf and hi>=1 and 0<=hf<=24:
	tot=hf-hi+24	
	print("O JOGO DUROU {} HORA(S)".format(tot))
elif hi==hf and hi>=0 and 0<=hf<=24 :
	tot=24
	print("O JOGO DUROU {} HORA(S)".format(tot))
	