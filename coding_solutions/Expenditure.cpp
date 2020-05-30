#include<stdio.h>
#include<stdlib.h>
long int * array;
long int cmp(const void *a, const void *b){
    long int ia = *(long int *)a;
    long int ib = *(long int *)b;
    return array[ia] < array[ib] ? -1 : array[ia] > array[ib];
}
int main()
{
 
    long int q,n,sum=0,mincost=0;
    scanf("%ld",&q);
    for(int k=0;k<q;k++){
    mincost=0;
    sum=0;
    scanf("%ld",&n);
   long int  N=n;
 long  int t[n];
  long  int l[n],p[n];
  long  int s2[n+1];
 
    for(int i=0;i<n;i++)
    {
        scanf("%ld",&p[i]);
        t[i]=i;
    }
    array=p;
    s2[0]=0;
    for(int i=0;i<n;i++)
    {
        scanf("%ld",&l[i]);
        sum=sum+l[i];
        s2[i+1]=sum;
    }
    qsort(t,n,sizeof(* t),cmp);
   for(int i=0;N>0;i++){
        if(N>t[i])
        {
           mincost =mincost+(p[t[i]]*(s2[N]-s2[t[i]]));
            N=t[i];
         
        }}
           printf("%ld\n",mincost);
 
 
}
 
    return 0;
}