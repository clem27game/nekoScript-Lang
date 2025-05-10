#!/bin/bash

# Étape 1 : Installer les dépendances Python
echo "Installation des dépendances Python..."
python3 -m pip install antlr4-python3-runtime

# Étape 2 : Créer le répertoire d'installation
INSTALL_DIR="$HOME/.nekoScript"
mkdir -p "$INSTALL_DIR"

# Étape 3 : Copier les fichiers nécessaires depuis le dossier local
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

python3 "$NEKO_HOME/nekoScriptInterpreter.py" "$@"
EOF

# Étape 5 : Donner les droits d'exécution
chmod +x "$SCRIPT_PATH"

echo "Installation terminée ! Vous pouvez maintenant utiliser nekoScript avec la commande 'neko-script'"