
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
            resultat = float(val1) + float(val2)
        elif operateur == 'moins':
            resultat = float(val1) - float(val2)
        elif operateur == 'multiplier':
            resultat = float(val1) * float(val2)
        elif operateur == 'diviser':
            if float(val2) != 0:
                resultat = float(val1) / float(val2)
            else:
                print("Erreur: Division par zéro")
                return None
                
        variables[identifiant] = resultat
        return None

    def visitAppelFonction(self, ctx):
        fonction = ctx.IDENTIFIANT().getText()
        if fonction == "nekAfficher":
            params = []
            for param in ctx.valeur():
                val = self.visit(param)
                if val is not None:
                    params.append(str(val))
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

    try:
        input_stream = FileStream(sys.argv[1], encoding='utf-8')
        lexer = nekoScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = nekoScriptParser(stream)
        tree = parser.script()
    
        interpreter = NekoInterpreter()
        interpreter.visit(tree)
    except Exception as e:
        print(f"Erreur lors de l'exécution: {str(e)}")

if __name__ == '__main__':
    main()
