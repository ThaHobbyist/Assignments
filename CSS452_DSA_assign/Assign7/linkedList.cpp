#include <iostream>

using namespace std;

template <class T> class List;

template <class T> class Node {
  T data;

public:
  Node *next;
  Node(T);
  ~Node();
  friend List<T>;
};

template <class T> Node<T>::Node(T d) {
  cout << "\n Node constructed: " << d << endl;
  data = d;
  next = NULL;
}

template <class T> Node<T>::~Node() { delete this; }

template <class T> class List {
  Node<T> *head;
  Node<T> *tail;

public:
  List();
  List(const List<T> &);
  ~List();
  void push_back(T);
  void disp();
  void del(T);
  List<T> &insertBeg(T x);
  int search(T);
  List<T> &concat(List<T> &);
};

template <class T> List<T>::List() {
  head = NULL;
  tail = NULL;
}

template <class T> List<T>::List(const List<T> &b) {
  head = tail = NULL;
  Node<T> *p = b.head;
  while (p != NULL) {
    Node<T> *c = new Node<T>((p->data));
    if (head == NULL)
      head = tail = c;
    else {
      tail->next = c;
      tail = c;
    }
    p = p->next;
  }
}

template <class T> List<T>::~List() {
  while (head != NULL) {
    Node<T> *p = head;
    head = head->next;
  }
}

template <class T> void List<T>::push_back(T d) {
  Node<T> *p = new Node<T>(d);
  if (head == NULL) {
    head = p;
    tail = p;
  } else {
    tail->next = p;
    tail = p;
  }
}

template <class T> void List<T>::disp() {
  Node<T> *p = head;
  while (p != NULL) {
    cout << (p->data) << "->";
    p = p->next;
  }
  cout << "NULL" << endl;
}
template <class T> int List<T>::search(T x) {
  int k = 0;
  Node<T> *p = head;
  while (p != NULL) {
    if ((p->data) == x)
      return k;
    k++;
    p = p->next;
  }
  return -1;
}

template <class T> void List<T>::del(T x) {
  Node<T> *prev, *p;
  prev = NULL;
  p = head;
  if (p == NULL) {
    cout << "\n List is empty" << endl;
    return;
  } else {
    bool f = false;
    while (p != NULL) {
      if ((p->data) == x) {
        f = true;
        if (prev != NULL)
          prev->next = p->next;
        else
          head = head->next;
      }
      prev = p;
      p = p->next;
    }
    if (f == false)
      cout << "\n No occurences of " << x << " found" << endl;
    else
      cout << "\n All occurences of " << x << " deleted" << endl;
  }
}

template <class T> List<T> &List<T>::concat(List<T> &b) {
  List c(b);
  if (head == NULL) {
    head = c.head;
  } else {
    tail->next = c.head;
    tail = c.tail;
  }
  return *this;
}

template <class T> List<T> &List<T>::insertBeg(T x) {
  Node<T> *p = new Node<T>(x);
  if (head == NULL) {
    head = tail = p;
  } else {
    p->next = head;
    head = p;
  }
  return *this;
}

int main() {
  List<string> L;
  while (1) {
    cout << "\n Press 1 to push-back values into Linked List";
    cout << "\n Press 2 to insert values at the beginning of the Linked List";
    cout << "\n Press 3 to delete values from the Linked List:";
    cout << "\n Press 4 to concatenate another Linked List with current List";
    cout << "\n Press 5 to search a value in the Linked List";
    cout << "\n Press 6 to display the values in the Linked List";
    cout << "\n Press any other key to exit";
    cout << "\n Enter choice:";
    int c;
    cin >> c;
    if (c == 1) {
      cout << "\n Enter number of nodes you wish to push-back:";
      int n;
      cin >> n;
      cout << "\n Enter the elements:";
      while (n--) {
        string x;
        cin >> x;
        L.push_back(x);
      }
      cout << "\n The list after push-backs:" << endl;
      L.disp();
    } else if (c == 2) {
      string x;
      cout << "\n Enter value to be inserted at the beginning:";
      cin >> x;
      L.insertBeg(x);
    } else if (c == 3) {
      string x;
      cout << "\n Enter the value to be deleted:";
      cin >> x;
      L.del(x);
    } else if (c == 4) {
      cout << "\n Enter number of nodes in the list to be concatenated:";
      int n;
      cin >> n;
      List<string> L2;
      cout << "\n Enter the elements:";
      while (n--) {
        string x;
        cin >> x;
        L2.push_back(x);
      }
      L.concat(L2);
    } else if (c == 5) {
      string x;
      cout << "\n Enter value to be searched:";
      cin >> x;
      int pos = L.search(x);
      if (pos == -1) {
        cout << "\n Element not in list" << endl;
      } else {
        cout << "\n Element found at position: " << pos + 1 << endl;
      }
    } else if (c == 6) {
      L.disp();
    } else {
      break;
    }
  }
  return 0;
}