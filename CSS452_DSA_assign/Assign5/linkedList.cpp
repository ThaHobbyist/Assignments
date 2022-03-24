#include <iostream>
using namespace std;
class Node
{
 
public:
   int data;
   Node *next_link;
   static Node *avail;
   Node(int, Node *);
   Node(const Node &);
   void *operator new(size_t size);
   void operator delete(void *p);
   void display();
};
 
Node::Node(int x = 0, Node *nd = NULL)
{
 
   data = x;
   next_link = nd;
}
 
Node::Node(const Node &nd)
{
   data = nd.data;
   next_link = nd.next_link;
}
 
void *Node::operator new(size_t size)
{
   void *p;
   if (avail == NULL)
   {
       p = ::operator new(size);
   }
   else
   {
       p = avail;
       avail = avail->next_link;
   }
   return p;
}
 
void Node::operator delete(void *p)
{
   Node *t = (Node *)p;
   t->next_link = avail;
   t->data = 0;
   avail = t;
   return;
}
 
Node *Node::avail = NULL;
 
void Node::display()
{
   cout << data;
}
 
class list
{
private:
   Node head;
   static list lstat;
 
public:
   list()
   {
       head.data = 0;
       head.next_link = NULL;
   }
   list(const list &ll)
   {
       head.data = ll.head.data;
       Node *p = ll.head.next_link;
       if (p == NULL)
       {
           head.next_link = NULL;
       }
       else
       {
           Node *q = &head;
           while (p != NULL)
           {
               Node *temp = new Node(p->data);
               q->next_link = temp;
               q = q->next_link;
               p = p->next_link;
           }
       }
   }
   ~list(){
       Node *p = head.next_link;
       while (p != NULL)
       {
           Node *temp = p;
           p = p->next_link;
           delete temp;
       }
       head.data = 0;
   }
 
   list &operator+(const list &ll){
       static list lstat;
       lstat.~list();
       lstat = *this;
       Node *p = &lstat.head;
       while (p->next_link != NULL)
       {
           p = p->next_link;
       }
 
       Node *q = ll.head.next_link;
       while (q != NULL)
       {
           p->next_link = new Node(q->data);
           q = q->next_link;
           p = p->next_link;
       }
       lstat.head.data = head.data + ll.head.data;
       return lstat;
   }
   list &operator!(){
       if (head.data < 2)
       {
           return *this;
       }
       static list lstat;
       lstat.~list();
       lstat.head.data = head.data;
       Node *p = head.next_link;
 
       while (p != NULL)
       {
           lstat.head.next_link = new Node(p->data, lstat.head.next_link);
           p = p->next_link;
       }
       return lstat;
   }
   bool operator==(const list &ll){
       if (this == &ll)
       {
           return true;
       }
       if (head.data != ll.head.data)
       {
           return false;
       }
       Node *p = head.next_link;
       Node *q = ll.head.next_link;
       while (p != NULL)
       {
           if (p->data != q->data)
           {
               return false;
           }
           p = p->next_link;
           q = q->next_link;
       }
       return true;
   }
   list &operator=(const list &ll){
       if (this == &ll)
       {
           return *this;
       }
       this->~list();
       this->head.data = ll.head.data;
       Node *p = &(this->head);
       Node *q = ll.head.next_link;
       while (q != NULL)
       {
           p->next_link = new Node(q->data);
           p = p->next_link;
           q = q->next_link;
       }
       return *this;   
   }
   int operator[](int index){
       if (index >= head.data)
       {
           return -1e5;
       }
       Node *p = head.next_link;
       int i = 0;
       while (p != NULL)
       {
           if (i == index)
           {
               return p->data;
           }
           i++;
           p = p->next_link;
       }
       return 1e-5;
   }
 
   friend ostream &operator<<(ostream &os, list &ll){
       Node *p = &(ll.head);
       p = p->next_link;
       while (p != NULL)
       {
           p->display();
           os << "-->";
           p = p->next_link;
       }
       os << "NULL\n";
       return os;
   }  
   friend istream &operator>>(istream &is, list &ll){
       cout << "Enter no. of nodes: ";
       is >> ll.head.data;
       Node *p = &ll.head;
       while (p->next_link != NULL)
       {
           p = p->next_link;
       }
       for (int i = 0; i < ll.head.data; i++)
       {
           Node *temp = new Node();
           is >> temp->data;
           p->next_link = temp;
           p = p->next_link;
       }
       return is;
   }
};
 
int main(void)
{
   list l1;
   cin >> l1;
   list l2;
   cin >> l2;
   cout << "List 1 : " << l1 << endl;
   cout << "List 2 : " << l2 << endl;
   cout << "Concatinating 2 lists :" << l1 + l2 << endl;
   cout << "Reversing the list : " << (!l1) << endl;
   if (l1 == l2)
   {
       cout << "Lists are equal\n";
   }
   else
   {
       cout << "Lists are not equal\n";
   }
   cout << "Index 1 of 1st list is : " << l1[1] << endl;
}
