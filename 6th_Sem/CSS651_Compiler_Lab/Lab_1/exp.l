%{
    //#include<stdio.h>
    int id = 0, chr = 0, num = 0, op = 0;
%}

%%
[a-zA-Z_] {id++;}
[+*=/-] {op++;}
[0-9] {num++;}
[!@#$%^&()_.,?] {chr++;}

%%
int main(){

    while(yylex());

    printf("Number of Identifiers are %d \n", id);
    printf("Number of Special Characters are %d \n", chr);
    printf("Number of Operators are %d \n", op);
    printf("Number of integers are %d \n", num);
    printf("Number of tokens are %d \n", id+chr+op+num);

    return 0;
}

int yywrap(){
    return 1;
}