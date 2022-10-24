#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

pid_t am[2];
int dx = 2;
void fun(int xd) {
  int i = 0;
  FILE *f = fopen("log.txt", "r");
  fscanf(f, "%d\n", &i);
  fclose(f);

  printf("Prime Number = %d\n", i);
  kill(am[0], SIGINT);
  kill(am[1], SIGINT);
  signal(SIGINT, SIG_DFL);
  kill(getpid(), SIGINT);
}

void fun2(int xd) {
  dx--;
  if (dx == 0) {
    printf("No Prime in this range\n");
    kill(am[0], SIGINT);
    kill(am[1], SIGINT);
    signal(SIGINT, SIG_DFL);
    kill(getpid(), SIGINT);
  }
}

int checkprime(int n) {
  for (int k = 2; k <= (n / 2); k++) {
    if (n % k == 0) {
      return 0;
    }
  }
  return 1;
}

void main(void) {
  signal(SIGUSR1, fun);
  signal(SIGUSR2, fun2);

  int i = 0, n = 0, m = 0;
  printf("Give the range:\n");
  scanf("%d %d", &n, &m);

  int md = n + (m - n) / 2;
  for (i = 1; i <= 2; i++) {
    am[i - 1] = fork();
    if (am[i - 1] == 0) {
      // signal(SIGINT, SIG_DFL);
      int j = 0, k = 0, l = 0;
      if (i == 1) {
        k = n;
        l = md - 1;
      } else {
        k = md;
        l = m;
      }
      for (j = k; j <= l; j++) {
        int ddl = checkprime(j);
        if (ddl == 1 && j != 1) {

          FILE *f;
          f = fopen("log.txt", "w+");
          fprintf(f, "%d\n", j);
          fflush(f);
          fclose(f);
          kill(getppid(), SIGUSR1);
          break;
        }
      }
      kill(getppid(), SIGUSR2);
      break;
    }
  }

  for (;;)
    ;
}