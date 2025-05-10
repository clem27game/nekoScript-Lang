import os
import sys
from antlr4 import *
from nekoScriptLexer import nekoScriptLexer
from nekoScriptParser import nekoScriptParser
from nekoScriptVisitor import nekoScriptVisitor

variables = {}

class NekoInterpreter(nekoScriptVisitor):
    def visitAffectation(self, ctx):
        identifiant = ctx.IDENTIFIANT().getText()
        valeur = self.visit(ctx.valeur())  
        variables[identifiant] = valeur
        print(f"Affectation: {identifiant} = {valeur}")
        return None

    def visitAppelFonction(self, ctx):
        fonction = ctx.IDENTIFIANT().getText()
        if fonction == "nekAfficher":
            param = self.visit(ctx.parametre())
            print(f"Affichage: {param}")
        return None

    def visitValeur(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.IDENTIFIANT():
            identifiant = ctx.IDENTIFIANT().getText()
            if identifiant in variables:
                return variables[identifiant]
            else:
                print(f"Erreur: variable {identifiant} non définie.")
                return None
        return None

def execute_neko_file(file_path):
    input_stream = FileStream(file_path)
    lexer = nekoScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = nekoScriptParser(stream)
    tree = parser.script()
    visitor = NekoInterpreter()
    visitor.visit(tree)

def execute_all_neko_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".neko"):
            print(f"Exécution du fichier: {filename}")
            execute_neko_file(os.path.join(directory, filename))

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = '.'  # Répertoire courant par défaut
    
    execute_all_neko_files_in_directory(directory)

if __name__ == '__main__':
    main()
    