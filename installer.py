import os
import shutil
import sys

# Répertoire d'installation de NekoScript
neko_dir = os.path.expanduser("~/.nekoScript")

# Dossier source contenant les fichiers nécessaires (interpréteur, lexer, parser)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Vérifie si le répertoire d'installation existe déjà, sinon le crée
if not os.path.exists(neko_dir):
    os.makedirs(neko_dir)

# Copier l'interpréteur et les autres fichiers nécessaires dans le répertoire d'installation
shutil.copy(os.path.join(current_dir, "nekoScriptInterpreter.py"), neko_dir)

# Copier les fichiers nécessaires pour lexer, parser, visitor (adapté à ton projet)
shutil.copy(os.path.join(current_dir, "src", "nekoScriptLexer.py"), os.path.join(neko_dir, "nekoScriptLexer.py"))
shutil.copy(os.path.join(current_dir, "src", "nekoScriptParser.py"), os.path.join(neko_dir, "nekoScriptParser.py"))
shutil.copy(os.path.join(current_dir, "src", "nekoScriptVisitor.py"), os.path.join(neko_dir, "nekoScriptVisitor.py"))

# Ajouter un alias global dans le fichier ~/.bashrc (ou fichier similaire selon l'OS)
bashrc_path = os.path.expanduser("~/.bashrc")

# Ajouter l'alias si ce n'est pas déjà fait
with open(bashrc_path, "a") as bashrc:
    bashrc.write(f"\n# Alias pour NekoScript\n")
    bashrc.write(f"alias neko-script='python3 {neko_dir}/nekoScriptInterpreter.py'\n")

print(f"NekoScript a été installé avec succès !")
print(f"Vous pouvez maintenant utiliser la commande '$neko-script' pour exécuter des fichiers .neko.")
