#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(){
	int *num_al, n;
	//tuberias
	int pip1[2], pip2[2], pip3[2], pip4[2];
	int res, res2, res3 = 0, res4 = 0;
	int sum1 = 0, sum2 = 0, suma;
	int par = 0, impar = 0, pr1, pr2;
	//processid
	int ip_padre = getpid();

	printf("Cuantos numeros: ");
	scanf("%d", &n);

	srand(time(NULL));
	//creamos las tuberias
	/*
		Posdata: Nunca olviden abrir todas las tuberias con las que 
		piensan trabajar, pueden existir problemas al momento de trabajar con ellas
		En mi caso olvide abrir la tuberia 3 y 4 y me mandaba valores basura.

		tuberia[0]-->lectura
		tuberia[1]-->escritura
	*/
	pipe(pip1);
	pipe(pip2);
	pipe(pip3);
	pipe(pip4);

	num_al = (int *) calloc(n, sizeof(int));

	if(num_al == NULL){
		printf("No se creo xd...");
		//si no se asigno memoria se sale
		exit(0);
	}
	//crea numeros aleatorios y muestra los numeros aleatorios
	printf("\nNumeros aleatorios: \n\n");
	for (int i = 0; i < n; ++i){
		num_al[i] = rand()%51;
		printf("%d \n", num_al[i]);
		if(num_al[i]%2 == 0){
			write(pip1[1], &num_al[i], sizeof(int));
			++par;
		}else{
			write(pip2[1], &num_al[i], sizeof(int));
			++impar;
		}
	}
	
	//se cierran las tuberias

	close(pip1[1]);
	close(pip2[1]);



	printf("\n\n");
	//se creal el proceso 1
	pr1 = fork();
	if(pr1 == 0){
		printf("Proceso hijo1\n");
		close(pip1[1]);
		/*aqui use un ciclo para recorrer todos los valores que se escribieron
		en la tuberia. Pasa lo mismo en proceso hijo 2
		*/
		for (int i = 0; i < par; ++i)
		{			
			read(pip1[0], &res, sizeof(int));
			//sum2 = (int)res;
			sum1 += res;
			//printf("Pares: %d\n", res);			
		}
		close(pip1[0]);
		write(pip3[1], &sum1, sizeof(int));
		printf("Suma de pares: %d\n", sum1);
		//Este exit sirve para salir de este proceso hijo
		exit(0);
	}else if(pr1 < 0){
		printf("Error");
		system("exit");
	}

	//se crea el proceso 2
	printf("\n\n");
	pr2 = fork();
	if(pr2 == 0){
		printf("Proceso hijo2\n");
		close(pip2[1]);
		for (int i = 0; i < impar; ++i)
		{
			read(pip2[0], &res2, sizeof(int));
			sum2 += res2;			
		}
		close(pip2[0]);
		write(pip4[1], &sum2, sizeof(int));
		printf("Suma de impares: %d\n", sum2);
		exit(0);
	}else if(pr2 < 0){
		printf("Error");
		system("exit");
	}
	//aqui me aseguro de que sea el proceso padre...
	if (ip_padre == getpid()){
		printf("Proceso padre...\n");
		read(pip3[0], &res3, sizeof(int));
		//printf("Suma de pares e impares: %d\n", res3);
		read(pip4[0], &res4, sizeof(int));
		//printf("Suma de pares e impares: %d\n", res4);
		printf("Suma de pares e impares: %d\n", (res3 + res4));
		close(pip3[0]);
		close(pip4[0]);
		free(num_al);
	}

	

	return 0;

}
