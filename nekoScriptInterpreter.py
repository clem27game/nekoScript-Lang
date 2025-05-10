
import os
import sys
from antlr4 import *
from nekoScriptLexer import nekoScriptLexer
from nekoScriptParser import nekoScriptParser
from nekoScriptVisitor import nekoScriptVisitor

variables = {}

class NekoInterpreter(nekoScriptVisitor):
    def visitScript(self, ctx):
        return self.visitChildren(ctx)

    def visitAffectation(self, ctx):
        identifiant = ctx.IDENTIFIANT().getText()
        valeur = self.visit(ctx.valeur())
        variables[identifiant] = valeur
        return None

    def visitOperation(self, ctx):
        identifiant = ctx.IDENTIFIANT().getText()
        val1 = self.visit(ctx.valeur(0))
        val2 = self.visit(ctx.valeur(1))
        operateur = ctx.operateur().getText()
        
        resultat = None
        if operateur == 'plus':
            resultat = val1 + val2
        elif operateur == 'moins':
            resultat = val1 - val2
        elif operateur == 'multiplier':
            resultat = val1 * val2
        elif operateur == 'diviser':
            resultat = val1 / val2 if val2 != 0 else None
            
        if resultat is not None:
            variables[identifiant] = resultat
        return None

    def visitAppelFonction(self, ctx):
        fonction = ctx.IDENTIFIANT().getText()
        if fonction == "Afficher":
            params = []
            for param in ctx.valeur():
                params.append(self.visit(param))
            print(*params)
        return None

    def visitValeur(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.IDENTIFIANT():
            identifiant = ctx.IDENTIFIANT().getText()
            return variables.get(identifiant)
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 nekoScriptInterpreter.py <fichier.neko>")
        return

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = nekoScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = nekoScriptParser(stream)
    tree = parser.script()
    
    interpreter = NekoInterpreter()
    interpreter.visit(tree)

if __name__ == '__main__':
    main()
