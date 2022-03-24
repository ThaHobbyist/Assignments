#include "bits/stdc++.h"
using namespace std;
class Matrix
{
   int **a;
   int r, c, t;
 
public:
   Matrix()
   {
       r = 0;
       c = 0;
       t = -1;
       a = new int *[r];
   }
   Matrix(int R, int C)
   {
       r = R;
       c = C;
       t = -1;
       a = new int *[r];
       for (int i = 0; i < r; i++)
       {
           a[i] = new int[c];
       }
   }
   Matrix(const Matrix &M)
   {
       r = M.r;
       c = M.c;
       t = -1;
       a = new int *[r];
       for (int i = 0; i < r; i++)
       {
           a[i] = new int[c];
           for (int j = 0; j < c; j++)
           {
               a[i][j] = M.a[i][j];
           }
       }
   }
   bool checkEqualOrder(const Matrix &M)
   {
       if (M.c == c && M.r == r)
           return true;
       return false;
   }
   Matrix operator+(const Matrix &M)
   {
       if (checkEqualOrder(M))
       {
           for (int i = 0; i < r; i++)
           {
               for (int j = 0; j < c; j++)
               {
                   a[i][j] += M.a[i][j];
               }
           }
       }
       return *this;
   }
   Matrix operator-(const Matrix &M)
   {
       if (checkEqualOrder(M))
       {
           for (int i = 0; i < r; i++)
           {
               for (int j = 0; j < c; j++)
               {
                   a[i][j] -= M.a[i][j];
               }
           }
       }
       return *this;
   }
   bool checkMulOrder(const Matrix &M)
   {
       return c == M.r;
   }
   Matrix operator*(const Matrix &M)
   {
       if (checkMulOrder(M))
       {
           Matrix M2(r, M.c);
           for (int i = 0; i < r; i++)
           {
               for (int j = 0; j < M.c; j++)
               {
                   for (int k = 0; k < c; k++)
                   {
                       M2.a[i][j] += a[i][k] * M.a[k][j];
                   }
               }
           }
           return M2;
       }
       return *this;
   }
   void Copy(const Matrix &M)
   {
       delete[] a;
       a = new int *[M.r];
       r = M.r;
       c = M.c;
       for (int i = 0; i < r; i++)
       {
           a[i] = new int[c];
           for (int j = 0; j < c; j++)
           {
               a[i][j] = M.a[i][j];
           }
       }
   }
   bool Compare(const Matrix &M)
   {
       if (r == M.r && c == M.c)
       {
           for (int i = 0; i < r; i++)
           {
               for (int j = 0; j < c; j++)
               {
                   if (a[i][j] != M.a[i][j])
                       return false;
               }
           }
           return true;
       }
       else
           return false;
   }
   Matrix operator!()
   {
       for (int i = 0; i < r; i++)
       {
           for (int j = i; j < c; j++)
           {
               int t = a[i][j];
               a[i][j] = a[j][i];
               a[j][i] = t;
           }
       }
       return *this;
   }
   int *operator[](int x)
   {
       if (x >= r)
       {
           t = -1;
           return NULL;
       }
       t = x;
       return a[x];
   }
   int operator[](long x)
   {
       if (x > c || t == -1)
       {
           cout << "Out of Bounds access!" << endl;
           exit(1);
           return 2e-5;
       }
       return a[t][x];
   }
   bool operator==(const Matrix &M)
   {
       return Compare(M);
   }
   bool operator!=(const Matrix &M)
   {
       return !Compare(M);
   }
   void operator=(const Matrix &M)
   {
       Copy(M);
   }
   friend ostream &operator<<(ostream &x, const Matrix &M)
   {
       for (int i = 0; i < M.r; i++)
       {
           for (int j = 0; j < M.c; j++)
           {
               x << M.a[i][j] << " ";
           }
           x << endl;
       }
       return x;
   }
   friend istream &operator>>(istream &x, Matrix &M)
   {
       for (int i = 0; i < M.r; i++)
       {
           for (int j = 0; j < M.c; j++)
           {
               x >> M.a[i][j];
           }
       }
       return x;
   }
};
int main()
{
   int r1, r2, c1, c2;
   cout << "Enter order of first matrix:";
   cin >> r1 >> c1;
   cout << "Enter order of second matrix:";
   cin >> r2 >> c2;
   Matrix M1(r1, c1), M2(r2, c2);
   cout << "Enter first Matrix:\n";
   cin >> M1;
   cout << "Enter second Matrix:\n";
   cin >> M2;
   cout << "The 1<st Matrix is : \n";
   cout << M1;
   cout << "The 2nd Matrix is : \n";
   cout << M2;
   Matrix M3(r1, c1);
   M3 = M1 + M2;
   cout << "The Addition of 2 matrices is : \n";
   cout << M3;
   Matrix M4(r1, c1);
   M4 = M1 - M2;
   cout << "The Difference of 2 matrices is : \n";
   cout << M4;
   Matrix M5(r1, c1);
   M5 = M1 * M2;
   cout << "The Product of 2 matrices is : \n";
   cout << M5;
   cout << "Inversion of a matrix is : \n"
        << (!M1) << endl;
   if (M1 == M2)
   {
       cout << "The Matrices are equal!" << endl;
   }
   else
   {
       cout << "The Matrices are not equal!" << endl;
   }
   cout << "Enter subscript as row followed by column :\n";
   int x, y;
   cin >> x >> y;
   cout << "Output: " << M1[x][y] << endl;
   cout << "Copying M1 to M2:";
   M2 = M1;
   cout << "M2: \n"<< M2 << endl;
   return 0;
}
