#include <stdio.h>
#include <stdlib.h>

int pai[50010];

int achar(int x){
	if(pai[x]==x) return x;
	return achar(pai[x]);
}

int unir(int x,int y){
	pai[ achar(x) ] = achar(y);
}

int main(){
	int n,m,a,b;
	int resposta=0;
	
	scanf("%d %d",&n,&m);
	
	for(int i=1; i<=n; i++){ 
		pai[i]=i;
	}
	
	for(int i=1; i<=m; i++){
		scanf("%d %d",&a,&b);
		unir(a,b);
	}	

	for(int i=1; i<=n; i++){
		if( i == achar(i) ) resposta++;
	}

	printf("%d",resposta);

	return 0;
}
