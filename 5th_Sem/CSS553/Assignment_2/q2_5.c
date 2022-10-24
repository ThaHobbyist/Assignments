#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int isPrime(int n) {
  for (int i = 2; i * i <= n; i++) {
    if (n % i == 0)
      return 0;
  }

  return 1;
}

void printPrime(int a, int b) {
  FILE *file;
  file = fopen("log3.txt", "a");

  for (int i = a; i <= b; i++) {
    if (isPrime(i) && i >= 2) {
      printf("%d ", i);
      fprintf(file, "%d ", i);
    }
  }

  fclose(file);
}

int main(void) {
  int a, b;
  printf("Lower Limit(a): ");
  scanf("%d", &a);
  printf("Upper Limit(b): ");
  scanf("%d", &b);
  int m;
  printf("No. of processes(m): ");
  scanf("%d", &m);

  FILE *file;

  file = fopen("log3.txt", "w");
  fprintf(file, "Prime numbers between %d and %d : \n", a, b);
  fclose(file);

  int i = 1;
  pid_t x;

  int d = (b - a) / m;

  for (i = 0; i < m; i++) {
    x = fork();
    if (x == 0) {

      printPrime(a + (i * d), a + ((i + 1) * d));
      exit(0);
    }
  }

  sleep(1);
  printf("\n");
}