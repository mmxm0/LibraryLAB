#include <stdio.h>
#include <stdlib.h>

int main(){

	int n,resposta=0;
	
	scanf("%d",&n);
	
	for(int a=1; a*a <=n; a++){
		
		int b=(n+a-1)/(2*a-1);
		
		int tentativa=( (a*b) + ( (a-1)*(b-1) ) );
		
		if( tentativa==n && a<=b && a!=1) resposta++;
	}	

	printf("%d",resposta);
	
	return 0;
}
