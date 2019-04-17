#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]){

	while(1){
		printf("Aqui estoy \n");
		system("pidof -s bin/bin1/practica3");
		//sleep(3);
	}


	return 0;
}

