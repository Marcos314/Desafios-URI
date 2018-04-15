#s = salario
#ns = novo salario
#r = reajuste


s=float(input())
	
if s <= 400:
	ns = (15/100)*s+s 
	r = (15/100)*s
	print("Novo salario: {:.2f}".format(ns))
	print("Reajuste ganho: {:.2f}".format(r))
	print("Em percentual: 15 %") 	


if s >= 400.01 and s<=800:
	ns = (12/100)*s+s 
	r = (12/100)*s
	print("Novo salario: {:.2f}".format(ns))
	print("Reajuste ganho: {:.2f}".format(r))
	print("Em percentual: 12 %") 	

if s >= 800.01 and s<=1200:
	ns = (10/100)*s+s 
	r = (10/100)*s
	print("Novo salario: {:.2f}".format(ns))
	print("Reajuste ganho: {:.2f}".format(r))
	print("Em percentual: 10 %") 	

if s >= 1200.01 and s<=2000:
	ns = (7/100)*s+s 
	r = (7/100)*s
	print("Novo salario: {:.2f}".format(ns))
	print("Reajuste ganho: {:.2f}".format(r))
	print("Em percentual: 7 %") 	

if s > 2000:
	ns = (4/100)*s+s 
	r = (4/100)*s
	print("Novo salario: {:.2f}".format(ns))
	print("Reajuste ganho: {:.2f}".format(r))
	print("Em percentual: 4 %") 	
