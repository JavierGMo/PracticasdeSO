#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char *argv[]){
	time_t inicio, fin;
	inicio = time(NULL);
	//printf("inicion: %lu s \n", inicio);
	while(1){
		printf("Aqui estoy \n");
		system("pidof -s bin/bin2/pro2");
		if((int)difftime(fin, inicio) == 30){
			printf("Proceso terminado. \n tiempo: %fu s \n", difftime(fin, inicio));
			break;
		}
		fin = time(NULL);
	}
	//fin = time(NULL);
	//printf("final %lu \n", fin);
	//printf("tiempo elepsado: %fu s \n", difftime(fin, inicio));
}
