#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n;
    int t,i;
    scanf("%d",&n);
    if(n==0)
    {
        printf(" no staircase\n");
    }
    else
    {
        printf("%*s\n",n,"#");
        for(t=n-1;t>0;t--)
        {i=t;
            printf("%*s",t,"#");
            while(t<n)
            {
            printf("%s","#");
                t++;
            }
            t=i;
            printf("\n");
            
        }
        }
            
    return 0;
}
