#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

typedef struct Node {
    char* data;
    struct Node* left;
    struct Node* right;
} Node;

typedef struct Stack {
    int top;
    char* data[MAX_SIZE];
} Stack;

Node* makeNode(char* data, Node* left, Node* right) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->left = left;
    node->right = right;
    return node;
}

Stack* makeStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->top = -1;
    return stack;
}

int isEmpty(Stack* stack) {
    return stack->top == -1;
}

void push(Stack* stack, char* data) {
    stack->data[++stack->top] = data;
}

char* pop(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        exit(EXIT_FAILURE);
    }
    return stack->data[stack->top--];
}

char* peek(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        exit(EXIT_FAILURE);
    }
    return stack->data[stack->top];
}

int isOperand(char symbol) {
    return symbol >= '0' && symbol <= '9';
}

int precedence(char operator) {
    switch (operator) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            printf("Invalid operator!\n");
            exit(EXIT_FAILURE);
    }
}

void infixToPostfix(char* infix, char* postfix) {
    Stack* stack = makeStack();
    int i, j;
    for (i = 0, j = 0; infix[i]; i++) {
        if (isOperand(infix[i])) {
            postfix[j++] = infix[i];
        }
        else if (infix[i] == '+' || infix[i] == '-' || infix[i] == '*' || infix[i] == '/') {
            while (!isEmpty(stack) && precedence(peek(stack)[0]) >= precedence(infix[i])) {
                postfix[j++] = ' ';
                postfix[j++] = pop(stack)[0];
            }
            postfix[j++] = ' ';
            char* op = (char*)malloc(sizeof(char) * 2);
            op[0] = infix[i];
            op[1] = '\0';
            push(stack, op);
        }
    }
    while (!isEmpty(stack)) {
        postfix[j++] = ' ';
        postfix[j++] = pop(stack)[0];
    }
    postfix[j] = '\0';
}

void inorder(Node* node) {
    if (node) {
        inorder(node->left);
        printf("%s", node->data);
        inorder(node->right);
    }
}

int main() {
    char infix[] = "9-4+1";
    char postfix[MAX_SIZE];
    infixToPostfix(infix, postfix);
    printf("Infix expression: %s\n", infix);
    printf("Postfix expression: %s\n", postfix);

    Node* root = makeNode("+", makeNode("-", makeNode("9", NULL, NULL), makeNode("4", NULL, NULL)), makeNode("1", NULL, NULL));
    printf("Annotated parse tree: ");
    inorder(root);
    printf("\n");

    return 0;
}
