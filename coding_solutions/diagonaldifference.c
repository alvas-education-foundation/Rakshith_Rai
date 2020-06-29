#include <math.h>
#include <stdio.h>
#include <stdlib.h>
int main(){ int a[100][100];
    int n,i,j,s=0,r=0,t;
     scanf("%i",&n);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++)
           scanf("%i",&a[i][j]);}i=0;j=0;
    while(i<n){
        s=s+a[i][j];
    i++;j++;}i=0;j=n-1;
    while(i<n){
        r=r+a[i][j];
    j--;i++;}
    t=abs(s-r);
    printf("%d",t);
    return 0;
}
