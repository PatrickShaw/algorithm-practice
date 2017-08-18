#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>      /* printf */
#include <math.h>       /* sqrt */
using namespace std;
long LargestPrime(long number)
    { 
    if(number % 2 == 0)
        {
        number /= 2;
        return LargestPrime(number);
    }
    long  sqrt = std::sqrt(number);
    for( long i = 3; i <= sqrt;i++)
        {
        if (number % i == 0)
        {
            number /= i;
             long otherPrime = LargestPrime(number);
            if(otherPrime > i)
                {
                return otherPrime;
            }
            return i;
        }
    }
    return number;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;
    while(T--)
        { 
         long N;
        cin >> N; 
        cout << LargestPrime(N) << endl; 
    }
    } 
