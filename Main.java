package uri;

 import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        Stack entradaA= new Stack(); 		 //pilha para guardar quem está em A
        
        int qntdVag = ler.nextInt(); 			//quantidade de vagões
        //arrays com o tamanho relativo a qntd de  vagões
        int[] saida = new int[qntdVag];		
        int[] entrada = new int[qntdVag];
        int posAux = 0;
         
        while (qntdVag != 0) {		
        	 
            for (int i = 0; i < qntdVag; i++) {
                saida[i] = ler.nextInt();       	// saida em A Ex:  [5,4,3,2,1]
                if (saida[0] == 0) {				//numero de vagão > 0
                    break;
                }
                entrada[i] = i + 1;    //Ex: entrada em A  [1,2,3,4,5]
            }
            while (saida[0] != 0) {
                for (int i = 0; i < qntdVag; i++) {
                    entradaA.push(entrada[i]);   //a pilha recebe os valores armazenados na entrada em A, a remoção dessa pilha é a entrada em B
                   
                    /*se a pilha não estiver vazia e o elemento do topo (.peek) for igual o elemento na posAux no array saida entra no while. 
                     *Esse laço abaixo vai remover todos os elementos da pilha caso o elemento do topo da pilha for igual ao primeiro elemento inserido
                     *no vetor saida.
                     * */
                    while (!entradaA.isEmpty() && (Integer)entradaA.peek() == saida[posAux]) { 
                        entradaA.pop(); //remove do top
                        posAux += 1;	
                    }
                }
                //if para verificar se a pilha esta vazia ou não
                if (entradaA.isEmpty()) {
                    System.out.println("Yes");
                } else {
                    System.out.println("No");
                }
                
                /*laço para a proxima entrada com os vagões permutados*/
                 for (int i = 0; i < qntdVag; i++) {
                    saida[i] = ler.nextInt();		
                    //System.out.println(saida[i]);
                    if (saida[0] == 0) {                   	
                    	break;
                        
                    }
                    entrada[i] = i + 1;
                }
                 
                posAux = 0;			
                entradaA.clear(); // remove todos os elementos da pilha
            }
            // Reinicio, entrada de outro trem
            System.out.println();
            entradaA.clear();
            qntdVag = ler.nextInt();
            saida = new int[qntdVag];
            entrada = new int[qntdVag];
            posAux = 0;
        }
    }
}
/*
5
5 4 3 2 1
1 2 3 4 5
5 4 1 2 3
0
6
1 3 2 5 4 6
0
0
*/
