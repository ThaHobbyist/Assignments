#include <stdio.h>
#include <stdlib.h>
#define __USE_GNU 1
#include <pthread.h>
static int x = 1;

void *func(void *arg) {
  int* m = (int *)arg;
  for (int i = 0; i < *m; i++)
    x = x + 1;
  pthread_exit(0);
}

int main() {
  int n, m, i;
  printf("Enter number of Threads = ");
  scanf("%d", &n);
  printf("Enter number of Increments = ");
  scanf("%d", &m);
  pthread_t *tids = (pthread_t *)malloc(sizeof(pthread_t) * n);
  
  for (i = 0; i < n; i++)
    pthread_create(&tids[i], NULL, &func, (void *)(&m));

  for (i = 0; i < n; i++)
    pthread_join(tids[i], NULL);

  printf("Final value of x = %d\n", x);
}