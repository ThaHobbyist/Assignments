#include <stdio.h>

int C(int n) {
  if (n == 0)
    return 1;
  else if (n < 0)
    return 0;

  return C(n - 3) + C(n - 2) + C(n - 1);
}

int C_i(int n) {
  int res[n + 1];
  res[0] = 1;
  res[1] = 1;
  res[2] = 2;
  for (int i = 3; i <= n; i++) {
    res[i] = res[i - 1] + res[i - 2] + res[i - 3];
  }

  return res[n];
}

int C_m(int n, int m) {
  if (n == 0 && m == 0)
    return 1;
  else if (n < 0)
    return 0;

  return C_m(n - 3, m - 1) + C_m(n - 2, m - 1) + C_m(n - 1, m - 1);
}

int C_m_i(int n, int m) {
  int prev1, prev2, prev3, curr;
  if ((n < m) || (n > 3 * m))
    return 0;
  if (n <= 2)
    return 1;

  int res[n + 1];
  res[0] = 1;
  for (int i = 1; i <= n; ++i)
    res[i] = 0;

  for (int j = 1; j <= m; ++j) {

    for (int i = 0; i < j; ++i)
      res[i] = 0;

    if (j <= n) {
      prev3 = res[j];
      res[j] = 1;
    }

    if (j <= n - 1) {
      prev2 = res[j + 1];
      res[j + 1] = j;
    }

    if (j <= n - 2) {
      prev1 = res[j + 2];
      res[j + 2] = j * (j + 1) / 2;
    }

    int i = j + 3;

    while ((i <= n) && (i <= 3 * j)) {
      curr = prev3 + prev2 + prev1;
      prev3 = prev2;
      prev2 = prev1;
      prev1 = res[i];
      res[i] = curr;
      ++i;
    }

    while (i <= n)
      res[i++] = 0;
  }

  return res[n];
}

int main() {
  int n, m;
  printf("n: ");
  scanf("%d", &n);

  printf("+++ Any number of jumps...\n\n");

  printf("    Recursive function returns count = %d\n\n", C(n));

  printf("    Iterative function returns count = %d\n\n", C_i(n));

  printf("+++ Fixed number of jumps...\n\n");

  int sum = 0, count = 0;
  for (m = 0; m <= n; ++m) {
    count = C_m(n, m);
    printf("    Recursive function returns count = %d for m = %d\n", count, m);
    sum += count;
  }
  printf("    ---------------------------------------------\n");
  printf("    Total number of possibilities    = %10u\n\n", sum);

  sum = 0;
  for (m = 0; m <= n; ++m) {
    count = C_m_i(n, m);
    printf("    Iterative function returns count = %d for m = %d\n", count, m);
    sum += count;
  }
  printf("    ---------------------------------------------\n");
  printf("    Total number of possibilities    = %d\n\n", sum);

  return 0;
}