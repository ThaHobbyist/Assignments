#include<iostream>
using namespace std;

template <typename T>
class Stack(){
	private:
		T * date;
		int top;
		int size;

	public:
		stack(const int);
		stack &push(const T);
		stack &pop();
		T peek();
		bool isEmpty();
		bool isFull();
		void display();
		~stack();
}

template<typename T>
stack<T>::stack(const int s){
	size = s;
	data = new T(size);
	top = -1;
}

template<typename T>
stack<T> &stack<T>::push(const T n){
try:
	data[++top] = n;
	return (*this);
catch:
	cout<<"\nError: Overflow";
}

template <typename T>
stack<T> &stack<T>::pop(){
try:
	T temp = data[top];
	data[top--] = T(NULL);
	cout<<">>"<<temp<<" was popped";
	return *this;
catch:
	cout<<"Error: Underflow";
}

template<typename T>
stack<T> &stack::peek(){
try:
	return data[top];
}
