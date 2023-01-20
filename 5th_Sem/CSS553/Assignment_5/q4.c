#define __USE_GNU 1
#include <pthread.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define NRFULL "/sem-nrfull"
#define NREMPTY "/sem-nrempty"
#define MUTEXPD "/sem-mutexPd"
#define MUTEXCN "/sem-mutexCn"
#define BUFFER_SIZE 10
int in = 0;
int out = 0;
int buffer[BUFFER_SIZE];
sem_t *nrfull, *nrempty, *mutexPd, *mutexCn;
int *producer(void)
{
 int item;
 while (1)
 {
 sem_wait(mutexPd);
 sem_wait(nrempty);
 item = rand() % 100;
 buffer[in] = item;
 in = (in + 1) % BUFFER_SIZE;
 printf("Produced %d\n", item);
 sem_post(mutexCn);
 sem_post(nrfull);
 }
}
int *consumer(void)
{
 int item;
 while (1)
 {
 sem_wait(mutexCn);
 sem_wait(nrfull);
 item = buffer[out];
 out = (out + 1) % BUFFER_SIZE;
 printf("Consumed %d\n", item);
 sem_post(mutexPd);
 sem_post(nrempty);
 }
}
int main()
{
 nrfull = sem_open(NRFULL, O_CREAT, 0660, 0);
 nrempty = sem_open(NREMPTY, O_CREAT, 0660, 1);
 mutexPd = sem_open(MUTEXPD, O_CREAT, 0660, 1);
 mutexCn = sem_open(MUTEXCN, O_CREAT, 0660, 1);
 pthread_t *prod = (pthread_t *)malloc(BUFFER_SIZE * sizeof(pthread_t));
 pthread_t *cons = (pthread_t *)malloc(BUFFER_SIZE * sizeof(pthread_t));
 for(int i = 0; i < 5; i++)
 {
 pthread_create(&prod[i], NULL, (void *)producer, NULL);
 pthread_create(&cons[i], NULL, (void *)consumer, NULL);
 }
 for(int i = 0; i < 5; i++)
 {
 pthread_join(prod[i], NULL);
 pthread_join(cons[i], NULL);
 }
 return 0;
}