#include <time.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

pid_t pid;
int r;
int search(int arr[], int low, int high, int x) {
  for (int i = low; i < high; i++) {
    if (arr[i] == x) {
      return 1;
    }
  }
  return 0;
}

void handler_parent_1(int sig) {
  kill(pid, SIGTERM);
  kill(getpid(), SIGTERM);
}
void handler_parent_2(int sig) {
  printf("Search unsuccessful\n");
  kill(pid, SIGTERM);
}

int main() {
  srand(time(NULL));
  int n, h1, low = 0, xx;
  printf("Enter value of n : ");
  scanf("%d", &n);
  pid_t chid;
  int eex;
  int arr[n];
  if (n % 2 != 0) {
    h1 = n / 2;
  } else if (n % 2 == 0) {
    h1 = n / 2 - 1;
  }
  for (int i = 0; i < n; i++) {
    int num = rand() % 50 + 1;
    ;
    arr[i] = num;
  }
  printf("arr[n] :\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
  printf("Enter value of X :");
  scanf("%d", &xx);
  printf("Parent pid : %d\n", getpid());

  signal(SIGUSR1, handler_parent_1);
  signal(SIGUSR2, handler_parent_2);
  for (int id = 0; id < 2; id++) {
    pid_t x = fork();
    if (x > 0) {
      chid = wait(&eex);
    } else if (x == 0) {
      pid = getpid();
      printf("Inside child[%d] :pid %d\n", id, pid);
      if (id == 0) {
        r = 0;
        int k = search(arr, 0, h1, xx);
        if (k == 1) {
          printf("Search successful by child[%d] \n", id);
          kill(getppid(), SIGUSR1);
        }
        exit(0);
      } else if (id == 1) {
        r = 1;

        int k = search(arr, h1, n, xx);
        if (k == 1) {
          kill(getppid(), SIGUSR1);
          printf("Search successful by child[%d] \n", id);
        } else {
          sleep(2);
          kill(getppid(), SIGUSR2);
        }
        exit(1);
      }
    }
  }
}
