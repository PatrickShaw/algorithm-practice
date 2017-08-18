import java.io.*;
import java.util.*;

public class ArraysDS {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int array[] = new int[scanner.nextInt()];
        for (int i =0 ; i < array.length;i++)
            {
            array[i] = scanner.nextInt();
        }
        String outputString = "";
        for(int i = array.length - 1; i >= 0;i--)
            {
            outputString += Integer.toString(array[i]) + " ";
        }
        System.out.println(outputString);
    }
}