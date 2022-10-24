// Name: Sayantani Karmakar
// Roll No. 20CS8024

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 5

typedef struct {
  double coord[3];
  int ypart, zpart;
} point;

point *genpoints(int n) {
  point *A;
  int i;

  A = (point *)malloc(n * sizeof(point));
  for (i = 0; i < n; ++i) {
    A[i].coord[0] = (double)rand() / (double)RAND_MAX;
    A[i].coord[1] = (double)rand() / (double)RAND_MAX;
    A[i].coord[2] = (double)rand() / (double)RAND_MAX;
    A[i].ypart = A[i].zpart = -1;
  }
  return A;
}

void msort(point *A, int n, int *idx, int c) {
  int *index, i, j, i1, j1, i2, j2, k;

  if (n <= 1)
    return;

  i1 = 0;
  i2 = (n - 1) / 2;
  j1 = i2 + 1;
  j2 = n - 1;

  msort(A, i2 - i1 + 1, idx, c);
  msort(A, j2 - j1 + 1, idx + (i2 - i1 + 1), c);

  index = (int *)malloc(n * sizeof(int));
  k = 0;
  i = i1;
  j = j1;
  while ((i <= i2) || (j <= j2)) {
    if (i > i2)
      index[k] = idx[j++];
    else if (j > j2)
      index[k] = idx[i++];
    else if (A[idx[i]].coord[c] < A[idx[j]].coord[c])
      index[k] = idx[i++];
    else
      index[k] = idx[j++];
    ++k;
  }

  for (k = 0; k < n; ++k)
    idx[k] = index[k];

  free(index);
}

void prnpoints(point *A, int n, int *idx) {
  int i, j;

  for (i = 0; i < n; ++i) {
    j = (idx == NULL) ? i : idx[i];
    printf("(%lf,%lf,%lf) ", A[j].coord[0], A[j].coord[1], A[j].coord[2]);
    if (i % 4 == 3)
      printf("\n");
  }
  if (i % 4)
    printf("\n");
}

void calcsupidx2(point *A, int n, int *yidx, int *xidx, int *sid, int zflag) {
  int i, j, k0, k1, n0;
  int *xidx0, *xidx1;
  int *ypart;

  if (n <= 1)
    return;

  ypart = (int *)malloc(n * sizeof(int));
  for (i = 0; i < (n + 1) / 2; ++i) {
    j = yidx[i];
    ypart[i] = A[j].ypart;
    A[j].ypart = 0;
  }
  for (i = 0; i < n / 2; ++i) {
    j = yidx[(n + 1) / 2 + i];
    ypart[(n + 1) / 2 + i] = A[j].ypart;
    A[j].ypart = 1;
  }

  xidx0 = (int *)malloc(((n + 1) / 2) * sizeof(int));
  xidx1 = (int *)malloc((n / 2) * sizeof(int));

  for (i = k0 = k1 = 0; i < n; ++i) {
    j = xidx[i];
    if (A[j].ypart == 0)
      xidx0[k0++] = j;
    else if (A[j].ypart == 1)
      xidx1[k1++] = j;
    else
      printf("*** Error 1 in calcsupidx2()\n");
  }

  calcsupidx2(A, (n + 1) / 2, yidx, xidx0, sid, zflag);
  calcsupidx2(A, n / 2, yidx + (n + 1) / 2, xidx1, sid, zflag);

  n0 = 0;
  if (zflag == 0) { /* The case of 2-d */
    for (i = 0; i < n; ++i) {
      j = xidx[i];
      if (A[j].ypart == 0)
        ++n0;
      else if (A[j].ypart == 1)
        sid[j] += n0;
      else
        printf("*** Error 2 in calcsupidx2()\n");
    }
  } else {
    for (i = 0; i < n; ++i) {
      j = xidx[i];
      if ((A[j].ypart == 0) && (A[j].zpart == 0))
        ++n0;
      else if ((A[j].ypart == 1) && (A[j].zpart == 1))
        sid[j] += n0;
    }
  }

  for (i = 0; i < n; ++i) {
    j = yidx[i];
    A[j].ypart = ypart[i];
  }

  free(xidx0);
  free(xidx1);
  free(ypart);
}

void diagnostic2(point *A, int n, int *sid) {
  int i, j;

  for (i = 0; i < n; ++i) {
    for (j = i + 1; j < n; ++j) {
      if ((A[i].coord[0] > A[j].coord[0]) && (A[i].coord[1] > A[j].coord[1]))
        sid[i]++;
      else if ((A[i].coord[0] < A[j].coord[0]) &&
               (A[i].coord[1] < A[j].coord[1]))
        sid[j]++;
    }
  }
}

int main(int argc, char *argv[]) {
  int n, i;
  int *xidx, *yidx, *zidx;
  int *supidx;
  point *A;

  srand((unsigned int)time(NULL));

  if (argc > 1)
    n = atoi(argv[1]);
  else
    n = N;

  A = genpoints(n);

  xidx = (int *)malloc(n * sizeof(int));
  yidx = (int *)malloc(n * sizeof(int));
  zidx = (int *)malloc(n * sizeof(int));
  for (i = 0; i < n; ++i)
    xidx[i] = yidx[i] = zidx[i] = i;
  msort(A, n, xidx, 0);
  msort(A, n, yidx, 1);
  msort(A, n, zidx, 2);

  printf("+++ The original points:\n");
  prnpoints(A, n, NULL);

  printf("\n+++ The points sorted wrt y-coordinates:\n");
  prnpoints(A, n, yidx);

  supidx = (int *)malloc(n * sizeof(int));

  for (i = 0; i < n; ++i)
    supidx[i] = 0;
  calcsupidx2(A, n, yidx, xidx, supidx, 0);
  printf("\n+++ Superiority indices in two dimensions (divide-and-conquer):\n");
  for (i = 0; i < n; ++i)
    printf("%3d", supidx[i]);
  printf("\n");

  for (i = 0; i < n; ++i)
    supidx[i] = 0;
  diagnostic2(A, n, supidx);
  printf("\n+++ Superiority indices in two dimensions (quadratic-time):\n");
  for (i = 0; i < n; ++i)
    printf("%3d", supidx[i]);
  printf("\n");

  exit(0);
}