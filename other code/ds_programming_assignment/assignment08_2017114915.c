//2017114915 김민수
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS												// fopen,scanf 보안 경고로 인한 컴파일 에러 방지

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define SWAP(a,b,temp) {temp=a; a=b; b=temp;}
int INF = 987654321;

typedef struct input* ip;
struct input
{
	int key;
	ip next;
};

typedef struct
{
	int id;
	int key;
}element;
int id = 0;

typedef struct B_tree* B_heap;
struct B_tree
{
	element data;
	B_heap child;
	B_heap l_link;
	B_heap r_link;
	int degree;
};
B_heap array[10000];

typedef struct queue queue;
struct queue
{
	B_heap node;
};
queue q[10000];
int front = -1, rear = -1;

void B_insert(B_heap*,int);															//이항히프 삽입
void B_min_delete(B_heap*);															//이항히프 최소원소삭제
B_heap B_meld(B_heap*, B_heap*);													//이항히프 병합
void print_B(FILE*,B_heap,int);														//이항히프 출력
void print_level_order(FILE*,B_heap);
B_heap update_min(B_heap);															//min 업데이트
B_heap find_du(B_heap);									

int main(int argc, char* argv[])
{
	FILE* fp1, *fp2, *fp3;
	int input_temp;						
	ip input1 = (ip)malloc(sizeof(struct input)),input2 = (ip)malloc(sizeof(struct input));
	ip root1 = (ip)malloc(sizeof(struct input)), root2 = (ip)malloc(sizeof(struct input));
	root1->next = NULL; root2->next = NULL;


	if (argc != 4)																		//입력파일명 및 출력파일명이 주어지지않으면 에러
	{
		fprintf(stderr, "입력파일명 및 출력파일명 입력이 잘못되었습니다.\n");
		exit(1);
	}

	fp1 = fopen(argv[1], "r");
	if (fp1 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[1]);
		exit(1);
	}

	fp2 = fopen(argv[2], "r");
	if (fp2 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[2]);
		exit(1);
	}

	fp3 = fopen(argv[3], "w");
	if (fp3 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[2]);
		exit(1);
	}

	//key값을 2개의 파일로부터 입력 받음
	
	input1 = root1;
	while(fscanf(fp1, "%d", &input_temp) != EOF)										
	{
		ip temp = (ip)malloc(sizeof(struct input));
		temp->key = input_temp; temp->next = NULL;
		input1->next = temp;
		input1 = input1->next;
	}

	input2 = root2;
	while (fscanf(fp2, "%d", &input_temp) != EOF)										
	{
		ip temp = (ip)malloc(sizeof(struct input));
		temp->key = input_temp; temp->next = NULL;
		input2->next = temp;
		input2 = input2->next;
	}

	fclose(fp1);
	fclose(fp2);


	//첫번째 파일의 key를 min binomial heap에 순서대로 모두 삽입
	B_heap min_tree1 = NULL;

	input1 = root1->next;
	while(1)
	{
		B_insert(&min_tree1, input1->key);

		input1 = input1->next;
		if (!(input1))
			break;
	}

	//모두 삽입 후에 최소 key 삭제연산 
	B_min_delete(&min_tree1);

	//최소 key 삭제후에 min binomial heap을 출력
	print_B(fp3,min_tree1,1);

	//두번째 파일의 key에 대해서도 같은 연산 실행
	B_heap min_tree2 = NULL;

	input2 = root2->next;
	while (1)
	{
		B_insert(&min_tree2, input2->key);

		input2 = input2->next;
		if (!(input2))
			break;
	}

	//모두 삽입 후에 최소 key 삭제연산 
	B_min_delete(&min_tree2);

	//최소 key 삭제후에 min binomial heap을 출력
	print_B(fp3,min_tree2,2);

	//생성한 min binomial heap 2개를 합병한 후에 최소 key 삭제
	B_heap min_tree3 = NULL;

	min_tree3 = B_meld(&min_tree1,&min_tree2);
	B_min_delete(&min_tree3);

	//최소 key 삭제후에 min binomial heap을 출력
	print_B(fp3,min_tree3,3);

	free(root1); free(root2); free(input1); free(input2); 
	free(min_tree1); free(min_tree2); free(min_tree3);
	fclose(fp3);
	return 0;
}

void B_insert(B_heap* min_tree, int data)
{
	B_heap temp = (B_heap)malloc(sizeof(struct B_tree));
	temp->child = NULL; temp->l_link = NULL; temp->r_link = NULL;
	temp->data.key = data; temp->degree = 0; temp->data.id = ++id;

	if (!(*min_tree))
	{
		*min_tree = temp;
	}

	else
	{
		if ((*min_tree)->l_link == NULL && (*min_tree)->r_link == NULL)
		{
			(*min_tree)->l_link = temp;
			(*min_tree)->r_link = temp;
			temp->l_link = *min_tree;
			temp->r_link = *min_tree;
		}

		else
		{
			temp->r_link = *min_tree;
			temp->l_link = (*min_tree)->l_link;
			(*min_tree)->l_link->r_link = temp;
			(*min_tree)->l_link = temp;
			
		}

		if (temp->data.key < (*min_tree)->data.key)														//min 업데이트
			*min_tree = temp;
	}

}

void B_min_delete(B_heap* min_tree)
{

	//step2

	(*min_tree)->l_link->r_link = (*min_tree)->r_link;
	(*min_tree)->r_link->l_link = (*min_tree)->l_link;

	if ((*min_tree)->child)															//최소원소제거후 최소원소의 child을 루트노트에 link
	{
		*min_tree = B_meld(&((*min_tree)->l_link), &((*min_tree)->child));
	}

	*min_tree = update_min((*min_tree)->l_link);

	//step3
	B_heap du1 = *min_tree, du2;
	int exist_du = 1;

	while (1)
	{
		//중복되는 degree 탐색
		while (1)
		{
			du2 = find_du(du1);

			if (du2->data.id == du1->data.id)
			{
				du1 = du1->l_link;

				if (du1->data.id == (*min_tree)->data.id)				//더 이상 중복되는 degree가 없음
				{
					exist_du = 0;
					break;
				}
			}
			else
				break;
		}

		if (exist_du == 0)												//중복되는 degree가 없으므로, 종료
			break;

		//중복되는 degree을 가진 이항트리 병합

		if (du1->data.key < du2->data.key)								//key값이 크면 child로 내려감
		{

			du2->l_link->r_link = du2->r_link;
			du2->r_link->l_link = du2->l_link;
			du2->l_link = NULL; du2->r_link = NULL;

			if (!(du1->child))											//child가 없을경우 
				du1->child = du2;
			

			else														//child가 있을경우 parent가 degree가 더 큰 child를 가리키도록 함
			{															//(degree가 높은 subtree를 왼쪽에 배치)
				if (du2->degree > du1->child->degree)
				{
					if (!(du1->child->l_link))
					{
						du1->child->l_link = du2;
						du1->child->r_link = du2;
						du2->l_link = du1->child;
						du2->r_link = du1->child;
					}
					else
					{
						du2->r_link = du1->child;
						du2->l_link = du1->child->l_link;
						du1->child->l_link->r_link = du2;
						du1->child->l_link = du2;
					}

					du1->child = du2;
				}
			}
			
			du1->degree += 1;
			*min_tree = du1;
		}

		else
		{
			du1->l_link->r_link = du1->r_link;
			du1->r_link->l_link = du1->l_link;
			du1->l_link = NULL; du1->r_link = NULL;

			if (!(du2->child))
				du2->child = du1;


			else
			{
				if (du1->degree > du2->child->degree)
				{
					if (!(du2->child->l_link))
					{
						du2->child->l_link = du1;
						du2->child->r_link = du1;
						du1->l_link = du2->child;
						du1->r_link = du2->child;
					}
					else
					{
						du1->r_link = du2->child;
						du1->l_link = du2->child->l_link;
						du2->child->l_link->r_link = du1;
						du2->child->l_link = du1;
					}

					du2->child = du1;
				}
			}

			du2->degree += 1;
			*min_tree = du2;

		}

		*min_tree = update_min(*min_tree);
		du1 = *min_tree;
	}
}

void print_B(FILE *fp,B_heap min_tree,int n)
{	

	switch (n)
	{
		case 1:
			fprintf(fp, "첫번째 heap\n");
			break;
		case 2:
			fprintf(fp, "두번째 heap\n");
			break;
		case 3:
			fprintf(fp, "세번째 heap\n");
			break;
	}

	//이항히프의 트리들을 degree에 대하여 오른차순으로 배열에 정리

	B_heap temp,now = min_tree;
	int cnt = 0,min,i,j;

	while (1)
	{
		array[cnt++] = now;

		now = now->l_link;

		if (now->data.id == min_tree->data.id)
			break;
	}
	
	for (i = 0; i < cnt; i++)
	{
		min = i;

		for (j = i; j < cnt; j++)
		{
			if (array[j]->degree < array[min]->degree)
				min = j;
		}

		SWAP(array[min], array[i], temp);
	}

	//binomial tree를 차수(degree)의 오름차순으로 출력
	for (i = 0; i < cnt; i++)
	{
		fprintf(fp,"차수 %d :",array[i]->degree);
		print_level_order(fp,array[i]);
		fprintf(fp,"\n");
	}

	fprintf(fp,"\n");
}

void print_level_order(FILE*fp,B_heap root)											//lever order으로 queue를 이용하여 이항트리 출력
{

	B_heap pop, push;

	q[++rear].node = root;
	while (rear != front)
	{
		pop = q[++front].node;

		fprintf(fp, " %d", pop->data.key);
		push = pop->child;

		while (1)
		{
			if (!push)
				break;

			q[++rear].node = push;

			push = push->r_link;

			if (!push || push->data.id == pop->child->data.id)
				break;
		}

	}
}

B_heap B_meld(B_heap* min_tree1, B_heap* min_tree2)									//이항히프 병합, 루트노드들을 link
{
	B_heap min_tree3,temp;

	(*min_tree1)->l_link->r_link = *min_tree2;
	(*min_tree2)->l_link->r_link = *min_tree1;
	temp = (*min_tree1)->l_link;
	(*min_tree1)->l_link = (*min_tree2)->l_link;
	(*min_tree2)->l_link = temp;

	if ((*min_tree1)->data.key < (*min_tree2)->data.key)
		min_tree3 = (*min_tree1);

	else
		min_tree3 = (*min_tree2);

	return min_tree3;
	

}

B_heap update_min(B_heap min_tree)
{
	B_heap temp_min, now;

	now = min_tree->l_link;
	temp_min = min_tree;
	while (1)
	{
		if (now->data.id == temp_min->data.id)
			break;

		if (now->data.key < temp_min->data.key)
			temp_min = now;

		now = now->l_link;
	}
	return temp_min;
}

B_heap find_du(B_heap du1)
{
	B_heap du2=du1->l_link;

	while (1)
	{
		if (du2->degree == du1->degree)
			return du2;

		du2 = du2->l_link;

		if (du2->data.id == du1->data.id)
			return du1;
	}
}