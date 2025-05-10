
import os
import sys
import shutil
from antlr4 import *
from nekoScriptLexer import nekoScriptLexer
from nekoScriptParser import nekoScriptParser
from nekoScriptVisitor import nekoScriptVisitor

variables = {}
package_dir = os.path.expanduser("~/.nekoScript/packages")

class NekoInterpreter(nekoScriptVisitor):
    def visitScript(self, ctx):
        results = []
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                results.append(result)
        return results

    def visitAffectation(self, ctx):
        try:
            identifiant = ctx.IDENTIFIANT().getText()
            valeur = self.visit(ctx.valeur())
            variables[identifiant] = valeur
            return valeur
        except Exception as e:
            print(f"Erreur d'affectation: {str(e)}")
            return None

    def visitOperation(self, ctx):
        try:
            val1 = self.visit(ctx.valeur(0))
            val2 = self.visit(ctx.valeur(1))
            operateur = ctx.operateur().getText()

            if val1 is None or val2 is None:
                raise ValueError("Valeurs invalides pour l'opération")

            val1, val2 = float(val1), float(val2)
            
            if operateur == 'plus':
                return val1 + val2
            elif operateur == 'moins':
                return val1 - val2
            elif operateur == 'multiplier':
                return val1 * val2
            elif operateur == 'diviser':
                if val2 == 0:
                    raise ValueError("Division par zéro")
                return val1 / val2
            else:
                raise ValueError(f"Opérateur inconnu: {operateur}")
        except Exception as e:
            print(f"Erreur d'opération: {str(e)}")
            return None

    def visitAppelFonction(self, ctx):
        try:
            fonction = ctx.IDENTIFIANT().getText()
            params = []
            for param in ctx.valeur():
                val = self.visit(param)
                if val is not None:
                    params.append(val)

            if fonction == "nekAfficher":
                if params:
                    print(*params)
                    return params[0]
                else:
                    print()
                    return None
            else:
                raise ValueError(f"Fonction inconnue: {fonction}")
        except Exception as e:
            print(f"Erreur d'appel de fonction: {str(e)}")
            return None

    def visitValeur(self, ctx):
        try:
            if ctx.STRING():
                return ctx.STRING().getText().strip('"')
            elif ctx.INT():
                return float(ctx.INT().getText())
            elif ctx.IDENTIFIANT():
                ident = ctx.IDENTIFIANT().getText()
                if ident in variables:
                    return variables[ident]
                raise ValueError(f"Variable non définie: {ident}")
            return None
        except Exception as e:
            print(f"Erreur de valeur: {str(e)}")
            return None

def execute_neko_file(file_path):
    if not os.path.exists(file_path):
        print(f"Erreur: Fichier {file_path} non trouvé")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        input_stream = InputStream(code)
        lexer = nekoScriptLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = nekoScriptParser(stream)
        tree = parser.script()
        
        interpreter = NekoInterpreter()
        return interpreter.visit(tree)
    except Exception as e:
        print(f"Erreur d'exécution: {str(e)}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: neko-script <commande> <fichier>")
        print("Commandes disponibles: execute, publish, librairie")
        return

    command = sys.argv[1]
    if command == "execute" and len(sys.argv) == 3:
        execute_neko_file(sys.argv[2])
    elif command == "publish" and len(sys.argv) == 3:
        publish_package(sys.argv[2])
    elif command == "librairie" and len(sys.argv) == 3:
        download_package(sys.argv[2])
    else:
        print("Commande invalide ou arguments manquants")

def publish_package(package_path):
    if not os.path.exists(package_path):
        print(f"Erreur: Package {package_path} non trouvé")
        return
    
    try:
        os.makedirs(package_dir, exist_ok=True)
        dest_path = os.path.join(package_dir, os.path.basename(package_path))
        shutil.copy2(package_path, dest_path)
        print(f"Package {package_path} publié avec succès!")
    except Exception as e:
        print(f"Erreur de publication: {str(e)}")

def download_package(package_name):
    package_path = os.path.join(package_dir, package_name)
    if not os.path.exists(package_path):
        print(f"Erreur: Package {package_name} non trouvé")
        return
    
    try:
        shutil.copy2(package_path, os.path.basename(package_name))
        print(f"Package {package_name} téléchargé avec succès!")
    except Exception as e:
        print(f"Erreur de téléchargement: {str(e)}")

if __name__ == '__main__':
    main()
