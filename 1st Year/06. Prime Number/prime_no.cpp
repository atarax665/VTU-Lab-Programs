/*To implement functions to check if a number is prime or not in c++*/
#include <iostream>
#include <math.h>

using namespace std;

int isprime (int n)
{
    /*
Function that returns
0 --> when n is not a prime
1 --> when n is a prime
*/
    int r;
    if(n == 1 || n == 0)
    {
        return 0;
    }
    /*Check only till sqrt(n) because every composite number has atleast one
    prime factor less than or equal to square root of itself*/
    for(int i = 2; i <= sqrt(n); i++)
    {
        if(n % i == 0)
        {
            return 0;
        }
    }

    return 1;
}

int main ()
{
    int f, n; //Works only for small integers, i.e n<32767

    cout << "Enter the number: "<<endl;
    cin >> n;

    //Assigning f as 0 or 1
    f = isprime(n);


    //Same as if(f == 1)
    if(f)
    {
        cout<< n << " is a prime number.\n"<<endl;
    }
    else
    {
        cout<< n << " is not a prime number.\n"<<endl;
    }
    return 0;
}


/*
Time Complexity: O(sqrt(n))

Sample I/O

Input: Enter the number: 17
Output: 17 is a prime number.

Input: Enter the number: 39
Output: 39 is not a prime number.
*/
