#include<stdio.h>
#include <climits>
#define swap(a,b) {int t; t=a; a=b; b=t;}

int main()
{
    int i, j, min, index;
    int array[10] = { 1,4,5,3,6,8,10,2,7,9 };

    for (i = 0; i < 10; i++)
    {
        min = INT_MAX;
        for (j = i; j < 10; j++)
        {
            if (min > array[j])
            {
                index = j;
                min = array[j];
            }
        }
        swap(array[i], array[index]);
    }

    for (i = 0; i < 10; i++)
    {
        printf("%d ",array[i]);
    }
        
}