
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
        try:
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
        except ValueError:
            print(f"Erreur: Opération invalide avec {val1} et {val2}")
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

    def visitTerminalCommand(self, ctx):
        command = ctx.STRING().getText().strip('"')
        if command.startswith("neko-script"):
            parts = command.split()
            if len(parts) >= 2:
                action = parts[1]
                if action == "execute":
                    if len(parts) == 3:
                        execute_neko_file(parts[2])
                    else:
                        print("Usage: neko-script execute <fichier>")
                elif action == "publish":
                    print("Publication du package...")
                elif action == "librairie":
                    print("Téléchargement de la librairie...")
                else:
                    print(f"Commande inconnue: {action}")
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

def execute_neko_file(file_path):
    try:
        input_stream = FileStream(file_path, encoding='utf-8')
        lexer = nekoScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = nekoScriptParser(stream)
        tree = parser.script()
    
        interpreter = NekoInterpreter()
        interpreter.visit(tree)
    except Exception as e:
        print(f"Erreur lors de l'exécution: {str(e)}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "execute":
        print("Usage: neko-script execute <fichier.neko>")
        return

    execute_neko_file(sys.argv[2])

if __name__ == '__main__':
    main()
