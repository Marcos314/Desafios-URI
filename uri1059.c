/*Números pares
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha
*/
# include <stdio.h>

int main(){

	int cont;

		for (cont = 2; cont <= 100; cont+=2)
		{
		printf("%i\n",cont );
		} 

	return 0;
}
