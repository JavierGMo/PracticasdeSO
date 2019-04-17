#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <string.h>

int pid = 0;

void parar();

int main(int argc, char *argv[]){
	while(1){
		printf("Aqui estoy \n");
		printf("Proceso: %d \n", getpid());
		pid = (int)getpid();
		signal(SIGINT, parar);
		sleep(3);
	}
	return 0;
}

void parar(){
	signal(SIGINT, SIG_IGN);
	printf("\n Terminacion por interrupcion del S.O. \n");
	char prid[20];
	char cmm[40] =  "kill -9 ";
	sprintf(prid, "%d", pid);
	strcat(cmm, prid);
	//printf("%s \n", cmm);
	system(cmm);
	signal(SIGINT, parar);
}
