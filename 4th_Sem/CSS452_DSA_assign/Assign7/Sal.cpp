#include <iostream>
#include <iomanip>
using namespace std;

template <class T> class salary {
private:
  T gross, basic;

public:
  static T da;
  const T bonus;

  salary(T);
  ~salary();
  void display(void);
  T get_gross_salary();

  friend float average_gross_sal(salary<int> &x1, salary<int> &x2);
  friend float average_gross_sal(salary<float> &x1, salary<float> &x2);
};

float average_gross_sal(salary<int> &x1, salary<int> &x2) {
  return (x1.get_gross_salary() + x2.get_gross_salary()) / 2;
}
float average_gross_sal(salary<float> &x1, salary<float> &x2) {
  return (x1.get_gross_salary() + x2.get_gross_salary()) / 2;
}

template <class T> salary<T>::salary(T a) : bonus(2000) {
  cout << "constr invoked" << endl;
  gross = basic = a;
}

template <class T> salary<T>::~salary() { cout << "destr invoked" << endl; }

template <class T> T salary<T>::get_gross_salary(void) {
  gross = basic + (basic * da) / 100 + bonus;
  return (gross);
}

template <class T> void salary<T>::display(void) {

  cout << "Salary details::" << endl;
  cout << "BASIC==" << basic << endl;
  cout << "GROSS==" << gross << endl;
}
template <class T> T salary<T>::da = 28;

int main(void) {
  salary<int> s1(40000);
  s1.get_gross_salary();
  s1.display();

  salary<int> s2(65500);
  s2.get_gross_salary();
  s2.display();
  cout << "AVERAGE SALARY==" << average_gross_sal(s1, s2) << endl;

  salary<float> s3(40000.782);
  s3.get_gross_salary();
  s3.display();

  salary<float> s4(65500.232);
  s4.get_gross_salary();
  s4.display();
  cout << "AVERAGE SALARY==" << average_gross_sal(s3, s4) << endl;
}