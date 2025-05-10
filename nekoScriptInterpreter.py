
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
        identifiant = ctx.IDENTIFIANT().getText()
        valeur = self.visit(ctx.valeur())
        variables[identifiant] = valeur
        return valeur

    def visitOperation(self, ctx):
        val1 = self.visit(ctx.valeur(0))
        val2 = self.visit(ctx.valeur(1))
        operateur = ctx.operateur().getText()

        try:
            val1, val2 = float(val1), float(val2)
            if operateur == 'plus':
                return val1 + val2
            elif operateur == 'moins':
                return val1 - val2
            elif operateur == 'multiplier':
                return val1 * val2
            elif operateur == 'diviser':
                if val2 != 0:
                    return val1 / val2
                raise ValueError("Division par zéro")
        except (ValueError, TypeError) as e:
            print(f"Erreur d'opération: {str(e)}")
            return None

    def visitAppelFonction(self, ctx):
        fonction = ctx.IDENTIFIANT().getText()
        params = [self.visit(param) for param in ctx.valeur()]
        
        if fonction == "nekAfficher":
            print(*params)
            return params[0] if params else None
        return None

    def visitImportation(self, ctx):
        fichier = ctx.STRING().getText().strip('"')
        if os.path.exists(fichier):
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    code = f.read()
                    input_stream = InputStream(code)
                    lexer = nekoScriptLexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    parser = nekoScriptParser(stream)
                    tree = parser.script()
                    return self.visit(tree)
            except Exception as e:
                print(f"Erreur d'importation: {str(e)}")
        else:
            print(f"Fichier non trouvé: {fichier}")
        return None

    def visitPackageDeclaration(self, ctx):
        package_name = ctx.IDENTIFIANT().getText()
        self.current_package = package_name
        return self.visitChildren(ctx)

    def visitAppelExterne(self, ctx):
        type_appel = ctx.IDENTIFIANT().getText()
        fichier = ctx.STRING().getText().strip('"')

        if type_appel == "nekAppelerJs":
            try:
                import subprocess
                process = subprocess.run(['node', fichier], 
                                      capture_output=True, 
                                      text=True, 
                                      check=True)
                if process.stdout:
                    print(process.stdout.strip())
                return process.stdout.strip()
            except subprocess.CalledProcessError as e:
                print(f"Erreur JavaScript: {e.stderr}")
            except Exception as e:
                print(f"Erreur d'exécution: {str(e)}")
        return None

    def visitValeur(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return float(ctx.INT().getText())
        elif ctx.IDENTIFIANT():
            return variables.get(ctx.IDENTIFIANT().getText())
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
        print("Usage: neko-script <command> <file>")
        print("Commands: execute, publish, librairie")
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
