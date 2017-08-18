import java.io.*;
import java.util.*;

public class LargestProductInASeries {

    public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt();
    for(int q = 0 ; q < T ; q ++)
        {
        int noDigits = scanner.nextInt();
        int K = scanner.nextInt();
        int key = 0;
        String digitString = scanner.next();
        long highestProduct = 0;
        while(key + K <= digitString.length())
            {
            long product = 1;
            for(int i = key; i < (K+key);i++)
                {
                if(digitString.charAt(i) == '0'){key = i; product = 0; break;}
                product *= digitString.charAt(i) - 48;
            }
            if(product > highestProduct)
                {
                highestProduct = product;
            }
            key++;
        }
        System.out.println(highestProduct);
    }
    }
}