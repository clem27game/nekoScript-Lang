grammar nekoScript;

script        : instruction* EOF;

instruction
    : affectation
    | operation
    | appelFonction
    | importation
    | blocSite
    | packageDeclaration
    | terminalCommand
    | appelExterne
    | commentaire
    ;

affectation
    : IDENTIFIANT '=' '(' valeur ')' ';'?
    ;

operation
    : IDENTIFIANT '=' valeur operateur valeur ';'?
    ;

appelFonction
    : 'nek' IDENTIFIANT '(' (valeur (',' valeur)*)? ')' ';'?
    ;

importation
    : 'nekImporter' '(' STRING ')' ';'?
    ;

blocSite
    : 'neksite.créer' ',' 'script' '{' contenuSite* '}' 
    ;

contenuSite
    : 'contenu' ':' '(' STRING ')' ';'?
    | 'titre' ':' STRING ';'?
    | 'lang' ':' STRING ';'?
    | 'couleur-de-fond' ':' STRING ';'?
    | 'style' '{' styleInstruction* '}'
    | 'script' '{' instruction* '}'
    ;

styleInstruction
    : 'nek' IDENTIFIANT ':' STRING ';'?
    ;

packageDeclaration
    : 'package' IDENTIFIANT '{' packageInstruction* '}' ';'
    ;

packageInstruction
    : 'dep' ':' STRING ';'?
    | 'function' IDENTIFIANT '(' paramList? ')' '{' instruction* '}'
    ;

paramList
    : IDENTIFIANT (',' IDENTIFIANT)*
    ;

terminalCommand
    : '$' 'neko-script' 'publish' STRING ';'
    | '$' 'neko-script' 'librairie' STRING ';'
    | '$' 'neko-script' 'télécharger' STRING ';'
    ;

appelExterne
    : 'nekAppelerJs' '(' STRING ')' ';'
    | 'nekAppelerPython' '(' STRING ')' ';'
    ;

valeur
    : STRING
    | INT
    | IDENTIFIANT
    ;

operateur
    : 'plus'
    | 'moins'
    | 'multiplier'
    | 'diviser'
    ;

commentaire
    : COMMENT
    ;

IDENTIFIANT : [a-zA-Z_àâçéèêëîïôùûüÿ]+ [a-zA-Z0-9_àâçéèêëîïôùûüÿ]* ;
STRING      : '"' (~["\\] | '\\' .)* '"';
INT         : [0-9]+;

COMMENT     : '//' ~[\r\n]* -> skip;
WS          : [ \t\r\n]+ -> skip;
