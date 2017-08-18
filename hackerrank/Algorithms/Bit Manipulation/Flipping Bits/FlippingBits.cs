using System;
using System.Collections.Generic;
using System.IO;
class FlippingBits {
    static void Main(String[] args) {
        int T = int.Parse(Console.ReadLine());
        for(int i = 0;  i < T;i++)
            {
            uint number = uint.Parse(Console.ReadLine());
            
                //Console.WriteLine(Convert.ToString(number, 2).PadLeft(32, '0'));
            for(int q = 0; q < 32;q++)
                {
                if(number % 2 == 0)
                    {
                number >>= 1;
                    number += (uint)1 << 31;
                }
                else
                    {
                    
                number >>= 1;
                }
                //Console.WriteLine(Convert.ToString(number, 2).PadLeft(32, '0'));
            }
            Console.WriteLine(number);
        }
    }
}