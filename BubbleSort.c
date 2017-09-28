/*10
5
-2
0
1
9
11
7
23

Bubble sort

20 numeros aleatorios entre Rand 0..99

*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 20

void bubbleSort(int a[N])
{
	int x=0;
	int i=0;
	int j=0;

	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(a[j]>a[j+1])
			{
				x=a[j];
				a[j]=a[j+1];
				a[j+1]=x;
			}
		}
	}

	for(i=0;i<N;i++)
	{
		if(i!=N-1)
		printf("%i, ",a[i]);
	}
	printf("%i.\n",a[i]);
}

int main()
{
	int arr[N]={0};
	int i=0;
	int v=0;	
	srand(time(NULL));

	for(i=0;i<N;i++)
	{
		v=rand()%10000-rand()%10;
		arr[i]=v;
		if(i!=N-1)
		{
			printf("%d, ",v);
		}
	}
	printf("%d.\n",v);
	bubbleSort(arr);
	return 0;
}
