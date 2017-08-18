import java.io.*;
import java.util.*;

public class SherlockAndArray {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int w = 0 ;w < T ; w++)
            {
            int length = scanner.nextInt();
            int array[] = new int[length];
            for(int q = 0; q < length; q++)
                {
                array[q] = scanner.nextInt();
            }
            int min = 0;
            int max = length - 1;
            boolean equal = false;
            while(min <= max)
                {
            int key = (min + max) /2;
                long sumLeft =0;
                long sumRight = 0;
                for(int i = 0 ;i < key;i++)
                    {
                    sumLeft += array[i]; 
                }
                for(int i = key+1; i < length;i++)
                {
                    sumRight += array[i];
                }
                if(sumRight == sumLeft)
                    {
                    equal = true;
                    break;
                }
                if(sumRight>sumLeft)
                    {
                    min = key+ 1;
                }
                else{                    max = key - 1;

                }
            }
            if(equal)
                {
                System.out.println("YES");
            }else{System.out.println("NO");}
        }
    }
}