/*Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main() {


    float a,b,c,r1,r2,delta;
    
	scanf("%f %f %f", &a,&b, &c);
	
	delta = (b*b)-(4*a*c);
	r1 = (-b + (sqrt(delta)))/(2*a);
	r2 = (-b - (sqrt(delta)))/(2*a);

	if (a!=0 && delta>0){	
		
		printf("R1 = %.5f\n",r1 );
		printf("R2 = %.5f\n",r2 );
	}	

   	else printf("Impossivel calcular\n"); 

	
	return 0;
}

