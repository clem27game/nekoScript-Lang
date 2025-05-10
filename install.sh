#!/bin/bash

# Vérifier si le dossier "nekoScript-Lang" existe
if [ ! -d "nekoScript-Lang" ]; then
  echo "Le dossier nekoScript-Lang n'existe pas !"
  exit 1
fi

# Accéder au dossier où se trouve le projet
cd nekoScript-Lang

# Étape 1 : Installer les dépendances (si un requirements.txt est présent)
if [ -f "requirements.txt" ]; then
  echo "Installation des dépendances Python..."
  python3 -m pip install -r requirements.txt
fi

# Étape 2 : Donner les droits d'exécution sur les fichiers nécessaires
echo "Attribution des droits d'exécution sur neko-script..."
chmod +x neko-script

# Étape 3 : Ajouter le dossier au PATH (optionnel)
echo "Ajout du chemin de nekoScript-Lang au PATH..."
echo "export PATH=\$PATH:$(pwd)" >> ~/.bashrc

# Étape 4 : Recharger le fichier .bashrc pour appliquer les changements
source ~/.bashrc

echo "Installation terminée ! Vous pouvez maintenant utiliser nekoScript avec la commande 'neko-script'."
