#include <iostream>
using namespace std;

class Matrix {
protected:
  int val[3][3];

public:
  void show();
  void read();
};

void Matrix::read() {
  cout<<"Enter values for the matrix: "<<endl;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << "[" << i << "][" << j << "]: ";
      cin>>val[i][j];
    }
  }
}

void Matrix::show() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout<<val[i][j]<<" ";
    }
    cout<<endl;
  }
}

class MatrixA : public Matrix {
public:
  void show();
};

void MatrixA::show() {
  Matrix::show();
}

class MatrixB : public MatrixA {
public:
  void show();
};

void MatrixB::show() {
  MatrixA::show();
}

int main() {
  Matrix m1;
  MatrixA m2;
  MatrixB m3;

  cout << "For m1: " << endl;
  m1.read();

  cout << "For m2: " << endl;
  m2.read();

  cout << "For m3: " << endl;
  m3.read();

  cout << endl << "m1: "<<endl;
  m1.show();

  cout << endl << "m2: " << endl;
  m2.show();

  cout << endl << "m3: " << endl;
  m3.show();

  return 0;
}