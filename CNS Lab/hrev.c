#include<stdio.h>

void main() 
{
    int dataatrec[10],c,c1,c2,c3,i;
 
    printf("\n\n\tEnter received data bits one by one\n");
    for(i=0;i<7;i++)
        scanf("%d",&dataatrec[i]);
 
    c1=dataatrec[6]^dataatrec[4]^dataatrec[2]^dataatrec[0];
    c2=dataatrec[5]^dataatrec[4]^dataatrec[1]^dataatrec[0];
    c3=dataatrec[3]^dataatrec[2]^dataatrec[1]^dataatrec[0];
    
    c=c3*4+c2*2+c1 ;//calculating decimal value
 
    if(c==0) 
        printf("\n\tNo error while transmission of data\n");
    else
     {
        printf("\n\tError on position: %d",c);
       
        printf("\nData received : ");
        for(i=0;i<7;i++)
            printf("%d",dataatrec[i]);
        
        printf("\n\tCorrect message is: ");
 
        //if errorneous bit is 0 we complement it else vice versa
        if(dataatrec[7-c]==0)
            dataatrec[7-c]=1;
        else
            dataatrec[7-c]=0;
        
        for (i=0;i<7;i++) 
            printf("%d",dataatrec[i]);
        
    }
}
   
