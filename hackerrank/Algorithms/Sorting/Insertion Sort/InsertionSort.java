import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class InsertionSort {
    
    
    public static void printAr(int ar[])
        {
        String str = Integer.toString(ar[0]); 
        for(int i = 1 ; i < ar.length;i++)
            {
            str += " ";
            str += Integer.toString(ar[i]);
        }
        System.out.println(str);
    }
    public static void insertIntoSorted(int[] ar) {
        for(int i=1; i < ar.length;i++)
            {
            int temp = ar[i];
            int j;
            for(j = i - 1; j >=0 && temp < ar[j];j--)
                {
                ar[j+1] = ar[j];
                printAr(ar);
            }
            ar[j + 1] = temp;
        }
            printAr(ar);
    }
    
    
/* Tail starts here */
     public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int[] ar = new int[s];
         for(int i=0;i<s;i++){
            ar[i]=in.nextInt(); 
         }
         insertIntoSorted(ar);
    }
    
    
    private static void printArray(int[] ar) {
      for(int n: ar){
         System.out.print(n+" ");
      }
        System.out.println("");
   }
    
    
}
