#include <reg51.h>

void delay() {
    int i, j;
    for(i = 0; i< 1275; i++){
        for(j = 0; j < 100; j++);
    }
}

void main(void) {
    int i;
    P1 = 9;
    P2 = 9;
    delay();
    
    for(i = 1; i < 3; i++){
        P1 = (1<<i)+8;
        delay();
    }

    while(1) {
        for(i = 1; i < 3; i++){
            P1 = (4>>i)+8;
            P2 = (1<<i)+8;
            delay();
        }
        for(i = 1; i < 3; i++){
            P2 = (4>>i)+(8<<i);
            delay();
        }
        for(i = 1; i < 3; i++){
            P1 = (8<<i)+1;
            P2 = (32>>i)+1;
            delay();
        }
        for(i = 1; i < 3; i++){
            P1 = (1<<i)+(32>>i);
            delay();
        }
    }
}