import java.io.*;
import java.util.*;

public class SmallestMultiple {

    public static void main(String[] args) {
        int primeFactors[][] = {{},{}
                    ,{2}
                    ,{3}
                    ,{2,2}
                    ,{5}
                    ,{2,3}
                    ,{7}
                    ,{2,2,2}
                    ,{3,3}
                    ,{2,5}
                    ,{11}
                    ,{2,2,3}
                    ,{13}
                    ,{2,7}
                    ,{3,5}
                    ,{2,2,2,2}
                    ,{17}
                    ,{2,3,3}
                    ,{19}
                    ,{2,2,5}
                    ,{3,7}
                    ,{2,11}
                    ,{23}
                    ,{2,2,2,3}
                    ,{5,5}
                    ,{2,13}
                    ,{3,3,3}
                    ,{2,2,7}
                    ,{29}
                    ,{2,3,5}
                    ,{31}
                    ,{2,2,2,2,2}
                    ,{3,11}
                    ,{2,17}
                    ,{5,7}
                    ,{2,2,3,3}
                    ,{37}
                    ,{2,19}
                    ,{3,13}
                    ,{2,2,2,5}
            };
            Scanner scanner = new Scanner(System.in);
            int T = scanner.nextInt();
            for(int i = 0 ; i < T ;i++)
            {
                    int N = scanner.nextInt();
                    int numberCounts[] = new int[40];
                    for(int k = 0 ; k <= N ; k++)
                    {
                            int thisPrimesCount[] = new int[40];
                            for(int j = 0; j < primeFactors[k].length;j++)
                            {
                                    thisPrimesCount[primeFactors[k][j]]++;
                            }
                            for(int j = 0 ; j < numberCounts.length;j++)
                            {
                                    if(numberCounts[j] < thisPrimesCount[j])
                                    {
                                            numberCounts[j] = thisPrimesCount[j];
                                    }
                            }
                    }
                    int number = 1;
                    for(int j = 0 ; j < numberCounts.length;j++)
                    {
                            for(int k = 0 ; k < numberCounts[j];k++)
                            {
                                    number *= j;
                            }
                    }
                    System.out.println(number);
            }
    }
}