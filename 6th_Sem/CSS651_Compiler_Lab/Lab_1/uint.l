%{
    //#include<stdio.h>

    int count_num = 0;
    int count_id = 0;
%}

%%
[a-zA-Z_][a-zA-Z0-9_]* {
    count_id++;
    
}
[0-9]* {
    count_num++;
    
}

[!@#$%^&()_.,?0-9-][!@#$%^&()_.,?a-zA-Z0-9_]* {
    printf("invalid identifier or number");
}

%%
int main(){
    
    while(yylex());
        printf("Count of numbers: %d \n", count_num);
        printf("Count of identifiers: %d \n", count_id);
    
    return 0;
}

int yywrap(){
    return 1;
}
