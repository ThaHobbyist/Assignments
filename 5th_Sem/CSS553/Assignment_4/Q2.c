#include <stdio.h>
#include <stdlib.h>
#define __USE_GNU 1
#include <math.h>
#include <sched.h>
#define STACK_SIZE (1024 * 1024)

typedef struct {
  int start;
  int end;
} range;

static int prime_nos(void *arg) {
  range *r = (range *)arg;
  int i, j;
  printf("Primes in %d === %d\n", r->start, r->end);
  for (i = r->start == 1 ? 2 : r->start; i <= r->end; i++) {
    int flag = 1;
    for (j = 2; j <= i / 2; j++) {
      if (i % j == 0) {
        flag = 0;
        break;
      }
    }
    if (flag)
      printf("%d\t", i);
  }
  printf("\n");
  return (0);
}

int main() {
  range r;
  char *stack = malloc(STACK_SIZE);
  int n, m, i;
  printf("Enter n = ");
  scanf("%d", &n);
  printf("Enter no. of threads = ");
  scanf("%d", &m);
  
  for (i = 0; i < m; i++) {
    r.start = n / m * i + 1;
    if (i == m - 1)
      r.end = n;
    else
      r.end = n / m * (i + 1);
    clone(prime_nos, stack + STACK_SIZE, 0, (void *)(&r));
  }
  return (0);
}