#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int birthdayCakeCandles(int n, int ar_size, int* ar) {
    // Complete this function
    int result,c=0;
    int i,max=0;
    for(i=0;i<n;i++){
        if(ar[i]>=max)
            max=ar[i];}   
     for(i=0;i<n;i++){
         if(max==ar[i])
             c++;}
    result=c;
                 return result;
}

int main() {
    int n; 
    scanf("%d", &n);
    int *ar = malloc(sizeof(int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%d",&ar[ar_i]);
    }
    int result = birthdayCakeCandles(n, n, ar);
    printf("%d\n", result);
    return 0;
}