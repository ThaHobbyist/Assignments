#include <stdio.h>
#include <stdlib.h>
#define __USE_GNU 1
#include <pthread.h>
#include <time.h>
#define N 10
static int nums[N] = {0};
void *func(void *arg) {
  int i, sum = 0;
  for (i = 0; i < N; i += 2) {
    if (nums[i] != 0)
      nums[i + 1] = nums[i] + 2;
    sum = sum + nums[i];
  }
  printf("\nThe Array ===>\n");
  for (i = 0; i < N; i++)
    printf("\t%d", nums[i]);
  printf("\n");
  printf("\nSum of odd indexes= %d\nAverage of odd indexes= %.4f\n", sum,
         sum / 5.0);
  pthread_exit(0);
}
int main() {
  srand(time(NULL));
  int i, sum = 0;
  pthread_t tid;
  for (i = 0; i < N; i += 2)
    nums[i] = rand() % 100;
  pthread_create(&tid, NULL, &func, NULL);
  pthread_join(tid, NULL);
  for (i = 1; i < N; i++)
    sum = sum + nums[i];
  printf("\nSum of even indexes= %d\nAverage of even indexes= %.4f\n", sum,
         sum / 5.0);
  return (0);
}