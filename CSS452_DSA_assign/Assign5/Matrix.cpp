#include <iostream>
using namespace std;

class Matrix {
private:
  int rows, cols;
  int **p;

  void allocSpace(int r, int c) {
    p = new int *[r];
    for (int i = 0; i < r; ++i) {
      p[i] = new int[c];
    }
  }

public:
  Matrix() {
    rows = cols = 1;
    p = NULL;
  }
  Matrix(const Matrix &mat) {
    rows = mat.rows;
    cols = mat.cols;
    for (int i = 0; i < mat.rows; i++) {
        for (int j = 0; j < mat.cols; j++) {
          p[i][j] = 0;
        }
    }
  }
  Matrix(int r, int c) {
    rows = r;
    cols = c;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
          p[i][j] = 0;
        }
    }
  }
  ~Matrix()
  {
    for (int i = 0; i < rows; ++i) {
      delete[] p[i];
    }
    delete[] p;
  }
  Matrix operator+(const Matrix &mat) {
    if (mat.rows == rows && mat.cols == cols) {
      Matrix res(mat);
      for (int i = 0; i < mat.rows; i++) {
        for (int j = 0; j < mat.cols; j++) {
          res.p[i][j] = p[i][j] + mat.p[i][j];
        }
      }
      return res;
    } else {
      Matrix res;
      cout << "Addition is not possible" << endl;
      return mat;
    }
  }
  Matrix operator-(const Matrix &mat) {
    Matrix res(mat);
    if (mat.rows == rows && mat.cols == cols) {
      for (int i = 0; i < mat.rows; i++) {
        for (int j = 0; j < mat.cols; j++) {
          res.p[i][j] = p[i][j] - mat.p[i][j];
        }
      }
      return res;
    }
    else {
      cout << "Addition is not possible" << endl;
      return mat;
    }
  }
  Matrix operator*(const Matrix &mat) {
    if (cols == mat.rows) {
      Matrix res(rows, mat.cols);
      for (int i = 0; i < res.rows; i++) {
        for (int j = 0; j < res.cols; j++) {
          for (int k = 0; k < cols; k++) {
            res.p[i][j] += p[i][k]*mat.p[k][j];
          }
        }
      }
      return res;
    }
    else {
      cout << "Multiplication is not possible" << endl;
      return mat;
    }
  }
  Matrix operator/(const Matrix &mat) {
    
  }
};