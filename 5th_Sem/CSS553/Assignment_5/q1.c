#include <linux/sched.h>
#include <stdio.h>
#include <stdbool.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
int c=0;
sem_t sem;
int cp(int n)
{
 for (int k = 2; k <= (n / 2); k++)
 {
 if (n % k == 0)
 {
 return 0;
 }
 }
 return 1;
}
void *fp(void *at)
{
 int k = (*(int *)(at)), xt = *((int *)(at) + 1);
 
 for (int j = k; j <= xt; j++)
 {
 if ((cp(j) == 1) && (j != 1))
 {
 sem_wait(&sem);
 c++;


 sem_post(&sem);
 }
 }
}
void main()
{
 long long int i = 0, n = 0, t = 0;
 printf("Give the value of n: ");
 scanf("%lld", &n);
 t = sem_init(&sem, 1, 1);
 int d = n / 2;

 pthread_t id[2];
 int a[2][2];
 for (i = 1; i <= 2; i++)
 {
 int x = (i * d) + 1, k = ((i - 1) * d) + 1;
 a[i - 1][0] = k;
 a[i - 1][1] = x;
 pthread_create(&id[i - 1], NULL, fp, &a[i - 1]);
 }
 for (i = 1; i <= 2; i++)
 {
 int res = pthread_join(id[i - 1], NULL);
 }
 sem_destroy(&sem);
 printf(" prime numbers = %d \n", c);
}