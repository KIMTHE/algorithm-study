#include<stdio.h>
#define SIZE 20

struct student
{
	char name[SIZE];
	char number[SIZE]; //학점
	int grade[2];
	double grade_aver;
	int rank;
};

double average(int a, int b);

int main()
{
	struct student s[SIZE], temp;
	int i,j,k,n=0; //n=학생수
	int A, B, C, G;

	FILE* fp;

	fopen_s(&fp,"students.txt", "r");
	if (fp == NULL)
	{
		printf("파일이 제대로 열리지 않습니다.\n");
		return 0;
	}

	while (1)
	{
		printf("\n---------------------------\n");
		printf("무엇을 하시겠습니까?\n");
		printf("1. 학생성적 입력\n");
		printf("2. 학생성적 조회\n");
		printf("3. 장학생 조회\n");
		printf("0. 프로그램 종료\n");
		printf("입력 : ");

		scanf_s("%d",&i);

		if (i == 1)
		{
			printf("---------------------------\n");
			printf("학생의 인원수를 입력하시오.(최대 10명) : ");
			scanf_s("%d", &n);
			if (n > 10 || n <= 0) printf("학생수가 잘못입력되었습니다.\n");
			else 
			{
				for (j = 0; j<n; j++)
				{
					fscanf_s(fp, "%s %s %d %d",s[j].name,sizeof(s[j].name),s[j].number,sizeof(s[j].number)
						,&s[j].grade[0], &s[j].grade[1]);

					s[j].grade_aver = average(s[j].grade[0],s[j].grade[1]);
				}

				for (j = 0; j < n; j++) //내림차순 정렬
				{
					for (k = j + 1; k < n; k++)
					{
						if (s[j].grade_aver <= s[k].grade_aver)
						{
							temp = s[j];
							s[j] = s[k];
							s[k] = temp;
						}
					}
				}

				for (j = 0; j < n; j++) //공동등수를 고려한 등수매기기
				{
					if ( j!=0 && s[j].grade_aver == s[j - 1].grade_aver)
						s[j].rank = s[j - 1].rank;
					else
						s[j].rank = j + 1;
				}
			}
		}

		else if (i == 2) // 상위 30퍼 A ,다음 40퍼 B, 마지막 30퍼 C
		{
			if (n == 0) printf("학생성적이 입력되지 않았습니다.\n");

			else //내림차순으로 정렬되어있음
			{
				A = n * 0.3;
				B = n * 0.7;
				C = n;
				printf("---------------------------\n");

				for (j = 0; j < n; j++)
				{
					printf("%s %s ",s[j].name,s[j].number );

					if (s[j].rank <= A)
						printf("A\n");

					else if(s[j].rank <= B)
						printf("B\n");

					else
						printf("C\n");
				}
			}
			
		}

		else if (i == 3) // 상위 10퍼 장학생
		{
			if (n == 0) 
				printf("학생성적이 입력되지 않았습니다.\n");

			else if(n < 10) 
				printf("학생수가 적어 장학생을 선발하지 못합니다.\n");

			else //내림차순 정렬되어있음
			{
				G = n * 0.1;

				printf("---------------------------\n");
				for (j = 0; j < n; j++)
				{
					if (s[j].rank <= G)
						printf("%s %s 장학생\n", s[j].name, s[j].number);
				}
			}
		}

		else if (i == 0)
		{
			printf("---------------------------\n");
			printf("프로그램을 종료하겠습니다.\n");
			fclose(fp);
			return 0;
		}

		else
		{
			printf("---------------------------\n");
			printf("숫자를 잘못입력하셨습니다.\n");
		}
	}

	fclose(fp);
}

double average(int a, int b)
{
	double result;
	result = (a + b) / 2;

	return result;
}