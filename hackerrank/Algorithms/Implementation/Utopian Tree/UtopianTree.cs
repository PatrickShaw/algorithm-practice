using System;
using System.Collections.Generic;
using System.IO;
class UtopianTree {
    static void Main(String[] args) {
        int cases = int.Parse(Console.ReadLine());
        for(int i = 0 ; i < cases ; i ++)
            {
            int height = 1;
            bool doubling = true;
            int cycles = int.Parse(Console.ReadLine());
            for(int o = 0 ;o < cycles;o++ )
                {
                if(doubling){height *= 2;}else{height++;}
                doubling = !doubling;
             
            }
            Console.WriteLine(height);
        }
        }
}
