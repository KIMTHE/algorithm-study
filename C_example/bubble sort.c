#include<stdio.h>
#include <climits>
#define swap(a,b) {int t; t=a; a=b; b=t;}

int main()
{
    int i, j;
    int array[10] = { 1,4,5,3,6,8,10,2,7,9 };

    for (i = 0; i < 10; i++)
    {        
        for (j = 0; j < 9-i; j++)
        {
            if(array[j] > array[j+1])
                swap(array[j], array[j+1]);
        }
        
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ",array[i]);
    }
        
}