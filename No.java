package uri;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No {
	int valor;
	No noEsquerda;
	No noDireita;	
	public No (int valor) {
		this.valor = valor;
	}
	public static Noo raiz ;
	
	public static void inserir ( int valor) {      // primeira inserção No raiz
		inserir (raiz, valor);
	}

	public static void inserir(Noo node, int valor) {
		if (node==null) {								//verifica se arvore esta vazia
			raiz= new Noo (valor);					   // vai inserir na raiz o valor 

		}else {
			if (valor < node.valor) {				//  verifica se o valor é menor do que o que está na raiz
				if(node.noEsquerda !=null) {		//insere a esquerda da rais
					inserir (node.noEsquerda, valor);
				}else {
					
					node.noEsquerda = new Noo(valor);
				}
			}else 							// valor maior que o valor que está na raiz
				if (node.noDireita!=null) {	//inserção a direita da raiz
					inserir(node.noDireita, valor);
				}else{
					
					node.noDireita=new Noo (valor);
				}
		}
	}
		
	public static void preordem (Noo node) {						// raiz - esquerda - direita
		if (node != null) {
			System.out.print(" "+node.valor);
			preordem (node.noEsquerda);
			preordem (node.noDireita);
		}
	}
	public static void posordem (Noo node) {				// esquerda - raiz - direita
		if (node !=null) {
			posordem(node.noEsquerda);
			posordem (node.noDireita);
			System.out.print(" "+node.valor);
		}
	}	
	public static void inordem (Noo node) {       // esquerda - direita - raiz
		if (node !=null) {
			inordem(node.noEsquerda);
			System.out.print(" "+node.valor);
			inordem(node.noDireita); 
		}
	}
	public static void main (String []ags) throws IOException {
		
		BufferedReader ler = new BufferedReader(new InputStreamReader(System.in));		
		String x,qntdCasos,qntdNumeros,numeros; 
		
		while ((x = ler.readLine()) != null && x.length() > 0) {
			
			int qntdEntrada = Integer.parseInt(x);
			for(int j = 1;j<qntdEntrada+1;j++) {
				
				qntdNumeros = ler.readLine();    //ler a qntd de numeros a serem inseridos na arvore
				int qntdNum = Integer.parseInt(qntdNumeros); //passa a linha lida como string para inteiro
				numeros = ler.readLine();
				String []num = numeros.split(" "); //ler os números a serem inseridos na árvore 
				No tree = new No(qntdNum);				
				
				for(int i=0;i<qntdNum; i++) {					
					int numero = Integer.parseInt(num[i]);
					tree.inserir(numero);
				}
				System.out.println("Case " + j + ":");
				System.out.print("Pre.:");
				tree.preordem(raiz);
				System.out.println();
				System.out.print("In..:");
				tree.inordem(raiz);
				System.out.println();
				System.out.print("Post:");
				tree.posordem(raiz);
				System.out.println();
			}
		}
		/*System.out.println("POS-ORDEM");
		posordem(raiz);
		System.out.println("PRE-ORDEM");
		preordem(raiz);
		System.out.println("IN-ORDEM");
		inordem(raiz);*/
	}
}

/*
2
3
5 2 7
9
8 3 10 14 6 4 13 7 1
 
 */
