#include <stdio.h>
#include <sys/types.h>

int main(void) {
  FILE *f1;

  int i, x = 2000;

  for (i = 0; i < 200; i++) {
    // reads current balance from text file
    f1 = fopen("acc_balance.txt", "r");
    fscanf(f1, "bal:%d", &x);
    fclose(f1);

    x++;

    // writes updated balance to text file
    f1 = fopen("acc_balance.txt", "w+");
    fprintf(f1, "bal:%d", x);
    fclose(f1);
  }
}
