import java.io.*;
import java.util.*;

public class LonelyInteger {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int isPair[] = new int[101];
        for (int n = 0; n < N;n++)
            {
            isPair[scanner.nextInt()]++;
        } 
        for(int i = 0 ; i < isPair.length;i++)
            {
            if(isPair[i] == 1)
                System.out.println(i);
        }
    }
}