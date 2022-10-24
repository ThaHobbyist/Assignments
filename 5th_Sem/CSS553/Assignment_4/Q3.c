#include <stdio.h>
#include <stdlib.h>
#define __USE_GNU 1
#include <pthread.h>
typedef struct {
  int start;
  int end;
} range;
static int *primes;
static void *prime_nos(void *arg) {
  range *r = (range *)arg;
  int i, j;
  printf("Searching Primes in %d === %d\n", r->start, r->end);
  for (i = r->start == 1 ? 2 : r->start; i <= r->end; i++) {
    int flag = 1;
    for (j = 2; j <= i / 2; j++) {
      if (i % j == 0) {
        flag = 0;
        break;
      }
    }
    if (flag)
      primes[i] = 1;
  }
  printf("Search Primes in %d === %d finished\n", r->start, r->end);
  return (0);
}
int main() {
  int n, m, i;
  printf("Enter n = ");
  scanf("%d", &n);
  printf("Enter no. of threads = ");
  scanf("%d", &m);
  primes = (int *)malloc(sizeof(int) * n);
  for (i = 0; i < n; i++)
    primes[i] = 0;
  pthread_t *tid = (pthread_t *)malloc(m * sizeof(pthread_t));
  for (i = 0; i < m; i++) {
    range *r = (range *)malloc(sizeof(range));
    r->start = n / m * i + 1;
    if (i == m - 1)
      r->end = n;
    else
      r->end = n / m * (i + 1);
    pthread_create(&tid[i], NULL, &prime_nos, (void *)r);
  }
  for (i = 0; i < m; i++)
    pthread_join(tid[i], NULL);
  for (i = 1; i <= n; i++)
    if (primes[i] == 1)
      printf("%-6d ", i);
  printf("\n");
  return (0);
}