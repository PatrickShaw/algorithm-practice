import java.io.*;
import java.util.*;

public class DiagonalDifference {

    public static void main(String[] args) { 
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int array[][] = new int[N][];
    for(int q = 0 ;q < N;q++)
        {
        array[q] = new int[N];
        for(int j = 0 ; j < N ; j++)
            {
            array[q][j] = scanner.nextInt();
        }
    }
    int sum1 = 0;
        int sum2 = 0;
    for(int i = 0 ; i < N; i++)
    {
        sum1 += array[i][i];
        sum2 += array[i][(N-1) - (i)];
    }
    System.out.println(Math.abs(sum1-sum2));
    }
}