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

    if (start >= end) // ���Ұ� 1���϶�
        return ;

    key = start; //key�� ù��°����
    i = 1 + start;
    j = end;

    while (i <= j) //�������� ���� �ݺ�
    {
        while (array[key] >= array[i] && i <= end ) //Ű ������ ū ���� ã��������
        {
            i++;
        }

        while (array[key] <= array[j] && j > key) //Ű ������ ���� ���� ã��������
        {
            j--;
        }

        if (i > j) //���������� �Ŀ� ūwhile���� �����Ե�
        {
            swap(array[key], array[j]);
        }
        else //���������ʾ����� i �� j�� ��ü
        {
            swap(array[i], array[j]);
        }
    }

    quicksort(array,start,j-1); //j�� �ִ°��� ���� key�� �ִ����̱⶧���� 
    quicksort(array,j+1,end);   //j�� �������� ���� ���������� ����
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