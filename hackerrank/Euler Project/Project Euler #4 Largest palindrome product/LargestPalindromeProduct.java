import java.io.*;
import java.util.*;

public class LargestPalindromeProduct {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i = 0 ; i< T;i++)
            {
            int N = scanner.nextInt();
            
            int largest = 0;
            for(int q =1; q <= 999;q++)
            {
                for(int o = 1 ; o <= 999;o++)
                {
                    int val = o * q;
                    if( val < N)
                        {
                        if(val > largest)
                        {
                    if(isPalindrome(val))
                    {
                            largest = val;
                        }
                    }
                    }
                    else{
                        break;
                    }
                }
            }
            System.out.println(largest);
        }
        
    }
    public static boolean isPalindrome(int number)
        { 
        String string = Integer.toString(number);
        for(int i =0 ; i < string.length()/2;i++)
            {
            if(string.charAt(i) != string.charAt(string.length() - (i +1)))
                {
                return false;
            }
        }
        return true;
    }
}