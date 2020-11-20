//2017114915 김민수.
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS												// fopen,scanf 보안 경고로 인한 컴파일 에러 방지

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define SWAP(a,b,temp) {temp=a; a=b; b=temp;}
int INF = 987654321;

typedef struct input* ip;
struct input								//입력파일에서 입력되는 key
{
	int key;
	ip next;
};

typedef struct								//tree node의 데이터
{
	int key;
}element;

typedef struct B_tree* AVL;					//tree node
struct B_tree
{
	element data;
	AVL leftChild;
	AVL rightChild;
	int level;
	int bf;
};
		
void avlInsert(AVL* ,int, int*);			//AVL tree에 삽입
void leftRotation(AVL*, int*);
void rightRotation(AVL*, int*);
void avlremove(AVL* ,AVL*, int,int*);		//AVl tree에서 특정 key제거
void print_avl(AVL,int,FILE*);				//AVL tree의 inorder 순서와 preorder 순서를 출력
void inorder(AVL, FILE*);
void preorder(AVL, FILE*);

int main(int argc, char* argv[])
{
	FILE* fp1, *fp2;
	int input_temp;						
	ip input = (ip)malloc(sizeof(struct input));
	ip root_ip = (ip)malloc(sizeof(struct input));
	root_ip->next = NULL;


	if (argc != 3)																		//입력파일명 및 출력파일명이 주어지지않으면 에러
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
		input->next = temp;
		input = input->next;
	}

	fclose(fp1);

	//key를 순서대로 삽입하여 AVL tree 생성
	AVL root = NULL;
	int is_unbalanced = 0,n=0;

	input = root_ip->next;
	while(input != NULL)
	{
		avlInsert(&root, input->key, &is_unbalanced);

		//key를 하나씩 삽입할 때마다 AVL tree 출력
		print_avl(root, ++n,fp2);

		input = input->next;
	}

	//모두 삽입 후에 첫번째 key 삭제
	avlremove(&root,NULL, root_ip->next->key, &is_unbalanced);

	//마지막에 첫번째 key를 삭제 후에 출력
	print_avl(root, ++n,fp2);

	free(root);
	fclose(fp2); free(input); free(root_ip);
	return 0;
}

void avlInsert(AVL* parent, int key, int* unbalanced)
{	
	if (!*parent)												//빈 subtree에 삽입
	{							
		AVL temp = (AVL)malloc(sizeof(struct B_tree));
		*parent = temp;
		(*parent)->leftChild = (*parent)->rightChild = NULL;
		(*parent)->bf = 0; (*parent)->data.key = key;

		*unbalanced = 1;
	}
	else if (key < (*parent)->data.key) 
	{
		avlInsert(&(*parent)->leftChild, key, unbalanced);
		if (*unbalanced)										//왼쪽 서브트리에 추가될 경우, bf체크 및 균형유지
			switch ((*parent)->bf) 
			{
				case -1: (*parent)->bf = 0;
					*unbalanced = 0; break;
				case 0: (*parent)->bf = 1; break;
				case 1: leftRotation(parent, unbalanced);
			}
	}
	else if (key > (*parent)->data.key)
	{
		avlInsert(&(*parent)->rightChild, key, unbalanced);
		if (*unbalanced)										//오른쪽 서브트리에 추가될 경우, bf체크 및 균형유지
			switch ((*parent)->bf) 
			{
				case 1: (*parent)->bf = 0;
						*unbalanced = 0; break;
				case 0: (*parent)->bf = -1; break;
				case -1: rightRotation(parent, unbalanced);
			}
	}
	else														//key가 이미 있을때, 아무것도 하지 않는다.	
	{
		*unbalanced = 0;									
	}
}

void leftRotation(AVL* parent, int* unbalanced)
{
	AVL grandChild, child;
	child = (*parent)->leftChild;

	if (child->bf == 1)				//LL rotation 경우
	{
		
		(*parent)->leftChild = child->rightChild;
		child->rightChild = *parent;
		(*parent)->bf = 0;
		(*parent) = child;
	}
	else							//LR rotation 경우
	{
		
		grandChild = child->rightChild;
		child->rightChild = grandChild->leftChild;
		grandChild->leftChild = child;
		(*parent)->leftChild = grandChild->rightChild;
		grandChild->rightChild = *parent;

		switch (grandChild->bf) 
		{
			case 1: (*parent)->bf = -1; child->bf = 0;
				break;
			case 0: (*parent)->bf = child->bf = 0;
				break;
			case -1: (*parent)->bf = 0;
				child->bf = 1;
		}
		*parent = grandChild;
	}
	(*parent)->bf = 0;
	*unbalanced = 0;
}

void rightRotation(AVL* parent, int* unbalanced)
{
	AVL grandChild, child;
	child = (*parent)->rightChild;

	if (child->bf == -1)				// RR rotation 경우
	{

		(*parent)->rightChild = child->leftChild;
		child->leftChild = *parent;
		(*parent)->bf = 0;
		(*parent) = child;
	}
	else								//RL rotation 경우
	{

		grandChild = child->leftChild;
		child->leftChild = grandChild->rightChild;
		grandChild->rightChild = child;
		(*parent)->rightChild = grandChild->leftChild;
		grandChild->leftChild = *parent;

		switch (grandChild->bf) 
		{
			case 1: (*parent)->bf = 0; child->bf = -1;
				break;
			case 0: (*parent)->bf = child->bf = 0;
				break;
			case -1: (*parent)->bf = 1;
				child->bf = 0;
		}
		*parent = grandChild;
	}
	(*parent)->bf = 0;
	*unbalanced = 0;
}

void avlremove(AVL* parent, AVL *pre, int key, int* unbalanced)
{
	if ((*parent)->data.key == key)								//key를 찾았을 때,
	{
		//leaf노드 일 경우,부모의 자식 필드에 NULL을 삽입. 삭제된 노드를 해제한다.
		if ((*parent)->leftChild == NULL && (*parent)->rightChild == NULL)
		{
			if (pre == NULL)									//루트노드가 삭제대상일 때,
			{
				*parent = NULL;
				return;
			}

			if ((*pre)->leftChild == *parent) (*pre)->leftChild = NULL;
			else (*pre)->rightChild = NULL;

			*unbalanced = 1;
		}

		//자식이 두개있는 nonleaf노드 일 경우, 오른쪽 서브트리의 가장 작은 노드로 대체한다.
		else if ((*parent)->leftChild != NULL && (*parent)->rightChild != NULL)
		{
			AVL change_pre = (*parent),change= (*parent)->rightChild;

			while (change->leftChild != NULL)
			{
				change_pre = change;
				change = change->leftChild;
			}

			(*parent)->data.key = change->data.key;

			//오른쪽 서브트리의 가장 작은 노드로 대체하고, 기존의 대체된 노드는 삭제
			avlremove(&(*parent)->rightChild, &change_pre, change->data.key, unbalanced);			
		}

		//자식이 한개있는 nonleaf노드 일 경우,삭제된 노드의 자식을 삭제된 노드의 자리에 위치시킨다.
		else
		{
			if (pre == NULL)									//루트노드가 삭제대상일 때,
			{
				*parent = ((*parent)->leftChild != NULL) ? (*parent)->leftChild : (*parent)->rightChild;
				return;
			}

			if ((*pre)->leftChild == *parent)
				(*pre)->leftChild = ((*parent)->leftChild != NULL) ? (*parent)->leftChild : (*parent)->rightChild;
			else
				(*pre)->rightChild = ((*parent)->leftChild != NULL) ? (*parent)->leftChild : (*parent)->rightChild;

			*unbalanced = 1;
		}
	}
	else if (key < (*parent)->data.key)
	{
		avlremove(&(*parent)->leftChild, parent,key, unbalanced);
		if (*unbalanced)										//왼쪽 서브트리에 있는 key가 제거될 경우, bf체크 및 균형유지
			switch ((*parent)->bf)
			{
				case 1: (*parent)->bf = 0;
					*unbalanced = 0; break;
				case 0: (*parent)->bf = -1; break;
				case -1: rightRotation(parent, unbalanced);		//왼쪽이 제거되었으니, rightrotation 경우
			}
	}
	else if (key > (*parent)->data.key)
	{
		avlremove(&(*parent)->rightChild,parent, key, unbalanced);
		if (*unbalanced)										//오른쪽 서브트리에 있는 key가 제거될 경우, bf체크 및 균형유지
			switch ((*parent)->bf)
			{
				case -1: (*parent)->bf = 0;
					*unbalanced = 0; break;
				case 0: (*parent)->bf = 1; break;
				case 1: leftRotation(parent, unbalanced);		//오른쪽이 제거되었으니, leftrotation 경우
			}
	}
}

void print_avl(AVL root,int n, FILE* fp)
{
	fprintf(fp,"tree %d\n",n);

	//inorder 순서로 출력

	fprintf(fp,"inorder :");
	inorder(root,fp);
	fprintf(fp,"\n");

	//preorder 순서로 출력

	fprintf(fp,"preorder :");
	if (root != NULL)
	preorder(root,fp);
	fprintf(fp,"\n\n");
}

void inorder(AVL tree, FILE* fp)
{
	if (tree != NULL)
	{
		inorder(tree->leftChild,fp);
		fprintf(fp," %d",tree->data.key);
		inorder(tree->rightChild,fp);
	}
}

void preorder(AVL tree, FILE* fp)
{
	if (tree != NULL)
	{
		fprintf(fp," %d", tree->data.key);
		preorder(tree->leftChild,fp);
		preorder(tree->rightChild,fp);
	}
}
