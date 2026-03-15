import java.io.IOException;
import java.util.Scanner;

public class BEE1018 {
    
    public static void main(String[] args) throws IOException {
 
        int[] valores = {100, 50, 20, 10, 5, 2, 1};
        int[] quantidades = new int[7];
        
        Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();
        int valorOriginal = value;
        
        for (int i = 0; i < valores.length; i++){
            quantidades[i] = value / valores[i];
            value = value % valores[i];
        }
        
        System.out.println(valorOriginal);
        for (int i = 0; i < valores.length; i++){
            System.out.println(quantidades[i] + " nota(s) de R$ " + valores[i] + ",00");
        }
        
        sc.close();
    }
 
}