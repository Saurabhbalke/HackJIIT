#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main()
{
    int a[100][100],n,d=0,e=0,i,j,sum=0;
    scanf("%d",&n);
    for(int i=0; i<n; i++)
    for(int j=0; j<n; j++)
    {
        scanf("%d", &a[i][j]);
        
    }
    for (i=0; i<n; i++)
    d=d+a[i][i];
    for(i=0; i<n ;i++)
    e=e+a[i][n-1-i];
    sum=abs(d-e);
    printf("%d\n",sum);
}
