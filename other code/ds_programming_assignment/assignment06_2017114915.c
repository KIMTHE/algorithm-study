//2017114915 김민수
//visual studio 2019

#define _CRT_SECURE_NO_WARNINGS												// fopen,scanf 보안 경고로 인한 컴파일 에러 방지.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

typedef struct bucket														//directory 구조체
{
	int address;
	char slot1[3];
	char slot2[3];
}bucket;
int depth;
int address_cnt = 0;

int get_mask(char*);
bucket* insert_key(bucket*, char*);											//포인터도 반환하도록 하자.
void print_D(bucket *);


int main(int argc, char* argv[])
{
	FILE* fp;
	int  i, key_cnt = 0;
	char input_key[100],list_key[100][3];


	if (argc != 2)															//입력파일이름이 주어지지않으면 에러
	{
		fprintf(stderr, "입력파일이름 입력이 잘못되었습니다.\n");
		exit(1);
	}

	fp = fopen(argv[1], "r");
	if (fp == NULL)															//파일열기 실패시 error
	{
		fprintf(stderr, "error : 해당파일열기를 실패하였습니다.\n");
		exit(1);
	}

	while (fscanf(fp, "%s", input_key) != EOF)								//key 입력받음
	{
		if (strlen(input_key) != 2)											//key가 두글자가 아니라면 에러
		{
			fprintf(stderr, "error : key입력이 잘못되었습니다.\n");
			exit(1);
		}

		strcpy(list_key[key_cnt++],input_key);
	}

	//directory 초기화

	depth = 1;
	bucket* D = (bucket*)calloc((int)pow(2, depth),sizeof(bucket) );		//directory 크기는 2부터 시작
	for (i = 0; i < (int)pow(2, depth); i++)								//주소는 0으로 초기화
	{
		D[i].address = 0;
	}

	//directory를 이용한 동적해싱, key삽입

	for (i = 0; i < key_cnt; i++)
	{
		D = insert_key(D, list_key[i]);

		print_D(D);
	}
	printf("\n");

	free(D);

	return 0;
}

int get_mask(char* key)														//문자열key를 bit mask로 변환
{
	int mask = 0x00;

	switch (key[1])															//2번째 문자에 따른 하위비트 3개
	{
	case 'A' :
		mask = mask | 0x00;
		break;
	case 'B':
		mask = mask | 0x01;
		break;
	case 'C':
		mask = mask | 0x02;
		break;
	case 'D':
		mask = mask | 0x03;
		break;
	case 'E':
		mask = mask | 0x04;
		break;
	case 'F':
		mask = mask | 0x05;
		break;
	case 'G':
		mask = mask | 0x06;
		break;
	case 'H':
		mask = mask | 0x07;
		break;
	default :
		fprintf(stderr,"error : 해당 key입력이 잘못되었습니다.\n");
		exit(1);
	}

	switch (key[0])															//1번째 문자에 따른 상위비트 3개
	{
	case 'A':
		mask = mask | 0x00;
		break;
	case 'B':
		mask = mask | 0x08;
		break;
	case 'C':
		mask = mask | 0x10;
		break;
	case 'D':
		mask = mask | 0x18;
		break;
	case 'E':
		mask = mask | 0x20;
		break;
	case 'F':
		mask = mask | 0x28;
		break;
	case 'G':
		mask = mask | 0x30;
		break;
	case 'H':
		mask = mask | 0x38;
		break;
	default:
		fprintf(stderr,"error : 해당 key입력이 잘못되었습니다.\n");
		exit(1);
	}

	mask = mask & (int)(pow(2, depth) - 1);									//변환된 비트를 LSB에서 depth만큼만 반환함
	return mask;
}

bucket* insert_key(bucket* D , char* key)										//key를 table에 삽입한다.
{
	int i, j, k;
	int key_mask, slot1_mask, slot2_mask;

	key_mask = get_mask(key);
	

	for (i = 0; i < (int)pow(2, depth); i++)
	{
		if (i == key_mask)													//table에서 key_mask비트와 같은곳을 찾는다.
		{
			if (D[i].slot1[0] == '\0')
			{
				strcpy(D[i].slot1, key);
				if(D[i].address == 0 )
					D[i].address = ++address_cnt;
				break;
			}

			else if (D[i].slot2[0] == '\0')
			{
				strcpy(D[i].slot2, key);
				if (D[i].address == 0)
					D[i].address = ++address_cnt;
				break;
			}

			else																//슬롯에 자리가 없다면, overflow
			{
				depth++;
				D = (bucket*)realloc(D, sizeof(bucket) * (int)pow(2, depth));	//table을 2배로 늘린다.

				k = 0;
				for (j = (int)pow(2, (depth - 1)); j < (int)pow(2, depth); j++)	//버킷주소를 추가된 뒷부분 그대로 복사한다. 
				{
					D[j].address = D[k++].address;
					D[j].slot1[0] = '\0';
					D[j].slot2[0] = '\0';
				}

				key_mask = get_mask(key);
				slot1_mask = get_mask(D[i].slot1);
				slot2_mask = get_mask(D[i].slot2);

				if (slot1_mask !=i)												//충돌이 일어나는 3개의 key를 다시 재삽입한다.
				{
					D= insert_key(D, D[i].slot1);
					D[i].slot1[0] = '\0';
				}

				if (slot2_mask != i)
				{
					D= insert_key(D, D[i].slot2);
					D[i].slot2[0] = '\0';
				}

				i--;
				continue;

				
			}
		}
	}

	return D;
}


void print_D(bucket* D)											//directory 출력, 버킷의 주소와 슬롯들을 출력한다.
{
	int i;

	printf("\nDirectory(%d) :",(int)pow(2,depth));

	for (i = 0; i < (int)pow(2, depth); i++)
	{
		if (D[i].address == 0)
			printf(" null");

		else
			printf(" %d",D[i].address);
	}
	printf("\n");

	for (i = 0; i < (int)pow(2, depth); i++)
	{
		if (D[i].address != 0 && (D[i].slot1[0] != '\0' || D[i].slot2[0] != '\0'))
		{
			printf("%d: ",D[i].address);

			if(D[i].slot1[0] != '\0')
				printf("%s ",D[i].slot1);

			if (D[i].slot2[0] != '\0')
				printf("%s ", D[i].slot2);
		}
	}
}