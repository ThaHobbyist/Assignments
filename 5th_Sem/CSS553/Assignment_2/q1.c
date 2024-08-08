#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void f2(int x) {
  printf("\n Recieved signal from child : %d", x);
  printf("\n Adios");
  kill(getpid(), SIGTSTP);
}

void proc(int n) {
  if (n == 0)
    return;
  else if (fork() == 0) {
    pid_t pp = getppid(), p = getpid();
    FILE *file;
    file = fopen("log2.txt", "a");
    printf("[child %d ]: %d, [parent]: %d\n", n, p, pp);
    fprintf(file, "[child %d ]: %d, [parent]: %d\n", n, p, pp);
    fclose(file);

    proc(--n);
    signal(SIGINT, f2);
    for (;;)
      ;
    exit(0);
  }
}

void f1(int x) {
  printf("\n Signal recieved: %d", x);
  printf("\n u can't stop me \n");
  signal(SIGINT, f1);
}

int main() {
  int n;
  FILE *file;
  printf("Enter the number of processes: ");
  scanf("%d", &n);

  int *pros = malloc((n + 1) * sizeof(int *));

  file = fopen("log2.txt", "w");
  printf("[parent]: %d\n", getpid());
  fprintf(file, "[parent]: %d\n", getpid());
  pros[0] = getpid();
  fclose(file);
  wait(NULL);

  proc(n);

  signal(SIGINT, f1);
  for (;;)
    ;
}