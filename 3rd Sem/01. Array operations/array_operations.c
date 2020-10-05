//To implement various array operations.

#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
int a[10000],n,item,i,pos;

void create();
void display();
void insert();
void delete();

//function to create an array
void create()
{
	printf("Enter the size of array:");
	scanf("%d",&n);
	printf("\nEnter the elements:\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
}

//function to display an array
void display()
{
	printf("\nThe array elements are:\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
	}
}

//function to insert an element in an array
void insert()
{
	printf("Enter the position of element to be inserted in an array: ");
	scanf("%d",&pos);
	printf("\nEnter the element to be inserted in an array: ");
	scanf("%d",&item);
	if(pos<=n-1)
	{
		for(i=n-1;i>=pos;i--)
		{
			a[i+1]=a[i];
		}
		a[pos]=item;
		n=n+1;
	}
	else
	{
		printf("Invalid position\n");
	}
}

//function to delete an element from an array
void delete()
{
	printf("Enter the position of element to be deleted in an array:");
	scanf("%d",&pos);
	item=a[pos];
	if(pos<=n-1)
	{
		for(i=pos;i<=n-1;i++)
		{
			a[i]=a[i+1];
		}
		n=n-1;
		printf("The deleted element is = %d\n",item);
	}
	else
		printf("Invaild position.\n");
}

//driver code
void main()
{       
	int c;
	do
	{
        	printf("Enter operator:\n");
        	printf("---------------------------------MENU---------------------------------\n");
        	printf("1.CREATE\t2.DISPLAY\t3.INSERT\t4.DELETE\t5.EXIT\n");
        	scanf("%d",&c);

         	switch(c)
        	{
          		case 1: create();
	                	break;
                        case 2: display();
         	        	break;
                 	case 3: insert();
        	        	break;
                 	case 4: delete();
	                 	break;
                	case 5: exit(0);
                	default:printf("invald operator");
        	}
	}
	while(c!=5);
	return 0;
}
