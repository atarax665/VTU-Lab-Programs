#include<stdio.h>
int a[20],n,ele,i,pos;	

void create()			
//creating an array
{
printf("\nEnter the size of the array elements:\t");
scanf("%d",&n);
printf("\nEnter the elements for the array:\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
}

void display()							//display array elements
{
printf("\nThe array elements are: \n");
for(i=0;i<n;i++)
printf("%d \t",a[i]);
}

void insert_ele()				//inserting an element at specified position
{
printf("\nEnter the position for the new element:\t");
scanf("%d",&pos);

printf("\nEnter the element to be inserted :\t");
scanf("%d",&ele);


if(pos> (n+1)||pos<=0)
{
printf("invalid position\n");
return;
}

for(i=n-1; i>=pos-1; i--)
a[i+1]=a[i];
a[pos-1]=ele;
n++;
}

void delete_ele()			//deleting an array element
{
printf("\nEnter the position of the element to be deleted:\t");
scanf("%d",&pos);
if(pos>=n+1||pos<=0)
{
printf("invalid position\n");
return;
}
printf("element deleted is %d", a[pos-1]);
for(i=pos-1; i<n-1; i++)
a[i]=a[i+1];
n--;
}

void main()
{
int ch;
do
{
printf(" \n -------- MENU -----------  \n");
printf("1:CREATE	  2:DISPLAY     3:INSERT    4:DELETE\n");
printf("-----------------------");

printf("\nENTER YOUR CHOICE:\t");
scanf("%d",&ch);
switch(ch)
{
case 1: create();
	break;

case 2: display();
	break;

case 3: insert_ele();
	break;

case 4: delete_ele();
	break;

default: printf("invalid choice\n");
}
} while(ch<=4);
}
