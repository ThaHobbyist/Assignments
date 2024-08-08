#include<stdio.h>
#include<inttypes.h>

int main() {
    uint32_t data;
    uint8_t* cptr;

    data = 1;
    cptr = (uint8_t *)&data;

    if(*cptr == 1) printf("little-endiann \n");
    else if(*cptr == 0) printf("big-endiann \n");
    return 0;
}