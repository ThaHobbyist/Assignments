#include <stdio.h>
#include <stdlib.h>

int min(int a, int b) {
  int mi = a;
  if (mi > b)
    mi = b;
  return mi;
}

int max(int a, int b) {
  int ma = a;
  if (ma < b)
    ma = b;
  return ma;
}

void merge(float arr[], int l, int m, int r) {
  int i, j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  float L[n1], R[n2];

  for (i = 0; i < n1; i++)
    L[i] = arr[l + i];
  for (j = 0; j < n2; j++)
    R[j] = arr[m + 1 + j];

  i = 0;
  j = 0;
  k = l;
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

void mergeSort(float arr[], int l, int r) {
  if (l < r) {
    int m = l + (r - l) / 2;

    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    merge(arr, l, m, r);
  }
}

int main(void) {
  int n;
  printf("Write n:");
  scanf("%d", &n);

  float *x = (float *)malloc(n * 2 * sizeof(float));
  float *y = (float *)malloc(n * 2 * sizeof(float));

  for (int i = 0; i < n; i++) {
    int h, w;
    scanf("%f %f %d %d", &x[i], &y[i], &w, &h);

    x[i + n] = x[i] + w;
    y[i + n] = y[i] + h;
  }

  mergeSort(x, 0, n - 1);
  mergeSort(y, 0, n - 1);

  float x_l = x[n];
  printf("\n%f\n", x_l);

  
}