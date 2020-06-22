#include <stdio.h>
#include <stdlib.h>
int main() {
    int n,m,i,j;
    scanf("%d", &n);
    int *grades = malloc(sizeof(int) * n);
    int *result=malloc(sizeof(int)*n);
    for(i=0;i<n;i++)
       scanf("%d",&grades[i]);
     for(i=0;i<n;i++)
    {
        if(grades[i]>=38){
            m=grades[i];
        while(m%5!=0)
        {
            m++;
        }
        j=m-grades[i];
        if(j<3)
            result[i]=m;
        else
            result[i]=grades[i];}
        else
            result[i]=grades[i];
    }
    for(i=0;i<n;i++)
        printf("%d\n",result[i]);
    
    return 0;
}
