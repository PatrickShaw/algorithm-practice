import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for(int i = 0; i < T ; i ++)
            {
            long N = scanner.nextInt();
            long sqrSum = 0;
            for(int j = 1; j <= N; j++)
                {
                sqrSum += j *j;
            }
            long sumSqr = N* (N+1)/2;
            sumSqr *= sumSqr;
            System.out.println(sumSqr - sqrSum);
        }
    }
}