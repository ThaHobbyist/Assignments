#include <iostream>
using namespace std;

class Node {
public:
  int data;
  Node *next;

  Node() {
    data = 0;
    next = NULL;
  }

  Node(int val) {
    data = val;
    next = NULL;
  }

  ~Node() {
    cout<<"\n destructed"<<endl;
  }
};

class List {
private:
  Node *head;
  int length;

public:
  List() {
    head = new Node();
    length = 0;
  }
  ~List() {
    delete head;
    cout<<"destructed List"<<endl;
  }
  void display() {
    Node *tmp = head;
    while (tmp->next != NULL) {
      tmp = tmp->next;
      cout << tmp->data << "-";
    }
  }
  void insert(int val) {
    cout<<"hello1"<<endl;
    Node *tmp = head;
    cout<<"hello2"<<endl;
    Node *newNode = new Node(val);
    cout << "hello3" << endl;
    int cnt = 0;
    cout<<tmp->next<<endl;
    while (tmp->next != NULL || tmp->next != 0) {
      tmp = tmp->next;
      cout << ++cnt << endl;
    }
    cout<<"hello4"<<endl;
    tmp->next = newNode;
    cout<<"hello5"<<endl;
    length++;
  }
};

int main() {
  List l;
  l.insert(10);
  l.display();
}