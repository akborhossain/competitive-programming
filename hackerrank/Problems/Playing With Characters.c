#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    char s,s1[100],s2[100];
    scanf("%[^\n]%*c", &s);
    scanf("%[^\n]%*c", &s1);
    scanf("%[^\n]%*c", &s2);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("%c\n",s);
    printf("%s\n",s1);
    printf("%s\n",s2);

    return 0;
}
