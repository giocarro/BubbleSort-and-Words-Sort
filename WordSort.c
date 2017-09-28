#include<stdio.h>
#include<string.h>

#define N 10000

void BubbleSort(char A[][256])
{
	char C[256]={0};
	int i,j,k,l=0,m=0;
	
		for(i=0;i<N-1;i++)	
		{
			for(j=0;j<N-1;j++)
			{
				k=strcmp(A[j],A[j+1]);
				if(k>0)
				{
					l++;
					strcpy(C,A[j]); //copio A[j] a C
					memset(A[j],0,256); //borro A[j]
					strcpy(A[j],A[j+1]);  //copio A[j+1] a A[j]
					memset(A[j+1],0,256); // borro A[j+1]
					strcpy(A[j+1],C); //copio C a A[j+1]
					memset(C,0,256); //borro C
				}
			m++;
			}
		m++;
		}

	for(i=0;i<N;i++)
	{
		printf("%s\n",A[i]);
	}
	printf("\nInside if=%d\nIterations=%d\n",l,m);
}

int main()
{	
	char arr[N][256]={0};
	int i=0;
	int v=0;
	char str[256];
	FILE *f=fopen("words.txt","r");
	
	if(!f)
	{
		perror("Error al abrir el archivo");
		return -1;
	}
	//Read File
	i=0;
	while(fgets(str,256,f))
	{
		strcpy(arr[i],str);
		//printf("%s",arr[i]);
		i++;
	}
	fclose(f);
	
	//BubbleSort((char**) arr);
	BubbleSort(arr);
}
