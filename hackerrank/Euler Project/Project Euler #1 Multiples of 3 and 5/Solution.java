import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i = 0 ; i < T; i++)
            {
            long N = scanner.nextInt();
            long n = N - 1;
            
            long nd3 = n/3;
            long factors3sum = 3 * nd3*(nd3 + 1)/2;
            long nd5 = n/5;
            long factors5sum = 5 * nd5*(nd5 + 1)/2;
            long nd15 = n/15;
            long factors15sum = 15 * nd15*(nd15 + 1)/2;
            System.out.println(factors3sum + factors5sum - factors15sum);
        }
    }
}