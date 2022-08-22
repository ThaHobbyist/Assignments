#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void proc(int n) {
  if (n == 0)
    return;
  else if (fork() == 0) {
    FILE *file;
    file = fopen("log2.txt", "a");
    printf("[child %d ]: %d, [parent]: %d\n", n, getpid(), getppid());
    fprintf(file, "[child %d ]: %d, [parent]: %d\n", n, getpid(), getppid());
    fclose(file);

    proc(--n);
    wait(NULL);
    exit(0);
  }
}

int main() {
  int n;
  FILE *file;
  printf("Enter the number of processes: ");
  scanf("%d", &n);

  file = fopen("log2.txt", "w");
  printf("[parent]: %d\n", getpid());
  fprintf(file, "[parent]: %d\n", getpid());
  fclose(file);
  wait(NULL);

  proc(n);
  wait(NULL);
}