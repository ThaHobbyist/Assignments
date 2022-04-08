#include <iostream>
using namespace std;

template <class T> class Node {
  T data;

public:
  Node *next;
  Node(T);
  ~Node();
};

template <class T> Node<T>::Node(T d) {
  cout << "\n Node constructed: " << d << endl;
  data = d;
  next = NULL;
}

template <class T> Node<T>::~Node() { delete this; }

int main(void) {
  Node<int> n(1);
  
}