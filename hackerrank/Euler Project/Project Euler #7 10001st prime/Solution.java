import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
         ArrayList<Long> primes = new ArrayList<Long>();
        Long t = new Long(3);
            primes.add(new Long(2));
        while(primes.size() <= 10000)
            {
            Long sqrtT = new Long((long)Math.sqrt(t));
            if(t%2==1){
                boolean divided = false;
            for(int i = 3; i <= sqrtT;i+=2)
                if(t % i == 0){divided = true;break;}
                if(!divided){primes.add(t);}
                }
            t += 2;
        }
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i = 0;  i < T ;i++)
            {
            System.out.println(primes.get(scanner.nextInt()-1));
        }
    }
}