#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

int *p;
int no_of_fails = 0;
int m;

void func1() {
  for (int i = 0; i < m; i++) {
    kill(p[i], SIGTERM);
  }
  printf("All child processes have been killed\n");
  kill(getpid(), SIGTERM);
}

void func2() {
  printf("Element not found by any child process\n");
  kill(getpid(), SIGTERM);
}

bool search(int *arr, int low, int high, int x) {
  for (int i = low; i < high; i++) {
    if (arr[i] == x) {
      return true;
    }
  }
  return false;
}

int main() {
  srand(time(NULL));
  int n, x, new_process;
  int status = 0;
  pid_t child_pid, wpid;
  printf("Enter no. of elements = ");
  scanf("%d", &n);
  int arr[n];
  printf("Enter array elements:\n");
  for (int i = 0; i < n; i++) {
    arr[i] = rand() % 1000 + 1;
  }
  printf("The Array Elements are\n");
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\nEnter element to be searched = ");
  scanf("%d", &x);
  printf("Enter no. of processes to be created = ");
  scanf("%d", &m);
  p = (int *)malloc(sizeof(int) * m);
  int eachGrp = (n / m) + ((n % m) ? 1 : 0);
  printf("Parent process, ID = %d\n", getpid());
  signal(SIGUSR1, func1);
  signal(SIGUSR2, func2);
  for (int i = 0; i < m; i++) {
    int lo = i * eachGrp + 1;
    int hi = lo + eachGrp;
    // printf("Searching in group %d\n", i+1);
    new_process = fork();
    if (new_process == 0) {
      printf("Inside child[%d] with ID = %d\n", i + 1, getpid());
      if (search(arr, lo, hi, x)) {
        printf("Search successful by child[%d]\n", i + 1);
        kill(getppid(), SIGUSR1);
      }
      exit(i);
    }
    p[i] = new_process;
  }
  while ((wpid = wait(&status)) > 0)
    ;
  kill(getpid(), SIGUSR2);
  return 0;
}
