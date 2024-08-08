#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
int main() {
  int i = 0;
  struct timeval start, end;
  gettimeofday(&start, NULL);
  while (i < 100000) {
    if (fork() == 0)
      exit(0);
    else
      i++;
  }
  gettimeofday(&end, NULL);
  double dif = (double)(end.tv_usec - start.tv_usec) / 1000000 +
               (double)(end.tv_sec - start.tv_sec);
  printf("Time taken to spawn 100000 child processes = %.4f s\n", dif);
  return 0;
}