package uri;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.ArrayList;


public class OrdenacaoPorTamanho {
	public static void main (String []args) throws IOException {		
		BufferedReader ler = new BufferedReader(new InputStreamReader(System.in));
		String n; //nº de casos de teste
		
		while ((n = ler.readLine()) != null && n.length() > 0) {
			
			int n1 = Integer.parseInt(n); //passa o nº de casos de teste para inteiro
			
			String [] guardarF = new String[n1];//instancia um array de string com tamanho = n1
			for(int i=0; i < n1 ; i++) {
				
				guardarF[i]= ler.readLine();//recebe a string, guarda a string da forma q foi lida
			}
				for(int a =0; a<guardarF.length;a++) {
					String [] guardarP = guardarF[a].split(" "); //string para guardar cada palavra separadamente .split
					
					String auxiliar;
					int aux;
					int j;
					
					for(int i =1; i< guardarP.length;i++) {
						auxiliar=guardarP[i];
						//aux = Integer.parseInt(auxiliar);
						j=i-1;
						while((j>=0) && guardarP[j].length()<auxiliar.length()) {
							guardarP[j+1]=guardarP[j];
							j=j-1;
						}
						guardarP[j+1]=auxiliar;
					}					
				System.out.println(guardarP[i]);
					
				}
			}
		}
	}
/*
4
Top Coder comp Wedn at midnight
one three five
I love Cpp
sj a sa df r e w f d s a v c x z sd fd
*/