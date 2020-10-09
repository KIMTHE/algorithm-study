//2017114915 김민수

#define _CRT_SECURE_NO_WARNINGS							// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct element									//노드의 데이터와 레벨
{
	char data;
	int level;
}element;

struct node												//이진트리 노드
{
	element element;
	struct node* l_link;
	struct node* r_link;
	struct node* parent;
};

void stack_push(char*, int*, int, char);
char stack_pop(char*, int*);
void add_bt(struct node*, char, int);
void add_q(int, int*, struct node*, struct node**);
struct node* delete_q(int*, int, struct node**);


int main(int argc, char* argv[])
{
	FILE* fp;
	int infix_id = -1, postfix_id = -1, i;
	char temp, infix[100], postfix[100];



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


	while (1)															//infix 수식 입력받음
	{
		temp = fgetc(fp);
		if (temp == EOF)
			break;

		if (temp != ' ')												//띄어쓰기는 없앰
			infix[++infix_id] = temp;

	}
	infix[infix_id + 1] = '\0';

	//중위표기수식 -> 후위표기수식 시작

	char* stack = (char*)malloc(sizeof(char) * infix_id);
	int top = -1, MAX_stack = infix_id;									//stack의 최대크기는 전위표기수식의 길이만큼이다.

	for (i = 0; i <= infix_id; i++)
	{
		if ('a' <= infix[i] && infix[i] <= 'z')							//피연산자는 바로 후위표기수식에 출력
		{
			postfix[++postfix_id] = infix[i];
		}

		else if (infix[i] == '+' || infix[i] == '-' || infix[i] == '*' || infix[i] == '/')		//연산자 일 때,
		{
			if (top == -1)
				stack_push(stack, &top, MAX_stack, infix[i]);

			else if (infix[i] == '+' || infix[i] == '-')				//+,- 는 +,-,*,/ 들을 pop하고 자신을 push
			{
				while (1)
				{
					if (stack[top] == '+' || stack[top] == '-' || stack[top] == '*' || stack[top] == '/')
						postfix[++postfix_id] = stack_pop(stack, &top);
					else
						break;
				}

				stack_push(stack, &top, MAX_stack, infix[i]);

			}

			else if (infix[i] == '*' || infix[i] == '/')				//*,/ 는 *,/ 들만 pop하고 자신을 push
			{
				while (1)
				{
					if (stack[top] == '*' || stack[top] == '/')
						postfix[++postfix_id] = stack_pop(stack, &top);
					else
						break;
				}

				stack_push(stack, &top, MAX_stack, infix[i]);
			}
		}

		else if (infix[i] == '(')										// ( 는 push
		{
			stack_push(stack, &top, MAX_stack, infix[i]);
		}

		else if (infix[i] == ')')										// ) 는 (가 나올떄까지 pop
		{
			while (1)
			{
				temp = stack_pop(stack, &top);

				if (temp != '(' && temp != ')')
					postfix[++postfix_id] = temp;

				else if (temp == '(')
					break;
			}
		}
	}

	while (top >= 0)													//stack에 남은 연산자들 후위표기수식에 출력
	{
		postfix[++postfix_id] = stack_pop(stack, &top);
	}

	//후위표기수식으로 이진트리 구성 시작

	int mk_bt_id = postfix_id;
	struct node* root = (struct node*)malloc(sizeof(struct node));
	struct node* parent = root;
	root->element.data = postfix[mk_bt_id--];							//후위표기수식의 마지막 연산자가 이진트리의 root
	root->l_link = NULL;	root->r_link = NULL;	root->parent = NULL;	root->element.level = 1;

	for (i = mk_bt_id; i >= 0; i--)
	{

		while (1)
		{
			if (parent->r_link == NULL)									//오른쪽 자식노드부터 채운다.
			{
				add_bt(parent, postfix[i], 2);

				if (postfix[i] == '+' || postfix[i] == '-' || postfix[i] == '*' || postfix[i] == '/')	//연산자가 나오면,
					parent = parent->r_link;															//그 노드를 root로 하는 subtree에서 진행한다.

				break;
			}

			else if (parent->l_link == NULL)							//오른쪽자식노드에 이미있으면 왼쪽자식노드에 채운다.
			{
				add_bt(parent, postfix[i], 1);

				if (postfix[i] == '+' || postfix[i] == '-' || postfix[i] == '*' || postfix[i] == '/')	//위와 동일
					parent = parent->l_link;

				break;
			}

			else
			{
				parent = parent->parent;								//자식노드가 꽉 찼으면, 현재 subtree의 root의 부모노드를
			}															//root로 하는 subtree에서 진행한다.

		}

	}

	//표기수식과 이진트리 출력

	struct node** queue_bt = (struct node**)malloc(sizeof(struct node*) * infix_id);
	struct node* temp_node = (struct node*)malloc(sizeof(struct node) * infix_id);
	int rear = -1, front = -1, print_level = 1;
	char c;

	printf("중위 표기(infix)수식 :");
	for (i = 0; i <= infix_id; i++)
		printf(" %c", infix[i]);

	printf("\n후위 표기(postfix)수식 :");
	for (i = 0; i <= postfix_id; i++)
		printf(" %c", postfix[i]);

	printf("\n이진트리 : \n");											//queue를 이용하여 레벨에 따라서 출력

	temp_node = root;
	add_q(front, &rear, temp_node, queue_bt);						//queue에 root노드 삽입

	while (1)
	{
		temp_node = delete_q(&front, rear, queue_bt);					//queue에서 node를 삭제

		if (temp_node)
		{

			if (temp_node->l_link)										//queue에 자식 nodes삽입
			{
				add_q(front, &rear, temp_node->l_link, queue_bt);
			}

			if (temp_node->r_link)										//queue에 자식 nodes삽입
			{
				add_q(front, &rear, temp_node->r_link, queue_bt);
			}

			if (temp_node->parent == NULL)								//root노드 출력
				printf("(Root, %c)", temp_node->element.data);

			else														//그 외 노드 출력
			{
				printf("(%c, %c, %c) ", temp_node->parent->element.data
					, (temp_node == temp_node->parent->l_link) ? 'L' : 'R', temp_node->element.data);
			}

			if (temp_node->element.level != queue_bt[front + 1]->element.level)		//현재 level값의 마지막node일 떄, 다음줄
				printf("\n");

			if (front == rear)											//queue의 마지막노드일 때, 끝
				break;
		}

	}

	return 0;
}

void stack_push(char* stack, int* top, int MAX_stack, char data)
{
	if (*top >= MAX_stack)
	{
		fprintf(stderr, "STACK IS FULL ERROR\n");
		exit(1);
	}

	stack[++(*top)] = data;
}

char stack_pop(char* stack, int* top)
{
	if (*top < 0)
	{
		fprintf(stderr, "STACK IS EMPTY ERROR\n");
		exit(1);
	}

	return stack[(*top)--];
}

void add_bt(struct node* parent, char data, int dir)	//dir값에 따라 왼쪽 또는 오른쪽 자식노드에 추가함.
{
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->element.data = data;
	temp->l_link = NULL;	temp->r_link = NULL;	temp->parent = parent;
	temp->element.level = parent->element.level + 1;

	if (dir == 1)
		parent->l_link = temp;
	else if (dir == 2)
		parent->r_link = temp;
}

struct node* delete_q(int* front, int rear, struct node** queue)
{
	(*front)++;										//empty 검사는 main함수 내에서 front==rear로 하는 중
	return queue[*front];

}

void add_q(int front, int* rear, struct node* temp, struct node** queue)
{
	(*rear)++;										//queue의 max size가 입력된 데이터의 개수로 설정했으므로, 이를 초과할수없음
	queue[*rear] = temp;
}

