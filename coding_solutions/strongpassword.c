#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int minimumNumber(int n, char* password) {
    // Return the minimum number of characters to make the password 
    int answer=0;
    char p;
    int i,j=0,l=0;
  char  numbers[] ={ "0123456789"};
char lower_case[]= {"abcdefghijklmnopqrstuvwxyz"};
char upper_case[]= {"ABCDEFGHIJKLMNOPQRSTUVWXYZ"};
    char sp[] = {"!@#$%^&*()-+"};
        for(i=0;password[i]!='\0';i++)
        {j=0;
             p=password[i];
            while(numbers[j]!='\0')
            {
              if(numbers[j]==p)
              {
                 goto there;
              }
                j++;
                
            }
            
        }
        answer=answer+1;
      there:  for(i=0;password[i]!='\0';i++)
        {j=0;
             p=password[i];
            while(lower_case[j]!='\0')
            {
              if(lower_case[j]==p)
              {
                 goto here;
              }
                j++;
                
            }
            
        }
        answer=answer+1;
   here:     for(i=0;password[i]!='\0';i++)
        {j=0;
             p=password[i];
            while(upper_case[j]!='\0')
            {
              if(upper_case[j]==p)
              {
                 goto down;
              }
                j++;
                
            }
            
        }
        answer=answer+1;
  down:      for(i=0;password[i]!='\0';i++)
        { j=0;
             p=password[i];
            while(sp[j]!='\0')
            {
              if(sp[j]==p)
              {
                 goto hi;
              }
                j++;
                
            }
            
        }
        answer=answer+1;
hi:if(n<6){
    if((answer+n)<6){
        l=6-n;
        answer=(l-answer)+answer;
    }
}
    
return answer;
}

int main() {
    int n; 
    scanf("%i", &n);
    char* password = (char *)malloc(512000 * sizeof(char));
    scanf("%s", password);
    int answer = minimumNumber(n, password);
    printf("%d\n", answer);
    return 0;
}
