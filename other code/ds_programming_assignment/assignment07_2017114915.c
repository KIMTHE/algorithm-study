//2017114915 김민수
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS												// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int INF = 987654321;
#define SWAP(a,b,temp) {temp=a; a=b; b=temp;}

typedef struct
{
	int key;
}element;

typedef struct leftist* leftistTree;
struct leftist
{
	element data;
	leftistTree leftChild;
	leftistTree rightChild;
	int shortest;
};

typedef struct queue queue;
struct queue
{
	leftistTree *node;
};

void minMeld(leftistTree*, leftistTree*);									//두 최소 좌향 트리의 합병
void minUnion(leftistTree* , leftistTree* );								//공백이 아닌 두 최소트리의 합병
void print_tree(FILE*, leftistTree,int);										//min leftist tree 출력


int main(int argc, char* argv[])
{
	FILE* fp1, *fp2;
	int input_key[1000],input_cnt=0;										//최대입력 key를 1000개로 가정
	int input_temp,i;


	if (argc != 3)																		//입력파일명 및 출력파일명이 주어지지않으면 에러
	{
		fprintf(stderr, "입력파일이름 입력이 잘못되었습니다.\n");
		exit(1);
	}

	fp1 = fopen(argv[1], "r");
	if (fp1 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[1]);
		exit(1);
	}

	fp2 = fopen(argv[2], "w");
	if (fp2 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[2]);
		exit(1);
	}

	while(fscanf(fp1, "%d", &input_temp) != EOF)										//key 입력받음
	{
		input_key[input_cnt++] = input_temp;
	}

	fclose(fp1);

	//정수4개로 min leftist tree를 생성하여 queue에 삽입

	queue q[10000], q_return1,q_return2;
	int rear = -1, front = -1;
	leftistTree a;
	leftistTree b;
	a = NULL;
	
	for (i = 0; i < input_cnt; i++)
	{
		b = (struct leftist*)malloc(sizeof(struct leftist));
		b->data.key = input_key[i];
		b->leftChild = NULL; b->rightChild = NULL; b->shortest = 1;
		minMeld(&a, &b);																//정수 key를 하나씩 삽입하면서 tree 생성

		if ((i + 1) % 4 == 0)
		{
			q[++rear].node = a;

			print_tree(fp2, a,rear+1);													//queue에 min leftist tree를 삽입할 때 tree를 출력	

			a = NULL;
		}

		else if ((i + 1) == input_cnt)													//마지막에는 4개 이하로 된 min leftist tree 생성
		{
			q[++rear].node = a;

			print_tree(fp2, a,rear+1);													//queue에 min leftist tree를 삽입할 때 tree를 출력

			a = NULL;
		}
	}

	// queue에서 leftist tree 2개를 가져와서 합병하여 다시 queue에 삽입하는 과정을 반복하여 하나의 min leftist tree 생성

	while (rear != front+1)															//하나의 min leftist tree이 남을 때까지 반복
	{
		q_return1 = q[++front];
		q_return2 = q[++front];

		a = q_return1.node;
		b = q_return2.node;
		minMeld(&a, &b);

		q[++rear].node = a;
		print_tree(fp2, a,rear+1);													//queue에 min leftist tree를 삽입할 때 tree를 출력
		a = NULL;
	}



	fclose(fp2);
	return 0;
}

void minMeld(leftistTree* a, leftistTree* b)
{
	if(!*a) 
		*a = *b;
	else if(*b) 
		minUnion(a, b);

	*b = NULL;
}
void minUnion(leftistTree* a, leftistTree* b)
{
	leftistTree* temp;

	if ((*a)->data.key > (*b)->data.key) 
		SWAP(*a, *b, temp);

	if (!(*a)->rightChild) 
		(*a)->rightChild = *b;
	else 
		minUnion(&(*a)->rightChild, b);

	if (!(*a)->leftChild) 
	{
		(*a)->leftChild = (*a)->rightChild;
		(*a)->rightChild = NULL;
	}
	else if ((*a)->leftChild->shortest < (*a)->rightChild->shortest)
		SWAP((*a)->leftChild, (*a)->rightChild, temp);

	(*a)->shortest = (!(*a)->rightChild) ? 1 :(*a)->rightChild->shortest + 1;
}

void print_tree(FILE* fp, leftistTree root, int cnt)
{
	leftistTree temp;
	queue q[10000], q_return;															//queue를 배열로 설정해서 overflow위험
	int print_key[10000], print_index = 0, i;				
	int rear = 0, front = 0, tree_level =1;

	fprintf(fp, "%d번째 트리\n", cnt);

	q[++rear].node = root;
	while (rear != front)
	{
		temp = NULL;

		q_return = q[++front];
		temp = q_return.node;

		if (!temp || !temp->leftChild  )
			q[++rear].node = NULL;
		else
			q[++rear].node = temp->leftChild;

		if (!temp || !temp->rightChild)
			q[++rear].node = NULL;
		else
			q[++rear].node = temp->rightChild;


		if (!temp)
			print_key[++print_index] = INF;
		else
			print_key[++print_index] = temp->data.key;
																								//한 레벨의 key들이 모두 null이면 종료
		if (front == (int)pow(2, tree_level) - 1)												//각 레벨의 key들을 모두 모아서 한번에 출력한다.
		{
			for (i = (int)pow(2, (int)(tree_level-1)); i <= (int)pow(2, tree_level) - 1; i++)
			{
				if (print_key[i] == 0) printf("%d\n",i);

				if (print_key[i] != INF)
					break;
			}
			if (i == (int)pow(2, tree_level))
				break;

			for (i = (int)pow(2, (int)(tree_level - 1)); i <= (int)pow(2, tree_level) - 1; i++)
			{
				if (print_key[i] != INF)
					fprintf(fp,"%d ",print_key[i]);
				else
					fprintf(fp, "%% ");
			}

			tree_level++;
			fprintf(fp, "\n");
		}
	}

	fprintf(fp, "\n");
}
