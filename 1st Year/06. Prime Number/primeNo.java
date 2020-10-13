
import java.util.*;
class Main
{
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter the Number----->");
		int n=sc.nextInt();
		if(isPrime(n))
		System.out.println(n+ " is a Prime Number");
		else
		System.out.println(n+" is not a Prime Number");
	}
 static boolean	isPrime(int n){
	    int c=0;
	    for(int i=1;i<=(int)Math.sqrt(n);i++){
	        if(n%i==0)
	        c=c+1;
	        if(c>1){
	            return false;
	            
	        }
	        
	    }
	    return true;
	}
}
/******************************************************************************

Sample output
Enter the Number----> 7
7 is a Prime Number

Enter the Number----> 9
9 is not Prime Number

*******************************************************************************/
