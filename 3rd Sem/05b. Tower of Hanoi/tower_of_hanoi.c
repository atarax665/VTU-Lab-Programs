// Solve Tower of Hanoi problem for n disks.
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void tower(int n,int source,int temp,int dest)
{
	if(n==0)
	return;
	tower(n-1,source,dest,temp);
	printf("\nMove disk %d from %c to %c\n",n,source,dest);
	tower(n-1,temp,source,dest);
}

void main()
{
	int n;
	printf("Enter the number of disks:\n");
	scanf("%d",&n);
	tower(n,'A','B','C');
	printf("\nThe total number of moves are:\n%d\n",(int)pow(2,n)-1);
}
