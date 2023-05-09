%{
    //#include<stdio.h>
    int key = 0, tk = 0;
%}

%%
[if|else|main] {key++; tk++;}
[a-zA-Z_0-9]* {tk++;}
[==|(){}+*=/-] {tk++;}
%%
int main(){
    yylex();
    printf("\nNo of Keywords: %d", key);
    printf("\nNo of tokens: %d \n", tk);
}