#include <iostream>
using namespace std;

class fraction {
private:
  int num, deno;

public:
  fraction operator+(const fraction &frac) {
    fraction res;
    res.num = num * frac.deno + deno * frac.num;
    res.deno = deno * frac.deno;
    res.deno = gcd(num, deno);
    res.num /= gcd(num, deno);
    return res;
  }
  fraction operator-(const fraction &frac) {
    fraction res;
    res.num = num * frac.deno - deno * frac.num;
    res.deno = deno * frac.deno;
    res.deno = gcd(num, deno);
    res.num /= gcd(num, deno);
    return res;
  }
  fraction operator*(const fraction &frac) {
    fraction res;
    res.num = num * frac.num;
    res.deno = deno * frac.deno;
    res.deno = gcd(num, deno);
    res.num /= gcd(num, deno);
    return res;
  }
  fraction operator/(const fraction &frac) {
    fraction res;
    res.num = num * frac.deno;
    res.deno = deno * frac.num;
    res.deno = gcd(num, deno);
    res.num /= gcd(num, deno);
    return res;
  }
  fraction operator*() {
    fraction res;
    res.deno = gcd(num, deno);
    res.num /= gcd(num, deno);
    return res;
  }
  bool operator==(const fraction &frac) {
    if(num == )
  }
  
  
  
  
};

int main() {
  cout<<gcd(3, 6);
  return 0;
}