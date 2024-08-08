#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdbool.h>
#include <math.h>
#include <sys/wait.h>
#include <pthread.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <semaphore.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#define SEMAPHORE_NAME "/sem-mutex"
#define SHM_KEY 0x1234
bool isprime(int n)
{
 if (n == 1)
 return 0;
 for (int i = 2; i * i <= n; i++)
 {
 if (n % i == 0)
 return false;
 }
 return true;
}
void *printprime(int st, int en, sem_t *sem, int *count)
{
 for (int i = st; i <= en; i++)
 {
 if (isprime(i))
 {
 sem_wait(sem);
 (*count)++;
 sem_post(sem);
 }
 }
 return NULL;
}
int main()
{
 int shmid;
 void *sh_mem;
 int *count;
 shmid = shmget(SHM_KEY, sizeof(int), 0666 | IPC_CREAT);
 sh_mem = shmat(shmid, NULL, 0);
 count = (int *)sh_mem;
 *count = 0;
 int n, m = 10;
 printf("\nGive the value of n: ");
 scanf("%d", &n);
 int range = n;
 m = m > range ? range : m;
 int grpsize = range / m;
 if (range % m != 0)
 grpsize++;
 int j = 1;
 for (int i = 1; i <= m; i++)
 {
 if (i == range % m + 1 && i != 1)
 grpsize--;
 if (fork())
 {
 j += grpsize;
 continue;
 }
 else
 {
 sem_t *binary_sem = sem_open(SEMAPHORE_NAME,O_CREAT, 0660, 1);
 printprime(j, j + grpsize - 1, binary_sem, count);
 shmdt(sh_mem);
 exit(1);
 }
 }
 while (wait(NULL) > 0);
 printf("Total count of prime nos: %d\n\n", *count);
 sem_unlink(SEMAPHORE_NAME);
 shmctl(shmid, IPC_RMID, 0);
}