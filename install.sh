
#!/bin/bash

# Vérifier si le dossier "nekoScript-Lang" existe
if [ ! -d "nekoScript-Lang" ]; then
  echo "Le dossier nekoScript-Lang n'existe pas !"
  exit 1
fi

# Accéder au dossier où se trouve le projet
cd nekoScript-Lang

# Étape 1 : Installer les dépendances Python
echo "Installation des dépendances Python..."
python3 -m pip install antlr4-python3-runtime

# Étape 2 : Créer le répertoire d'installation
INSTALL_DIR="$HOME/.nekoScript"
mkdir -p "$INSTALL_DIR"

# Étape 3 : Copier les fichiers nécessaires
echo "Copie des fichiers dans $INSTALL_DIR..."
cp nekoScriptInterpreter.py "$INSTALL_DIR/"
cp nekoScriptLexer.py "$INSTALL_DIR/"
cp nekoScriptParser.py "$INSTALL_DIR/"
cp nekoScriptVisitor.py "$INSTALL_DIR/"

# Étape 4 : Créer le script exécutable neko-script
SCRIPT_PATH="/usr/local/bin/neko-script"
echo "Création du script exécutable..."

cat > "$SCRIPT_PATH" << 'EOF'
#!/bin/bash

NEKO_HOME="$HOME/.nekoScript"

case "$1" in
  "télécharger")
    echo "Téléchargement de nekoScript..."
    git clone https://github.com/clem27game/nekoScript-Lang
    cd nekoScript-Lang && bash install.sh
    ;;
  *)
    python3 "$NEKO_HOME/nekoScriptInterpreter.py" "$@"
    ;;
esac
EOF

# Étape 5 : Donner les droits d'exécution
chmod +x "$SCRIPT_PATH"

echo "Installation terminée ! Vous pouvez maintenant utiliser nekoScript avec la commande 'neko-script'"
