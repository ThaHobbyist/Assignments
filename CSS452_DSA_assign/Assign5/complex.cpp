#include <iostream>
using namespace std;

class Complex {
private:
  float real, imag;

public:
  Complex(float r = 0, float i = 0) {
    real = r;
    imag = i;
  }

  Complex operator+(Complex const &cmplx) {
    Complex res;
    res.real = real + cmplx.real;
    res.imag = imag + cmplx.imag;
    return res;
  }
  Complex operator-(Complex const &cmplx) {
    Complex res;
    res.real = real - cmplx.real;
    res.imag = imag - cmplx.imag;
    return res;
  }
  Complex operator*(const Complex &cmplx) {
    Complex res;
    res.real = real * (cmplx.real + cmplx.imag);
    res.imag = imag * (cmplx.real + cmplx.imag);
    return res;
  }
  Complex operator !() {
    Complex res;
    res.real = real;
    res.imag = -1 * imag;
    return res;
  }
  Complex operator/(Complex cmplx) {
    Complex res;
    res.real = real;
    res.imag = imag;
    float d = cmplx.real*cmplx.real + cmplx.imag*cmplx.imag;
    res = res * (!cmplx);
    res.real/=d; res.imag/=d;
    return res;
  }
  bool operator==(const Complex &cmplx) {
    Complex res;
    if (res.real == cmplx.real && res.imag == cmplx.real) {
      return true;
    } else {
      return false;
    }
  }
  bool operator!=(Complex cmplx) {
    Complex res;
    if (res.real == cmplx.real && res.imag == cmplx.real) {
      return false;
    } else {
      return true;
    }
  }
  Complex operator=(const Complex &cmplx) {
    Complex res;
    res.real = cmplx.real;
    res.imag = cmplx.imag;
    return res;
  }
  int operator[](int i) {
    if (i == 0)
      return real;
    else if (i == 1)
      return imag;
    else {
      cout << "Index Out of bounds";
      return -1;
    }
  }
  friend istream & operator >> (istream &in,  Complex &cmplx){
    cout << "Enter Real Part ";
    in >> cmplx.real;
    cout << "Enter Imaginary Part ";
    in >> cmplx.imag;
    return in;
  }
  friend ostream &operator<<(ostream &out, const Complex &cmplx) {
    if(cmplx.imag >= 0)
      out << cmplx.real << "+i" << cmplx.imag;
    else
      out << cmplx.real << "-i" << -cmplx.imag;
    return out;
  }
  void show() {
    cout<<endl<<real<<"+i"<<imag<<endl;
  }
};

int main() {
  Complex c1, c2;
  cout << "Enter value of c1: ";
  cin >> c1;
  cout << "Enter value of c2: ";
  cin >> c2;
  cout << "Sum is : " << c1 + c2 << endl;
  cout << "Difference is : " << c1 - c2 << endl;
  cout << "Product is : " << c1 * c2 << endl;
  cout << "Division(c1/c2) is : " << c1 / c2 << endl;
  cout << "Conjugate of c1 is " << !c1 << endl;
  cout << "Conjugate of c2 is " << !c2 << endl;
  cout<<"c1[0] = "<<c1[0]<<", c1[1] = "<<c1[1]<<endl;
}