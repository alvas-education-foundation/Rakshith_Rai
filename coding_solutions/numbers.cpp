#include<stdio.h>
int main(){
   long int n,que,L,R;
    long int sum=0;
 	scanf("%ld",&n);              			
	scanf("%ld",&que);
long	int a[n+1];
long	int s[n+1];
long	int avg;
	s[0]=0;
	for(int i=1;i<=n;i++){
	    scanf("%ld",&a[i]);
	    sum=sum+a[i];
	    s[i]=sum;
	}
	for (int j=0;j<que;j++){  
	scanf("%ld",&L);
	scanf("%ld",&R);
    avg=(s[R]-s[L-1])/(R-L+1);
    printf("%ld\n",avg);
    
	}
}