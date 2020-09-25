//2017114915 김민수

#define _CRT_SECURE_NO_WARNINGS							// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.
#include<stdio.h>
#include<stdlib.h>

typedef struct element									//노드에 숫자와 노드의레벨 기록
{
	int data;
	int level;
}element;

struct node												//이진트리 노드
{
	element element;
	struct node* l_link;
	struct node* r_link;
};

struct node* add_tree(int, struct node*);
void add_q(int,int*,struct node*, struct node**);
struct node* delete_q(int*,int, struct node**);


int main()
{
	FILE* fp;
	int temp,cnt=0;
	char f_name[100];

	struct node* root = (struct node*)malloc(sizeof(struct node));		//root노드
	root->element.level = 0;

	printf("파일 이름을 입력하시오 : ");
	scanf("%s", f_name);								//파일이름입력

	fp = fopen(f_name, "r");
	if (fp == NULL)										//파일열기 실패시 error
	{
		printf("error : 해당파일열기를 실패하였습니다.\n");
		return 0;
	}

	
	while (fscanf(fp,"%d",&temp) != -1)					//이진트리 생성
	{
		root = add_tree(temp,root);
		cnt++;											//입력되는 데이터의 수 기록
	}


	struct node** queue = (struct node**)malloc(cnt * sizeof(struct node*));		//입력된 데이터의 수를 max_queue_size로 설정
	struct node* tmp = (struct node*)malloc(sizeof(struct node));
	int front = -1, rear = -1;

	if (root->element.level != 0)						//이진트리에서 각 level의 가장 오른쪽 node 찾기
	{
		tmp = root;

		add_q(front, &rear, tmp, queue);				//queue에 root node삽입

		while (1)
		{
			tmp = delete_q(&front, rear, queue);		//queue에서 node를 삭제

			if (tmp)
			{

				if (tmp->l_link)						//queue에 child nodes삽입
				{
					add_q(front, &rear, tmp->l_link, queue);
				}

				if (tmp->r_link)						//queue에 child nodes삽입
				{
					add_q(front, &rear, tmp->r_link, queue);
				}

				if (front == rear)																	//queue의 마지막노드일 때
				{
					printf("(%d , %d) ", tmp->element.level, tmp->element.data);					//현재 level 값의 맨 오른쪽 데이터 출력
					break;																			//끝
				}

				else if ((tmp->element.level != queue[front + 1]->element.level) || (front==rear))	//현재 level값의 마지막node일 떄
					printf("(%d , %d) ", tmp->element.level, tmp->element.data);					//현재 level 값의 맨 오른쪽 데이터 출력
			}

		}
	}

	free(queue);
	free(tmp);
	free(root);
	fclose(fp);
	return 0;
}

struct node* add_tree(int data, struct node* root)
{
	struct node* temp_root = (struct node*)malloc(sizeof(struct node));
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->element.data = data;
	temp->l_link = NULL;
	temp->r_link = NULL;

	if (root->element.level ==0)				//queue가 비어있을떄 root노드 생성
	{
		temp->element.level = 1;
		return temp;
	}
	else										//queue가 비어있지 않을때
	{
		temp_root = root;

		while (1)
		{
			if (data < temp_root->element.data)		//root노드보다 작을 경우
			{
				if (temp_root->l_link == NULL)		//root노드 왼쪽subtree가 비어있을 경우, 왼쪽subtree에 할당 
				{
					temp->element.level = temp_root->element.level + 1;
					temp_root->l_link = temp;
					break;
				}

				else								//비어있지않을 경우, 왼쪽subtree로 이동
				{
					temp_root = temp_root->l_link;
					continue;
				}
			}

			else									//root노드보다 크거나 같을 경우
			{
				if (temp_root->r_link == NULL)		//root노드 오른쪽subtree가 비어있을 경우, 오른쪽subtree에 할당 
				{
					temp->element.level = temp_root->element.level + 1;
					temp_root->r_link = temp;
					break;
				}

				else								//비어있지않을 경우,오른쪽subtree로 이동
				{
					temp_root = temp_root->r_link;

				}


			}

		}

		return root;

	}
}

void add_q(int front, int* rear, struct node* temp, struct node** queue)
{
	(*rear)++;										//queue의 max size가 입력된 데이터의 개수로 설정했으므로, 이를 초과할수없음
	queue[*rear] = temp;
}
struct node* delete_q(int* front, int rear, struct node** queue)
{
	(*front)++;										//empty 검사는 main함수 내에서 front==rear로 하는 중
	return queue[*front];

}