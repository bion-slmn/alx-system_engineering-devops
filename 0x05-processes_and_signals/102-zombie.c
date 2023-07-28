#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int infinite_while(void);
/**
 * main - creates zombies
 *
 * Return: 0 in suceess an d 1 0n failure
 */
int main(void)
{
	int i, pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else if (pid > 0)
			sleep(1);
		else
			return (1);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - creates an infinte while loop
 *
 * Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
