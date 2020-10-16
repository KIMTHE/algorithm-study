//2017114915 김민수
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS											// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct edge														//edge 구조체
{
	int vnum1;
	int vnum2;
}edge;

void stack_push(int*, int*, int, int);
char stack_pop(int*, int*);


int main(int argc, char* argv[])
{
	FILE* fp;
	int v_cnt, e_cnt, i, j;



	if (argc != 2)														//입력파일이름이 주어지지않으면 에러
	{
		fprintf(stderr, "입력파일이름 입력이 잘못되었습니다.\n");
		exit(1);
	}

	fp = fopen(argv[1], "r");
	if (fp == NULL)														//파일열기 실패시 error
	{
		fprintf(stderr, "error : 해당파일열기를 실패하였습니다.\n");
		exit(1);
	}

	fscanf(fp, "%d %d", &v_cnt, &e_cnt);								//vertex, edge 개수 입력
	edge* E = (edge*)malloc(sizeof(edge) * e_cnt);
	for (i = 0; i < e_cnt; i++)											//edge입력
	{
		fscanf(fp, "%d %d", &E[i].vnum1, &E[i].vnum2);
	}

	int** V = (int**)malloc(sizeof(int*) * (v_cnt + 1));
	for (i = 1; i <= v_cnt; i++)										//graph는 matrix로 표현
	{
		V[i] = (int*)calloc(v_cnt + 1, sizeof(int));
	}

	for (i = 1; i <= v_cnt; i++)										//graph matrix에  graph표현
	{
		for (j = 0; j < e_cnt; j++)
		{
			if (E[j].vnum1 == i)
				V[i][E[j].vnum2] = 1;

			else if (E[j].vnum2 == i)
				V[i][E[j].vnum1] = 1;
		}
	}

	//tree 체크시작

	printf("탐색방법 : DFS, graph표현 : matrix \n");

	int* stack = (int*)malloc(sizeof(int) * v_cnt);
	int* visit = (int*)calloc(v_cnt + 1, sizeof(int));					//방문여부를 체크하는 배열
	int* path = (int*)calloc((v_cnt + 1)*2, sizeof(int));				//경로를 저장하는 배열
	int* cycle = (int*)calloc(v_cnt + 1, sizeof(int));					//cycle경로 저장하는 배열
	int top = -1, cnt = -1,cycle_index, pop=0;
	int is_cycle = 0, is_tree = 0, is_notconnect = 0;

	int now = 0, next = 1;												//탐색은 1부터 시작
	while (1)															//스택을 이용한 DFS
	{
		now = next;
		visit[now] = 1;
																		

		if(pop == 0)													//이전에 pop된 vertex는 path에 저장하지않음
			path[++cnt] = now;

		for (i = 1; i <= v_cnt; i++)									//visit배열을 이용하여 vertex의 방문확인
		{
			if (visit[i] == 0)
				break;
		}
		if (i > v_cnt)													//모두 방문하였으면, tree이다, DFS종료
		{
			is_tree = 1;
			break;
		}

		for (i = 1; i <= v_cnt; i++)
		{
			if (is_cycle == 0 && V[now][i] == 1 && top >= 0 && stack[top] != i && visit[i] == 1 && pop == 0)	//연결된 vertex중 부모vertex가 아니고,이미 방문한 vertex가 존재하고,
			{																									//이전에 pop되서 자식vertex가 아니라면,
				is_cycle = 1;																		//cycle이 존재한다.
				for (j = 0; j <= cnt; j++)															//cycle경로 저장
					cycle[j] = path[j];
				cycle_index = j;
				cycle[cycle_index] = i;
			}

			if (V[now][i] == 1 && visit[i] == 0 && now==next)			//연결된 vertex중 방문안한것을 다음vertex로 설정
			{
				next = i;
			}
		}
		
		pop = 0;

		if (now == next)												//연결된 vertex들이 모두 방문되었을 때,
		{
			if (top >= 0)												//다음vertex는 stack에서 pop으로 parent를 가져온다.
			{
				next = stack_pop(stack, &top);
				pop = 1;
				continue;
			}

			else if (top < 0)											//stack이 비었다면, 나머지 방문안한 vertex는 연결이 되지 않았다, DFS종료
			{
				is_notconnect = 1;
				break;
			}
		}


		stack_push(stack, &top, v_cnt, now);

	}

	//결과 출력

	if (is_cycle == 1)
	{
		printf("\n이 graph는 cycle이 포함되므로 tree가 아닙니다.\ncycle :");
		for (i = 0; i <= cycle_index; i++)
			printf(" %d", cycle[i]);
		printf("\n");
	}

	if (is_notconnect == 1)
	{
		printf("\n이 graph는 연결되지 않은 vertex가 포함되므로 tree가 아닙니다.\n");
		printf("not connected vertex :\n");

		for (i = 1; i <= v_cnt; i++)
		{
			if (visit[i] == 0)
			{
				printf("vertex %d는 vertex %d와 연결되어있지않습니다.\n",i,now);
			}
		}
	}

	if (is_tree == 1 && is_cycle == 0 && is_notconnect == 0)
	{
		printf("\n이 graph는 tree입니다.\n");
	}

	return 0;
}


void stack_push(int* stack, int* top, int MAX_stack, int data)
{
	if (*top >= MAX_stack)
	{
		fprintf(stderr, "STACK IS FULL ERROR\n");
		exit(1);
	}

	stack[++(*top)] = data;
}

char stack_pop(int* stack, int* top)
{
	if (*top < 0)
	{
		fprintf(stderr, "STACK IS EMPTY ERROR\n");
		exit(1);
	}

	return stack[(*top)--];
}


