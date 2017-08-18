import java.io.*;
import java.util.*;

public class IntroToTutorialChallenges {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int V = scanner.nextInt();
        int n = scanner.nextInt();
        int array[] = new int[n];
        for(int i = 0 ; i < n;i++)
            {
            array[i] = scanner.nextInt();
        }
        int min = 0;
        int max = n-1;
        while(min <= max)
            {
            int middle = (min+max) / 2; 
            if(array[middle] == V){System.out.println(middle);return;}
            if(array[middle] < V)
            {
                min = middle+1;
            }
            else
                {
                max = middle - 1;
            }
        }
        System.out.println(-1);
    }
}