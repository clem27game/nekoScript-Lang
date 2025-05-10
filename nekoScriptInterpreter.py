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
            variables[identifiant] = resultat
        except ValueError:
            print(f"Erreur: Opération invalide avec {val1} et {val2}")
            return None
        return None

    def visitAppelFonction(self, ctx):
        fonction = ctx.IDENTIFIANT().getText()
        params = []
        for param in ctx.valeur():
            val = self.visit(param)
            if val is not None:
                params.append(str(val))

        if fonction == "nekAfficher":
            print(*params)
        return None

    def visitImportation(self, ctx):
        fichier = ctx.STRING().getText().strip('"')
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                input_stream = InputStream(f.read())
                interpreter = NekoInterpreter()
                lexer = nekoScriptLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = nekoScriptParser(stream)
                tree = parser.script()
                interpreter.visit(tree)
        except Exception as e:
            print(f"Erreur lors de l'importation: {str(e)}")
        return None

    def visitPackageDeclaration(self, ctx):
        package_name = ctx.IDENTIFIANT().getText()
        print(f"Déclaration du package: {package_name}")
        return self.visitChildren(ctx)

    def visitTerminalCommand(self, ctx):
        try:
            command = sys.argv[1] if len(sys.argv) > 1 else ""
            if command == "publish":
                if len(sys.argv) == 3:
                    self.publish_package(sys.argv[2])
                else:
                    print("Usage: neko-script publish <fichier.neko>")
            elif command == "execute":
                if len(sys.argv) == 3:
                    execute_neko_file(sys.argv[2])
                else:
                    print("Usage: neko-script execute <fichier>")
            elif command == "librairie":
                if len(sys.argv) == 3:
                    self.download_package(sys.argv[2])
                else:
                    print("Usage: neko-script librairie <package>")
        except Exception as e:
            print(f"Erreur lors de l'exécution de la commande: {str(e)}")
        return None

    def publish_package(self, package_path):
        try:
            if os.path.exists(package_path):
                os.makedirs(package_dir, exist_ok=True)
                shutil.copy(package_path, os.path.join(package_dir, os.path.basename(package_path)))
                print(f"Package {package_path} publié avec succès!")
            else:
                print(f"Erreur: Le fichier {package_path} n'existe pas")
        except Exception as e:
            print(f"Erreur lors de la publication: {str(e)}")

    def download_package(self, package_name):
        package_path = os.path.join(package_dir, package_name)
        if os.path.exists(package_path):
            try:
                shutil.copy(package_path, os.path.basename(package_name))
                print(f"Package {package_name} téléchargé avec succès!")
            except Exception as e:
                print(f"Erreur lors du téléchargement: {str(e)}")
        else:
            print(f"Erreur: Le package {package_name} n'existe pas")

    def visitValeur(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.IDENTIFIANT():
            identifiant = ctx.IDENTIFIANT().getText()
            return variables.get(identifiant)
        return None

    def visitAppelExterne(self, ctx:nekoScriptParser.AppelExterneContext):
        type_appel = ctx.IDENTIFIANT().getText()
        fichier = ctx.STRING().getText().strip('"')

        if type_appel == "nekAppelerJs":
            try:
                import subprocess
                result = subprocess.run(['node', fichier], capture_output=True, text=True)
                if result.stdout:
                    print(result.stdout)
                return result.stdout
            except Exception as e:
                print(f"Erreur lors de l'appel JavaScript: {str(e)}")

        elif type_appel == "nekAppelerPython":
            try:
                with open(fichier, 'r') as f:
                    code = f.read()
                    exec(code, globals())
                return None
            except Exception as e:
                print(f"Erreur lors de l'appel Python: {str(e)}")

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
    try:
        if len(sys.argv) < 2:
            print("Usage: neko-script <commande> <fichier>")
            print("Commandes disponibles: execute, publish, librairie")
            return

        interpreter = NekoInterpreter()
        interpreter.visitTerminalCommand(None)
    except Exception as e:
        print(f"Erreur: {str(e)}")

if __name__ == '__main__':
    main()