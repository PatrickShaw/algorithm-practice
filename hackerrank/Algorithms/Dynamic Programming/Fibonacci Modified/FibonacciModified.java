import java.io.*;
import java.util.*;
import java.math.BigInteger;
public class FibonacciModified {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger t1 = BigInteger.valueOf(scanner.nextInt());
        BigInteger t2 = BigInteger.valueOf(scanner.nextInt());
        int N = scanner.nextInt();
        if(N == 1){System.out.println(t1); return;}
        for(int i = 3;i<= N;i++)
            {
            BigInteger ti = t2.multiply(t2).add(t1);
            t1 = t2;
            t2 = ti;
        }
        System.out.println(t2);
    }
}