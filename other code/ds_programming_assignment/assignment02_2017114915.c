//2017114915 김민수

#define _CRT_SECURE_NO_WARNINGS							// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.
#include<stdio.h>
#include<stdlib.h>

int IsFull(int*, int, int);
int IsEmpty(int*, int);
void push(int*, int, int*, int);
void pop(int*, int*);


int main()
{
	int input_cnt, * input, * purpose;					//input_cnt는 정수개수, input은 입력순서, purpose는 목표순서
	char f_name[100];
	int i;
	int* stack = NULL, top = -1, MAX_STACK_SIZE;		//스택에 관련된 변수들
	FILE* fp;

	printf("파일 이름을 입력하시오 : ");
	scanf("%s",f_name);									//파일이름입력

	fp = fopen(f_name,"r");					
	if (fp == NULL)										//파일열기 실패시 error
	{
		printf("error : 해당파일열기를 실패하였습니다.\n");
		return 0;
	}

	fscanf(fp, "%d", &input_cnt);						//파일의 첫번째 숫자를 input_cnt에 할당
	if (input_cnt <= 0)									//input_cnt이 양수가 아닐 시 error
	{
		printf("error : 입력될 숫자들의 개수가 음수입니다.\n");
		return 0;
	}

	input = (int*)malloc(input_cnt * sizeof(int));		//input과 purpose를 입력될 정수개수만큼 동적할당
	purpose = (int*)malloc(input_cnt * sizeof(int));

	for (i = 0; i < input_cnt; i++)						//input에 입력순서 입력
		fscanf(fp, "%d",&input[i]);
	for (i = 0; i < input_cnt; i++)						//purpose에 목표순서 입력
		fscanf(fp, "%d", &purpose[i]);

	MAX_STACK_SIZE = input_cnt;;						
	stack = (int*)malloc(sizeof(int) * MAX_STACK_SIZE);	//stack생성

	int input_index = 0, pur_index = 0;					//input_index는 입력순서 index, pur_index는 목표순서 index

	printf("입력: ");
	for (i = 0; i < input_cnt; i++)
		printf("%d ",input[i]);
	printf("목표: ");
	for (i = 0; i < input_cnt; i++)
		printf("%d ", purpose[i]);

	while (1)													//기찻길 문제 본문, 기차가 순서에 맞게 왼쪽 기찻길로 한대씩 가면, pur_index++한다.
	{
		if (pur_index ==input_cnt)								//성공, 목표순서의 index가 배열 끝까지갔다.(왼쪽길로 순서에 맞게 나갔다.)
		{
			printf("→ YES\n");
			break;
		}


		if (input_index < input_cnt)							//오른쪽 기찻길에 기차가 남았을 때
		{
			if (input[input_index] == purpose[pur_index])		//오른쪽 기찻길위 번호와 목표순서의 번호가 같을때, 오른쪽 기차를 왼쪽으로 보낸다.
			{
				input_index++;
				pur_index++;
				continue;
			}

			else if (IsEmpty(stack, top) == 1)					//위 조건이 맞지않고, 아래 기차길이 비었을때(stack이 empty),오른쪽 기찻길위 기차를 아랫쪽으로 push한다.
			{
				push(stack, input[input_index], &top, MAX_STACK_SIZE);
				input_index++;
				continue;
			}

			else if (stack[top] == purpose[pur_index])			//위 조건들이 맞지않고, stack(아래 기찻길)의 번호와 목표순서의 번호가 같을때, 아래 기차를 왼쪽으로 pop한다.
			{
				pop(stack, &top);
				pur_index++;
				continue;
			}

			else												//위 조건들이 맞지않을때, 오른쪽 기차를 아래로 push한다.
			{
				push(stack, input[input_index], &top, MAX_STACK_SIZE);
				input_index++;
				continue;
			}
		}
		


		else													//오른쪽 기찻길에 기차가 없을 때
		{
			if (stack[top] == purpose[pur_index])				//아래 기찻길의 번호와 목표순서의 번호가 같을때, 아래 기차를 왼쪽 기찻길로 pop한다.
			{
				pop(stack, &top);
				pur_index++;
				continue;
			}

			else												//실패, 순서에 맞게 기차들이 왼쪽으로 나갈 수 있는 경우의수가 존재하지않는다.
			{
				printf("→ NO\n");
				break;
			}
				
		}

			
	}
	
	return 0;
}

int IsFull(int* stack, int MAX_STACK_SIZE, int top)		//stack에 남는 공간없는지 확인
{
	if (MAX_STACK_SIZE - 1 == top)
		return 1;
	else
		return 0;

}

int IsEmpty(int* stack, int top)						//stack에 데이터가 비었는지 확인
{
	if (top < 0 )
		return 1;
	else
		return 0;
}

void push(int* stack, int data,int* top, int MAX_STACK_SIZE)	//stack에 데이터 삽입, 남는공간없는지 먼저확인
{
	if (IsFull(stack, MAX_STACK_SIZE, top) == 1)
		printf("error : stack is FULL\n");
	else
	{
		*top += 1;
		stack[*top] = data;
	}
}

void pop(int* stack, int *top)							//stack에서 데이터삭제, 데이터가 존재하는지 먼저확인
{
	if (IsEmpty(stack, top) == 1)
		printf("error : stack is EMPTY\n");
	else
	{
		*top -= 1;
	}
}