import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {

   
    public static void main(String[] args) throws IOException {
        BufferedReader ler = new BufferedReader (new InputStreamReader(System.in));
        String entrada;
        while((entrada=ler.readLine())!= null && entrada.length()>0) {
            int numero = Integer.parseInt(entrada);
            int vetor[] = new int [numero];
            for(int i = 0; i < numero; i++){
                vetor[i] = Integer.parseInt(ler.readLine()) ;
            }
            for(int i=0; i<numero;i++){
                for(int j=0; j<numero-1;j++){
                    if(vetor[j] > vetor [j+1]) {
                        int auxiliar = vetor [j];
                        vetor[j] = vetor[j+1];
                        vetor[j+1]= auxiliar;
                    }
                }
            }
            for(int i=0; i<numero; i++){
                System.out.println(vetor[i]);
            }
        }      
    }
}
/*
7
0752
1110
0001
6322
8000
6321
0000
*/