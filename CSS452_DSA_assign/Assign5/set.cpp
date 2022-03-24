#include <iostream>
#include <vector>
using namespace std;

class Set {
private:
  vector<int> val;

public:
  Set operator+(const Set &s) {
    Set res, tmp;
    tmp.val = val;
    Set t1 = tmp - s;
    res.val.insert(res.val.end(), t1.val.begin(), t1.val.end());
    res.val.insert(res.val.end(), s.val.begin(), s.val.end());
    return res;
  }
  Set operator-(const Set &s) {
    Set res;
    for (int i = 0; i < val.size(); i++) {
      res.val.push_back(val[i]);
      for (int j = 0; j < s.val.size(); j++) {
        if (val[i] == s.val[j]) {
          res.val.pop_back();
          break;
        }
      }
    }
    return res;
  }
  Set operator*(const Set &s) {
    Set res;
    for (int i = 0; i < val.size(); i++) {
      for (int j = 0; j < s.val.size(); j++) {
        if (val[i] == s.val[j]) {
          res.val.push_back(val[i]);
          break;
        }
      }
    }
    return res;
  }
  bool operator<(const Set &s) {
    if (val.size() <= s.val.size()) {
      int count = 0;
      for (int i = 0; i < val.size(); i++) {
        for (int j = 0; j < s.val.size(); j++) {
          if (val[i] == s.val[j]) {
            break;
            count++;
          }
        }
      }
      if (count == val.size())
        return true;
      else
       return false;
    }
    else {
      return false;
    }
  }
  bool operator<=(const Set &s) {
    if (val.size() <= s.val.size()) {
      int count = 0;
      for (int i = 0; i < val.size(); i++) {
        for (int j = 0; j < s.val.size(); j++) {
          if (val[i] == s.val[j]) {
            break;
            count++;
          }
        }
      }
      if (count == val.size())
        return true;
      else
       return false;
    }
    else {
      return false;
    }
  }
  bool operator>(const Set &s) {
    if (val.size() >= s.val.size()) {
      int count = 0;
      for (int i = 0; i < s.val.size(); i++) {
        for (int j = 0; j < val.size(); j++) {
          if (val[j] == s.val[i]) {
            break;
            count++;
          }
        }
      }
      if (count == s.val.size())
        return true;
      else
       return false;
    }
    else {
      return false;
    }
  }
  bool operator>=(const Set &s) {
    if (val.size() >= s.val.size()) {
      int count = 0;
      for (int i = 0; i < s.val.size(); i++) {
        for (int j = 0; j < val.size(); j++) {
          if (val[j] == s.val[i]) {
            break;
            count++;
          }
        }
      }
      if (count == s.val.size())
        return true;
      else
       return false;
    }
    else {
      return false;
    }
  }
  bool operator==(Set &s) {
    if (val == s.val)
      return true;
    else
      return false;
  }
  bool operator!=(Set &s) {
    if (val == s.val) {
      return false;
    } else {
      return true;
    }
  }
  friend istream &operator>>(istream &in, Set &s) {
    int n;
    cout << "Enter Number of elements for the set: ";
    in >> n;
    cout<<"Enter the values: \n";
    for (int i = 0; i < n; i++) {
      int t;
      in >> t;
      s.val.push_back(t);
    }
    return in;
  }
  friend ostream &operator<<(ostream &out, const Set &s) {
    for (int i = 0; i < s.val.size(); i++) {
      out<<s.val[i]<<" ";
    }
    return out;
  }
};

int main() {
  Set s1, s2;
  cout << "Enter values for s1: \n";
  cin >> s1;
  cout << "Enter valus for s2: \n";
  cin >> s2;
  cout << "Union of s1 and s2: " << s1 + s2 << endl;
  cout << "Difference of s1 and s2: " << s1 - s2 << endl;
  cout << "Intersection of s1 and s2: " << s1 * s2 << endl;
  return 0;
}