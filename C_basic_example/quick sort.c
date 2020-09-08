#include<stdio.h>
#include <climits>
#define swap(a,b) {int t; t=a; a=b; b=t;}

void quicksort(int* array, int start, int end)
{
    int i, j, key;

    for (i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");

    if (start >= end) // 원소가 1개일때
        return ;

    key = start; //key는 첫번째원소
    i = 1 + start;
    j = end;

    while (i <= j) //엇갈릴떄 까지 반복
    {
        while (array[key] >= array[i] && i <= end ) //키 값보다 큰 것을 찾을떄까지
        {
            i++;
        }

        while (array[key] <= array[j] && j > key) //키 값보다 작은 것을 찾을떄까지
        {
            j--;
        }

        if (i > j) //엇갈렷을때 후에 큰while문을 나가게됨
        {
            swap(array[key], array[j]);
        }
        else //엇갈리지않았으면 i 와 j를 교체
        {
            swap(array[i], array[j]);
        }
    }

    quicksort(array,start,j-1); //j에 있는값이 원래 key에 있던값이기때문에 
    quicksort(array,j+1,end);   //j를 기준으로 왼쪽 오른쪽으로 나눔
}

int main()
{
    int i;
    int array[10] = { 1,4,5,3,6,8,10,2,7,9 };

    quicksort(array, 0, 9);
    
    printf("***************************\n");
    for (i = 0; i < 10; i++)
    {
        printf("%d ",array[i]);
    }
    printf("\n");
        
}