#include <iostream>
#include <algorithm>
#include<cstdlib>
using namespace std;

int lcm(int a, int b) {
  return (a*b/__gcd(a,b));
}
class fraction {
private:
  int num, deno;

public:
  fraction() {
    num = deno = 1;
  }
  fraction operator+(const fraction &frac) {
    fraction res;
    res.num = (num * frac.deno) + (deno * frac.num);
    res.deno = deno * frac.deno;
    res.deno = res.deno / __gcd(res.num, res.deno);
    res.num = res.num / __gcd(res.num, res.deno);
    return res;
  }
  fraction operator-(const fraction &frac) {
    fraction res;
    res.num = num * frac.deno - deno * frac.num;
    res.deno = deno * frac.deno;
    res.deno = res.deno / __gcd(res.num, res.deno);
    res.num = res.num / __gcd(res.num, res.deno);
    return res;
  }
  fraction operator*(const fraction &frac) {
    fraction res;
    res.num = num * frac.num;
    res.deno = deno * frac.deno;
    res.deno = res.deno / __gcd(res.num, res.deno);
    res.num = res.num / __gcd(res.num, res.deno);
    return res;
  }
  fraction operator/(const fraction &frac) {
    fraction res;
    res.num = num * frac.deno;
    res.deno = deno * frac.num;
    res.deno = res.deno / __gcd(res.num, res.deno);
    res.num = res.num / __gcd(res.num, res.deno);
    return res;
  }
  fraction operator*() {
    fraction res;
    res.deno = res.deno / __gcd(res.num, res.deno);
    res.num = res.num / __gcd(res.num, res.deno);
    return res;
  }
  bool operator==(const fraction &frac) {
    if (num * (lcm(deno, frac.deno) / deno) ==
        frac.num * (lcm(deno, frac.deno) / frac.deno))
      return true;
    else
     return false;
  }
  bool operator!=(const fraction &frac) {
    if (num * (lcm(deno, frac.deno) / deno) ==
        frac.num * (lcm(deno, frac.deno) / frac.deno))
      return false;
    else
     return true;
  }
  bool operator>(const fraction &frac) {
    if (num * (lcm(deno, frac.deno) / deno) >
        frac.num * (lcm(deno, frac.deno) / frac.deno))
      return true;
    else
     return false;
  }
  bool operator<(const fraction &frac) {
    if (num * (lcm(deno, frac.deno) / deno) >
        frac.num * (lcm(deno, frac.deno) / frac.deno))
      return false;
    else
     return true;
  }
  fraction operator=(const fraction &frac) {
    fraction res;
    res.num = frac.num;
    res.deno = frac.deno;
    return res;
  }
  int operator[](int a) {
    if (a == 0)
      return num;
    else 
     return deno;
  }
  friend istream & operator >> (istream &in,  fraction &frac){
    cout << "Enter Numerator Part ";
    in >> frac.num;
    cout << "Enter Denominator Part ";
    in >> frac.deno;
    return in;
  }
  friend ostream &operator<<(ostream &out, const fraction &frac) {
    if(frac.deno * frac.num >= 0)
      out << frac.num << "/" << frac.deno;
    else
      out << -abs(frac.num) << "/" << abs(frac.deno);
    return out;
  }
};

int main() {
  fraction f1, f2;
  cout << "Enter Fraction 1: " << endl;
  cin >> f1;
  cout << "Enter Fraction 2: " << endl;
  cin >> f2;
  cout << "Sum is : " << f1 + f2 << endl;
  cout << "Difference is : " << f1 - f2 << endl;
  cout << "Product is : " << f1 * f2 << endl;
  cout << "Division(f1/f2) is : " << f1 / f2 << endl;
  cout<<"f1[0] = "<<f1[0]<<", f1[1] = "<<f1[1]<<endl;
  return 0;
}