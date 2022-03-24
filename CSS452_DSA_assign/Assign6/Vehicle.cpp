#include <iostream>
using namespace std;

template <class T> class vehicle {
protected:
  T wheel;

public:
  T speed;
  vehicle(T w = 0, T s = 0) {
    wheel = w;
    speed = s;
  }
  void input();
  void show();
};

template <class T> class truck : public vehicle<T> {
protected:
  T load;

public:
  void input();
  void show();
};

template <class T>class car : public vehicle<T> {
protected:
  T pass;

public:
  void input();
  void show();
  void isFast(truck<T> t);
};

template <class T> void vehicle<T>:: input() {
  cout << "Enter number of wheels: ";
  cin >> wheel;
  cout << "Enter Speed: ";
  cin >> speed;
}

template <class T> void vehicle<T>::show() {
  cout << "Number of wheels in vehicle: " << wheel << endl;
  cout<<"Speed of vehicle: "<<speed<<endl;
}

template <class T> void car<T>::input() {
  vehicle<T>::input();
  cout << "Enter number of passengers: ";
  cin >> pass;
}

template <class T> void car<T>::show() {
  vehicle<T>::show();
  cout<<"Number of passengers in Car is: "<<pass<<endl;
}

template <class T> void car<T>::isFast(truck<T> t) {
  if (vehicle<T>::speed > t.speed) {
    cout<<"faster"<<endl;
  } else if (vehicle<T>::speed < t.speed) {
    cout<<"slower"<<endl;
  } else {
    cout << "same " << endl;
  }
}

template <class T> void truck<T>::input() {
  vehicle<T>::input();
  cout << "Enter maximum load of truck: ";
  cin >> load;
}

template <class T> void truck<T>::show() {
  vehicle<T>::show();
  cout<<"Maximum load of truck is: "<<load<<endl;
}

int main() {
  car<int> c;
  truck<int> t;

  cout<<"For Car: "<<endl;
  c.input();
  
  cout << "For Truck: " << endl;
  t.input();


  c.show();
  t.show();
  c.isFast(t);
  return 0;
}