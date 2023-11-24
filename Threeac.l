LEX



%{
#include <stdio.h>
#include "y.tab.h"
#include <stdlib.h>
#include <string.h>
%}

%%

[0-9]+ {
    yylval.dval = strdup(yytext); 
    return NUM;
}

[ \t] ;
\n { return 0; }  

. { return yytext[0]; } 

%%

int yywrap() {
    return 1;
}
