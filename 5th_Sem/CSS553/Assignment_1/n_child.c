#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
  int n;
  printf("Enter the number n: ");
  scanf("%d", &n);

  FILE *file;

  file = fopen("log.txt", "w");

  printf("[parent] pid: %d ppid: %d \n", getpid(), getppid());
  fprintf(file, "%s %d \n", "[parent]:", getpid());
  wait(NULL);
  fclose(file);

  for (int i = 0; i < n; i++) {
    if (fork() == 0) {
      printf("[child] pid: %d from [parent] ppid: %d \n", getpid(), getppid());

      file = fopen("log.txt", "a");
      fprintf(file, "%s %d %s %d \n", "[child", i + 1, "]:", getpid());
      fclose(file);

      exit(0);
    }
  }
  // for (int i = 0; i < n; i++)
  //   wait(NULL);
}