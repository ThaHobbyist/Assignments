#include <stdio.h>
#include <stdlib.h>
#define __USE_GNU 1
#include <errno.h>
#include <pthread.h>
#include <string.h>
static int x = 0;

void *func(void *arg) {
  char *ret;
  ret = (char *)malloc(20);
  if ((int *)arg)
    printf("Created the Detached Thread\n");
  else
    printf("Created the Joinable Thread\n");
  sprintf(ret, "Thread#%d", x);
  x++;
  pthread_exit(ret);
}

int main() {
  pthread_attr_t attr;
  int status, n, i;
  printf("Enter number of Threads = ");
  scanf("%d", &n);
  pthread_t *tid = (pthread_t *)malloc(sizeof(pthread_t) * n);
  status = pthread_attr_init(&attr);

  if (status != 0) {
    printf("Error initalizing attributes");
    exit(0);
  }

  pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
  for (i = 0; i < n; i++) {
    if (i % 2 == 1)
      status = pthread_create(&tid[i], &attr, &func, (void *)1);
    else
      status = pthread_create(&tid[i], NULL, &func, (void *)0);
      
    if (status != 0)
      printf("Error creating thread");
    void *retval = NULL;
    status = pthread_join(tid[i], &retval);

    if (status == EINVAL)
      printf("Detached Thread#%d === Return Value: %s --- Status: %d\n", i,
             (char *)retval, status);
    else if (status == 0)
      printf("Joinable Thread#%d === Return Value: %s --- Status: %d\n", i,
             (char *)retval, status);
  }
  return (0);
}