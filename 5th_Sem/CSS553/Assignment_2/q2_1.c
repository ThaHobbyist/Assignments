#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int cnt = 0;
pid_t child[2];

int Rand(int lower, int upper) {
  return (rand() % (upper - lower + 1)) + lower;
}

int search(int s, int *arr, int l, int h) {
  for (int i = l; i < h; i++) {
    if (arr[i] == s) {
      kill(getppid(), SIGUSR1);
      return i;
    }
  }
  kill(getppid(), SIGUSR2);
  return -1;
}

void f1() {
  printf("Number is found\n");
  kill(child[0], SIGINT);
  kill(child[1], SIGINT);
  kill(getpid(), SIGINT);
}

void f2() {
  printf("Number is not found");
  // if (cnt == 0)
  //   cnt++;
  // else {

  //   kill(child[0], SIGINT);
  //   kill(child[1], SIGINT);
  //   kill(getpid(), SIGINT);
  // }
}

int main(void) {
  int pos;
  signal(SIGUSR1, f1);
  signal(SIGUSR2, f2);

  int *arr = (int *)malloc(10 * sizeof(int *));

  for (int i = 0; i < 10; i++) {
    // arr[i] = Rand(1, 1000);
    arr[i] = i;
  }
  // int s = (rand() % (10000 - 1 + 1)) + 1;
  int s;
  printf("Enter number to search: ");
  scanf("%d", &s);
  pid_t x;
  for (int i = 0; i < 2; i++) {
    x = fork();
    if (x) {
      child[i] = x;
      continue;

    } else {
      if (i == 0)
        pos = search(s, arr, 0, 5);
      else if(i == 1)
        pos = search(s, arr, 5, 10);
      exit(0);
    }
  }


  for (;;)
    ;
}