//2017114915 김민수
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS												// fopen,scanf 보안 경고로 인한 컴파일 에러 방지

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define SWAP(a,b,temp) {temp=a; a=b; b=temp;}
int INF = 987654321;
int tmp;

typedef struct input* ip;
struct input								//입력파일에서 입력되는 key, 개수는 제한이 없음
{
	int key;
	ip next;
};

typedef struct								//tree node의 원소
{
	int key;
}element;

typedef struct M_tree* tree_23;				//tree node (3-way)
struct M_tree
{
	element data[2];
	element data_error;
	tree_23 sub[4];							//sub[3] = temp

	int level;
	int key_cnt;
};

typedef struct queue
{
	tree_23* node;
}Q;
		
int t23Insert(tree_23* ,int,int, int*);		//2-3 tree에 특정 key 삽입
void div_t23(tree_23*, int, int*);			//2-3 tree에 삽입중 분할
int t23remove(tree_23*, int,int*);			//2-3 tree에서 특정 key제거
void rot_t23(tree_23*, int,int, int*);		//2-3 tree에서 제거중 회전수행
void com_t23(tree_23*, int, int,int*);		//2-3 tree에서 제거중 결합수행
void print_t23(tree_23*,int,int,FILE*);		//2-3 tree의 node를 queue를 이용하여 레벨에 따라서 출력
Q add_q(tree_23*);

int main(int argc, char* argv[])											//입력 파일과 출력 파일 이름은 명령줄에서 주어짐 (argc, argv)
{
	FILE* fp1, *fp2;
	int input_temp,input_cnt=0;						
	ip input = (ip)malloc(sizeof(struct input));
	ip root_ip = (ip)malloc(sizeof(struct input));
	root_ip->next = NULL;


	if (argc != 3)																		//입력파일명 및 출력파일명이 주어지지않으면 오류처리
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

	fp2 = fopen(argv[2], "w");
	if (fp2 == NULL)																	//파일열기 실패시 error
	{
		fprintf(stderr, "error : 파일 %s 열기를 실패하였습니다.\n", argv[2]);
		exit(1);
	}


	//key값을 파일로부터 입력 받음
	input = root_ip;
	while(fscanf(fp1, "%d", &input_temp) != EOF)										
	{
		ip temp = (ip)malloc(sizeof(struct input));
		temp->key = input_temp; temp->next = NULL;
		input->next = temp; input_cnt++;
		input = input->next;
	}

	fclose(fp1);

	//주어진 key값에 대하여, 양수는 삽입하고 음수는 절대값을 삭제하여 2-3 tree 생성

	tree_23 root = NULL;
	int is_unbalanced = 0,n=0,is_change=0;

	input = root_ip->next;
	while(input != NULL)
	{
		if (input->key >= 0)
		{
			is_change = t23Insert(&root, input->key,1, &is_unbalanced);
			if (is_change == 0) fprintf(stdout,"key가 이미 tree에 존재합니다.\n\n");

			else if (is_unbalanced == 1)		//루트노드가 분할해야할때,
			{
				tree_23 temp = (tree_23)malloc(sizeof(struct M_tree));
				temp->sub[0] = root;
				temp->sub[1] = temp->sub[2] = temp->sub[3] = NULL;
				temp->data[0].key = -1; temp->data[1].key = -1; temp->data_error.key = -1;
				temp->key_cnt = 0; temp->level = 1;

				root = temp;
				div_t23(&root, 0, &is_unbalanced);
			}
		}
		else if (input->key < 0)
		{
			is_change = t23remove(&root, -1 * (input->key), &is_unbalanced);
			if (is_change == 0) fprintf(stdout, "key가 tree에 존재하지않습니다.\n\n");
		}

		//key를 삽입 또는 삭제할 때마다 2-3 tree 출력
		if(is_change == 1)
			print_t23(&root, input_cnt,++n, fp2);

		input = input->next;
	}

	free(root);
	fclose(fp2); free(input); free(root_ip);
	return 0;
}

int t23Insert(tree_23* parent, int key,int level, int* unbalanced)
{	
	if (!*parent)												//빈 subtree root에 삽입, 빈 key는 -1
	{							
		tree_23 temp = (tree_23)malloc(sizeof(struct M_tree));
		*parent = temp;
		(*parent)->sub[0] = (*parent)->sub[1] = (*parent)->sub[2] = (*parent)->sub[3] = NULL;
		(*parent)->data[0].key = key; (*parent)->data[1].key = -1; (*parent)->data_error.key = -1;
		(*parent)->key_cnt = 1; (*parent)->level = level;

		return 1;
	}

	else if ((*parent)->data[0].key == key || (*parent)->data[1].key == key)	//삽입할 key가 tree에 있으면,key가 있다고 출력하고 삽입하지 않음
	{
		return 0;
	}

	else if ((*parent)->sub[0] == NULL && (*parent)->sub[1] == NULL && (*parent)->sub[2] == NULL) //새로운 키가 삽입될 리프노드 탐색함
	{
		if ((*parent)->key_cnt == 0)											//새로운 키를 삽입 후에 노드의 키 개수가 3개 보다 적으면 종료
		{
			(*parent)->data[0].key = key;
			(*parent)->key_cnt += 1;
		}

		else if ((*parent)->key_cnt == 1)											
		{
			if ((*parent)->data[0].key > key)									
			{
				(*parent)->data[1].key = (*parent)->data[0].key;
				(*parent)->data[0].key = key;
			}

			else
				(*parent)->data[1].key = key;

			(*parent)->key_cnt += 1;

		}

		else if ((*parent)->key_cnt == 2)										//삽입의 결과 노드가 3개의 키를 가지게 되면 노드를 분할
		{
			if ((*parent)->data[0].key > key)
			{
				(*parent)->data_error.key = (*parent)->data[0].key;
				(*parent)->data[0].key = key;
			}

			else if ((*parent)->data[1].key > key)
			{
				(*parent)->data_error.key = key;
			}

			else if ((*parent)->data[1].key < key)
			{
				(*parent)->data_error.key = (*parent)->data[1].key;
				(*parent)->data[1].key = key;
			}

			(*parent)->key_cnt += 1;
			*unbalanced = 1;
		}

		return 1;
	}

	else if (key < (*parent)->data[0].key)												
	{
		tmp = t23Insert(&(*parent)->sub[0], key,++level, unbalanced);	//E1보다 작을경우 subtree A0
		if (*unbalanced)
			div_t23(parent, 0, unbalanced);
			
		return tmp;
	}
	else if ((*parent)->data[1].key == -1 || key < (*parent)->data[1].key)
	{
		tmp = t23Insert(&(*parent)->sub[1], key, ++level, unbalanced);	//E2보다 작을경우 subtree A1
		if (*unbalanced)	
			div_t23(parent, 1, unbalanced);
			
		return tmp;
	}

	else if (key > (*parent)->data[1].key)
	{
		tmp = t23Insert(&(*parent)->sub[2], key,++level, unbalanced);	//E2보다 클경우 subtree A2
		if (*unbalanced)	
			div_t23(parent, 2, unbalanced);
			
		return tmp;
	}

}

void div_t23(tree_23* parent, int sub, int* unbalanced)
{
	int data_error = (*parent)->sub[sub]->data_error.key;
	(*parent)->sub[sub]->data_error.key = -1;

	if ((*parent)->key_cnt == 0)
	{
		(*parent)->data[0].key = data_error;
		*unbalanced = 0;
	}

	else if ((*parent)->key_cnt == 1)
	{
		if ((*parent)->data[0].key > data_error)			//A0이 분할되는 경우
		{
			(*parent)->data[1].key = (*parent)->data[0].key;
			(*parent)->data[0].key = data_error;

			(*parent)->sub[2] = (*parent)->sub[1];			//subtree들도 맞춰 움직여준다
			(*parent)->sub[1] = NULL;
		}

		else												//A1이 분할되는 경우
			(*parent)->data[1].key = data_error;


		*unbalanced = 0;

		
	}

	else if ((*parent)->key_cnt == 2)
	{
		if ((*parent)->data[0].key > data_error)			//A0이 분할되는 경우
		{
			(*parent)->data_error.key = (*parent)->data[0].key;
			(*parent)->data[0].key = data_error;

			(*parent)->sub[3] = (*parent)->sub[2];			//subtree들도 맞춰 움직여준다
			(*parent)->sub[2] = (*parent)->sub[1];
			(*parent)->sub[1] = NULL;
		}

		else if ((*parent)->data[1].key > data_error)		//A1이 분할되는 경우
		{
			(*parent)->data_error.key = data_error;

			(*parent)->sub[3] = (*parent)->sub[2];			//subtree들도 맞춰 움직여준다
			(*parent)->sub[2] = NULL;

		}

		else if ((*parent)->data[1].key < data_error)		//A2이 분할되는 경우
		{
			(*parent)->data_error.key = (*parent)->data[1].key;
			(*parent)->data[1].key = data_error;
		}

		*unbalanced = 1;


	}
	if ((*parent)->sub[sub + 1] == NULL)
	{
		tree_23 temp = (tree_23)malloc(sizeof(struct M_tree));
		temp->sub[0] = temp->sub[1] = temp->sub[2] = temp->sub[3] = NULL;
		temp->level = (*parent)->sub[sub]->level;
		(*parent)->sub[sub + 1] = temp;
	}
	

	(*parent)->sub[sub + 1]->data[0].key = (*parent)->sub[sub]->data[1].key;					//노드 분할
	(*parent)->sub[sub + 1]->data[1].key = -1;  (*parent)->sub[sub + 1]->data_error.key = -1;
	(*parent)->sub[sub + 1]->key_cnt = 1;

	(*parent)->sub[sub]->data[1].key = -1; (*parent)->sub[sub]->data_error.key = -1;
	(*parent)->sub[sub]->key_cnt = 1;
	
	if ((*parent)->sub[sub]->sub[3] != NULL)													//이전에 sub에서 분할된적이 있는경우																	
	{																							//subtree의 subtree들도 분배
		(*parent)->sub[sub + 1]->sub[0] = (*parent)->sub[sub]->sub[2];
		(*parent)->sub[sub + 1]->sub[1] = (*parent)->sub[sub]->sub[3];
		(*parent)->sub[sub]->sub[2] = (*parent)->sub[sub]->sub[3] = NULL;
	}

	else
	{
		(*parent)->sub[sub + 1]->sub[0] = (*parent)->sub[sub]->sub[1];
		(*parent)->sub[sub + 1]->sub[1] = (*parent)->sub[sub]->sub[2];
		(*parent)->sub[sub]->sub[1] = (*parent)->sub[sub]->sub[2] = NULL;
	}

	(*parent)->key_cnt += 1;

}

int t23remove(tree_23* parent, int key, int* unbalanced)
{
	if (!*parent)												//삭제할 key가 없으면 종료
	{
		return 0;
	}

	else if ((*parent)->data[0].key == key || (*parent)->data[1].key == key)	//삭제할 key를 발견함
	{
		if ((*parent)->data[0].key == key) tmp = 1;
		else if ((*parent)->data[1].key == key) tmp = 2;

		if ((*parent)->sub[0] == NULL && (*parent)->sub[1] == NULL && (*parent)->sub[2] == NULL) //리프노드에 있으면, 리프노드에서 삭제
		{
			if ((*parent)->level == 1)															//루트 노드일 경우
			{
				if ((*parent)->data[0].key == key)
				{
					(*parent)->data[0].key = (*parent)->data[1].key;
					(*parent)->data[1].key = -1;
				}
				else if ((*parent)->data[1].key == key) (*parent)->data[1].key = -1;
				(*parent)->key_cnt--;
			}

			else																				//루트가 아닌 경우
			{
				if ((*parent)->data[0].key == key)
				{
					(*parent)->data[0].key = (*parent)->data[1].key;
					(*parent)->data[1].key = -1;
				}
				else if ((*parent)->data[1].key == key) (*parent)->data[1].key = -1;

				(*parent)->key_cnt--;

				//p가 적어도  1개의 원소를 가지고 있으면 종료
				if ((*parent)->key_cnt >= 1) return 1;

				else if ((*parent)->key_cnt == 0)
				{
					//p가  0개, 인접한 형제 노드 q가 최소 2 개의 원소를 가진 경우, 회전수행
					//p가  0개, 인접한 형제 노드 q가 1 개의 원소를 가진 경우, 결합수행	
					*unbalanced = 1;
					return 1;
				}
				
			}
		}

		else																					//리프노드가 아닐때,
		{
			//왼쪽 노드의 키의 개수와 오른쪽 노드의 키의 개수비교

			tree_23 temp;

			if ((*parent)->sub[tmp - 1]->key_cnt <= (*parent)->sub[tmp]->key_cnt)	//오른쪽 서브트리의 가장 작은 키로 대체
			{
				temp = (*parent)->sub[tmp];

				while(temp->sub[0])
				{
					temp = temp->sub[0];
				}
				(*parent)->data[tmp - 1].key = temp->data[0].key;

				t23remove(&((*parent)->sub[tmp]), (*parent)->data[tmp - 1].key, unbalanced);
			}

			else																	//왼쪽 서브트리의 가장 큰 키로 대체
			{
				temp = (*parent)->sub[tmp-1];

				while (1)
				{
					if (temp->sub[2])
					{
						temp = temp->sub[2];
						continue;
					}

					else if (temp->data[1].key != -1)
					{
						(*parent)->data[tmp - 1].key = temp->data[1].key;
						break;
					}

					else if (temp->sub[1])
					{
						temp = temp->sub[1];
						continue;
					}

					else
					{
						(*parent)->data[tmp - 1].key = temp->data[0].key;
						break;
					}
				}

				t23remove(&((*parent)->sub[tmp-1]), (*parent)->data[tmp - 1].key, unbalanced);
			}

		}

		return 1;
	}


	else if (key < (*parent)->data[0].key)
	{
		tmp = t23remove(&(*parent)->sub[0], key, unbalanced);	//E1보다 작을경우 subtree A0
		if (*unbalanced)
		{
			//p가  0개, 인접한 형제 노드 q가 최소 2 개의 원소를 가진 경우, 회전수행
			if ((*parent)->sub[1]->key_cnt == 2)
				rot_t23(parent, 0,1, unbalanced);

			//p가  0개, 인접한 형제 노드 q가 1 개의 원소를 가진 경우, 결합수행
			else if ((*parent)->sub[1]->key_cnt == 1)
				com_t23(parent, 0, 1,unbalanced);
		}

		return tmp;
	}
	else if ((*parent)->data[1].key == -1 || key < (*parent)->data[1].key)
	{
		tmp = t23remove(&(*parent)->sub[1], key, unbalanced);	//E2보다 작을경우 subtree A1
		if (*unbalanced)
		{
			//p가  0개, 인접한 형제 노드 q가 최소 2 개의 원소를 가진 경우, 회전수행
			if ((*parent)->sub[0]->key_cnt == 2 )
				rot_t23(parent, 1,0, unbalanced);
			else if ((*parent)->sub[2]->key_cnt == 2)
				rot_t23(parent, 1, 2, unbalanced);

			//p가  0개, 인접한 형제 노드 q가 1 개의 원소를 가진 경우, 결합수행
			else if ((*parent)->sub[0]->key_cnt == 1)
				com_t23(parent, 1, 0,unbalanced);
			else if ((*parent)->sub[2]->key_cnt == 1)
				com_t23(parent, 1, 2, unbalanced);
		}

		return tmp;
	}

	else if (key > (*parent)->data[1].key)
	{
		tmp = t23remove(&(*parent)->sub[2], key, unbalanced);	//E2보다 클경우 subtree A2
		if (*unbalanced)
		{
			//p가  0개, 인접한 형제 노드 q가 최소 2 개의 원소를 가진 경우, 회전수행
			if ((*parent)->sub[1]->key_cnt == 2)
				rot_t23(parent, 2,1, unbalanced);

			//p가  0개, 인접한 형제 노드 q가 1 개의 원소를 가진 경우, 결합수행
			else if ((*parent)->sub[1]->key_cnt == 1)
				com_t23(parent, 2,1, unbalanced);
		}

		return tmp;
	}

}

void rot_t23(tree_23* parent, int p,int q, int* unbalanced)			//각 p와 q에 대하여 데이터이동은 달라진다.
{
	if (p == 0)	
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[0].key;
		(*parent)->data[0].key = (*parent)->sub[q]->data[0].key;
		(*parent)->sub[q]->data[0].key = (*parent)->sub[q]->data[1].key;
		(*parent)->sub[q]->data[1].key = -1;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[0];
		(*parent)->sub[q]->sub[0] = (*parent)->sub[q]->sub[1];
		(*parent)->sub[q]->sub[1] = (*parent)->sub[q]->sub[2];
		(*parent)->sub[q]->sub[2] = NULL;
	}

	else if (p == 1 && q==0)
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[0].key;
		(*parent)->data[0].key = (*parent)->sub[q]->data[1].key;
		(*parent)->sub[q]->data[1].key = -1;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[p]->sub[0];
		(*parent)->sub[p]->sub[0] = (*parent)->sub[q]->sub[2];
		(*parent)->sub[q]->sub[2] = NULL;
	}

	else if (p == 1 && q == 2)
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[1].key;
		(*parent)->data[1].key = (*parent)->sub[q]->data[0].key;
		(*parent)->sub[q]->data[0].key = (*parent)->sub[q]->data[1].key;
		(*parent)->sub[q]->data[1].key = -1;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[0];
		(*parent)->sub[q]->sub[0] = (*parent)->sub[q]->sub[1];
		(*parent)->sub[q]->sub[1] = (*parent)->sub[q]->sub[2];
		(*parent)->sub[q]->sub[2] = NULL;
	}

	else if (p == 2)
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[1].key;
		(*parent)->data[1].key = (*parent)->sub[q]->data[1].key;
		(*parent)->sub[q]->data[1].key = -1;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[p]->sub[0];
		(*parent)->sub[p]->sub[0] = (*parent)->sub[q]->sub[2];
		(*parent)->sub[q]->sub[2] = NULL;
	}

	(*parent)->sub[p]->key_cnt += 1;
	(*parent)->sub[q]->key_cnt -= 1;
	*unbalanced = 0;
}
void com_t23(tree_23* parent, int p,int q, int* unbalanced)			 //각 p와 q에 대하여 데이터이동은 달라진다.
{
	if (p == 0)
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[0].key;
		(*parent)->data[0].key = (*parent)->data[1].key;
		(*parent)->data[1].key = -1;
		(*parent)->sub[p]->data[1].key = (*parent)->sub[q]->data[0].key;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[0];
		(*parent)->sub[p]->sub[2] = (*parent)->sub[q]->sub[1];

		(*parent)->sub[q] = (*parent)->sub[q + 1];
		(*parent)->sub[q + 1] = NULL;

	}

	else if (p == 1 && q == 0)
	{
		(*parent)->sub[p]->data[1].key = (*parent)->data[0].key;
		(*parent)->data[0].key = (*parent)->data[1].key;
		(*parent)->data[1].key = -1;
		(*parent)->sub[p]->data[0].key = (*parent)->sub[q]->data[0].key;

		(*parent)->sub[p]->sub[2] = (*parent)->sub[p]->sub[0];
		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[1];
		(*parent)->sub[p]->sub[0] = (*parent)->sub[q]->sub[0];

		(*parent)->sub[q] = (*parent)->sub[p];
		(*parent)->sub[p] = (*parent)->sub[p + 1];
		(*parent)->sub[p + 1] = NULL;

	}

	else if (p == 1 && q == 2)
	{
		(*parent)->sub[p]->data[0].key = (*parent)->data[1].key;
		(*parent)->data[1].key = -1;
		(*parent)->sub[p]->data[1].key = (*parent)->sub[q]->data[0].key;

		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[0];
		(*parent)->sub[p]->sub[2] = (*parent)->sub[q]->sub[1];

		(*parent)->sub[q] = NULL;

	}

	else if (p == 2)
	{
		(*parent)->sub[p]->data[1].key = (*parent)->data[1].key;
		(*parent)->data[1].key = -1;
		(*parent)->sub[p]->data[0].key = (*parent)->sub[q]->data[0].key;

		(*parent)->sub[p]->sub[2] = (*parent)->sub[p]->sub[0];
		(*parent)->sub[p]->sub[1] = (*parent)->sub[q]->sub[1];
		(*parent)->sub[p]->sub[0] = (*parent)->sub[q]->sub[0];

		(*parent)->sub[q] = (*parent)->sub[p];
		(*parent)->sub[p] = NULL;

	}

	(*parent)->sub[p]->key_cnt = 2;
	(*parent)->key_cnt -= 1;

	if((*parent)->key_cnt > 0)
		*unbalanced = 0;
}

void print_t23(tree_23* root,int cnt, int  n, FILE* fp)
{
	fprintf(stdout, "tree %d\n", n);

	tree_23* temp;
	Q* q = (Q*)malloc(sizeof(Q) * cnt);
	int front=-1,rear=-1,i;
						
	q[++front] = add_q(root);											//queue에 root 삽입

	while (front != rear)
	{
		root = q[++rear].node;											//queue에서 node를 삭제

		if (*root)
		{

			if ((*root)->sub[0])										//queue에 subtree 삽입
			{
				(*root)->sub[0]->level = (*root)->level + 1;
				q[++front] = add_q(&((*root)->sub[0]));
			}

			if ((*root)->sub[1])
			{
				(*root)->sub[1]->level = (*root)->level + 1;
				q[++front] = add_q(&((*root)->sub[1]));
			}

			if ((*root)->sub[2])
			{
				(*root)->sub[2]->level = (*root)->level + 1;
				q[++front] = add_q(&((*root)->sub[2]));
			}

			fprintf(stdout,"( ");										//노드 key출력
			for (i = 0; i < 2; i++)
			{
				if ((*root)->data[i].key != -1)
					fprintf(stdout,"%d ", (*root)->data[i].key);
				if (i != 1 && (*root)->data[1].key != -1)
					fprintf(stdout,",");
			}
			fprintf(stdout,") ");
			
			if (rear != front)
			{
				temp = q[rear + 1].node;
				if ((*root)->level != (*temp)->level)						//현재 level값의 마지막node일 떄, 다음줄
					fprintf(stdout, "\n");
			}

		}

	}

	fprintf(stdout, "\n\n");

}

Q add_q(tree_23* data)
{
	Q temp;
	temp.node = data;

	return temp;
}