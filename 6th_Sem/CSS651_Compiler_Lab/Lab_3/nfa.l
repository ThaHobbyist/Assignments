%{
    //#include<stdio.h>
%}

%s A B C DEAD

%%
<INITIAL>[a] BEGIN A; {printf("Got a, moving to A state...\n");}
<INITIAL>[b] BEGIN DEAD; {printf("Not Accepted, Moving to DEAD state... \n");}
<INITIAL>[\n] BEGIN INITIAL; {printf("Empty string...\n");}
<A>[b] BEGIN B; {printf("Got b, moving to B state...\n");}
<A>[a] BEGIN DEAD; {printf("Not Accepted, Moving to DEAD state... \n");}
<A>[\n] BEGIN INITIAL; {printf("Not Accepted \n");}
<B>[a] BEGIN C; {printf("Got a, moving to C state...\n");}
<B>[b] BEGIN DEAD; {printf("Not Accepted, Moving to DEAD state... \n");}
<B>[\n] BEGIN INITIAL; {printf("Not Accepted\n");}
<C>[a] BEGIN C; {printf("Got a, moving to C state...\n");}
<C>[\n] BEGIN INITIAL; {printf("Accepted \n");}
<C>[b] BEGIN DEAD; {printf("Not Accepted, Moving to DEAD state... \n");}
<DEAD>[\n] BEGIN INITIAL; {printf("Moving to INITIAL State...\n");}
%%

int main(){
    yylex();
}
