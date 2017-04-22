import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static boolean isPrime(long n) {
        // Start off with the special cases: 1 & 2
        if (n == 1) {
            // 1 is not a prime
            return false;
        }
        else if(n == 2) {
            // 2 is a prime
            return true;
        } else if (n % 2 == 0) {
            // Everything even isn't a prime
            return false;
        } else {
            // We've checked everything 1, 2 and everything even
            // So loop i through all the odd numbers starting from 3 and check if n is divisible by the i
            // Also note that n / (sqrt(n)*sqrt(n)) = 1 and so stop iterating when i > sqrt(n)
            for(long i = 3; i * i <= n; i += 2) {
                if (n % i == 0) {
                    // If n / i is a whole number then n is divisible by i
                    // So n is not a prime
                    return false;
                }
            }
        }
        // At this point we know that n is prime
        return true;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int p = in.nextInt();
        for(int a0 = 0; a0 < p; a0++){
            long n = in.nextInt();
            String output;
            if(isPrime(n)) {
                output = "Prime";
            } else {
                output = "Not prime";
            }
            System.out.println(output);
        }
    }
}