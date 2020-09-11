//2017114915 김민수

#define _CRT_SECURE_NO_WARNINGS			// fopen,scanf 보안 경고로 인한 컴파일 에러 방지..
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int* cnt, *num;						//num은 입력된 숫자들의 배열, cnt는 num의 원소들이 입력된 횟수의 배열
	int input_num =0, dif_num=0;		//input_num은 입력될 숫자들의 개수, dif_num는 서로다른숫자의 개수(num,cnt의 원소의 개수)
	int temp, i,j,k;
	char f_name[100];
	FILE* fp;

	printf("파일 이름을 입력하시오 : ");
	scanf("%s",f_name);								//읽어올 파일이름입력

	fp = fopen(f_name,"r");				
	if (fp == NULL)									//파일열기 실패시 error
	{
		printf("error : 해당파일열기를 실패하였습니다.\n");
		return 0;
	}

	fscanf(fp, "%d", &input_num);					//파일의 첫번째 숫자를 input_num에 할당
	if (input_num <= 0)								//input_num이 양수가 아닐 시 error
	{
		printf("error : 입력될 숫자들의 개수가 음수입니다.\n");
		return 0;
	}

	cnt = (int*)calloc(input_num,sizeof(int));		//cnt와 num을 최대 input_num개의 int data를 저장하도록 동적할당
	num = (int*)malloc(sizeof(int) * input_num);	//cnt는 0으로 초기화

	for(i=0; i<input_num; i++)						//파일에서 숫자를 input_num만큼 입력받음
	{
		fscanf(fp,"%d",&temp);

		for (j = 0; j < dif_num; j++)				//입력받은 숫자가 num배열안에 중복되는 숫자가 있는지 확인
		{
			if (temp == num[j])						//num배열안에 이미 있는 숫자라면, cnt의 해당 index의 값에 1추가
			{
				cnt[j]++;
				break;
			}
		}
		if (j == dif_num)							//num배열안에 없었다면, 중복되는 수가 아니므로 num에 추가
		{
			num[dif_num] = temp;
			cnt[dif_num]++;
			dif_num++;
		}


	}

	for (i = 0; i < dif_num; i++)					//각 숫자가 몇번 입력되었는지 출력
	{
		if (i != 0)
			printf(", ");

		printf("%d :%d번", num[i], cnt[i]);
	}
	printf("\n");

	return 0;
}