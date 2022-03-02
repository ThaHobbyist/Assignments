#include<bits/stdc++.h>
using namespace std;

class Node{
public:
    int data;
    Node* next;
    Node() {
        data = 1;
        next = NULL;
    }

    Node(int x) {
        this->data = x;
        this->next = NULL;
    }
};

class List{
private:
    Node* head;
    int length;

public:
    List() {
      head = NULL;
      length = 0;
    }
    ~List() {
        cout<<"Destructed"<<endl;
    }
    void insert(int pos, int val);
    void insertEnd(int val);
    void del(int pos);
    void display();
    int search(int val);
    void conCat();  

};

void List::insert(int pos, int val) {
  int cnt = 1;
  Node *temp = head;
  Node* newNode = new Node(val);

  if (head == NULL)
    return;

  while (temp->next != NULL && cnt < pos) {
    temp = temp->next;
    cnt++;
  }
  newNode->next = temp->next;
  temp->next = newNode;
  length++;
}

void List::insertEnd(int val) {
  Node *temp = head;
  Node *newNode = new Node(val);

  while (temp->next != NULL) {
    temp = temp->next;
  }
  newNode->next = NULL;
  temp->next = newNode;
  length++;
}

void List::del(int pos) {
  int cnt = 1;
  Node *temp = head;

  if (head == NULL)
    return;

  while (temp->next != NULL && cnt <= pos) {
    if (cnt == pos) {
      Node* temp1 = temp->next;
      temp->next = temp1->next;
      delete temp1;
      length--;
      return;
    }
    temp = temp->next;
    cnt++;
  }
}

void List::display() {
  Node *temp = head;

  if (head == NULL) {
    cout << "List empty" << endl;
    return;
  }
  cout<<"HEAD->";
  while (temp->next != NULL) {
    temp = temp->next;
    cout<<temp->data<<"->";
  }
}

int List::search(int val) {
  Node *temp = head;
  int pos = 1;
  if (head == NULL) {
    cout << "List empty" << endl;
    return -1;
  }

  while (temp->next != NULL) {
    temp = temp->next;
    if (temp->data == val) {
      return pos;
    }
    pos++;
  }
  return -1;
}

int main() {
  List l;
  int c, num, temp;
  bool b = true;
  while (b) {
    cout<<"\n---------OPTIONS----------\n1.Insert Node\n2.Delete Node\n3.Display List\n4.Search a value\n5.Exit\nEnter your choice: "<<endl;
    cin >> c;
    switch (c) {
        case 1:
            cout << "Number of values to insert: ";
            cin >> num;
            for (int i = 0; i < num; i++) {
                cout << "\nEnter a number: ";
                cin >> temp;
                l.insertEnd(temp);
            }
            cout << "\nValues inserted, current list is: ";
            l.display();
            break;
        case 2:
            cout << "Current list is: ";
            int pos;
            l.display();
            cout << "\nEnter position of element you want to delete: ";
            cin >> pos;
            l.del(pos);
            cout << "\nList after deleting the element: ";
            l.display();
            break;
        case 3:
            cout << "The current Linked list is: ";
            l.display();
            break;
        case 4:
          int val;
          cout << "Enter value to search: ";
          cin >> val;
          cout<<val<<" found in "<<l.search(val)<<"th position"<<endl;
          break;
        case 5:
          b = false;
          break;
        default:
            cout << "Enter a valid choice: ";
    }
  }
  return 0;
}