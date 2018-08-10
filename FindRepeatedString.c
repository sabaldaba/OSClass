#include <stdio.h>

#ifndef N
#define N 256
#endif

int findFirstRepeated(unsigned char[]);

int main(void)
{
	
	findFirstRepeated("0012");
	
return 0;	
}

int findFirstRepeated(unsigned char sentence [])
{
	unsigned char allChars [N] = {0}; //arreglo de caracteres para contar en 0's
	unsigned char *ptr;
	unsigned char tmp;
	unsigned char found = 0;
	unsigned char allRep = 0;
	
	printf("La oracion es: %s\n", sentence);
	for(ptr=sentence; *ptr!=0, found!=1; ptr++){
		tmp = (int)*ptr;
		allChars[tmp]++;
		if(allChars[tmp]>1){
			printf("\n \nWe found one");
			printf("The first character found was: %c\n", tmp);
			return 1;
		}
	}
	
	return 1;
}
