# NekoScript - Guide d'utilisation

Bienvenue dans **NekoScript**, un langage de programmation simple et créatif conçu pour les développeurs qui souhaitent créer des sites web, des jeux ou des bots Discord de manière intuitive. Ce README vous guidera dans l'installation, l'utilisation, et la gestion des fichiers **.neko**.

## Table des matières

1. [Installation de NekoScript](#installation-de-nekoscript)
2. [Exécuter des fichiers .neko](#exécuter-des-fichiers-neko)
3. [Création de votre propre bibliothèque/package](#création-de-votre-propre-bibliothèquepackage)
4. [Téléchargement et gestion des packages](#téléchargement-et-gestion-des-packages)
5. [Exemples de code](#exemples-de-code)

---

## Installation de NekoScript

Suivez les étapes ci-dessous pour installer **NekoScript** sur votre système.

### 1. Cloner le dépôt ou télécharger le code source

Téléchargez les fichiers de NekoScript ou clonez ce dépôt via git.

```bash
git clone https://github.com/clem27game/nekoScript-Lang
cd nekoscript-Lang
```

### 2. Installer NekoScript

Une fois que vous avez téléchargé les fichiers de **NekoScript**, exécutez le script d'installation suivant pour installer **NekoScript** et configurer la commande `neko-script` sur votre machine.

Cloner le repo : git clone https://github.com/clem27game/nekoScript-Lang
Aller dans le dossier : cd nekoScript-Lang
Installer nekoScript : bash install.sh
Utiliser la commande : neko-script télécharger

Ce script fera les choses suivantes :

* Crée un répertoire `~/.nekoScript/` pour stocker les fichiers nécessaires.
* Copie l'interpréteur Python et les autres fichiers nécessaires (lexer, parser, etc.) dans ce répertoire.
* Ajoute un alias à la commande `neko-script` dans votre fichier de configuration (`~/.bashrc` ou autre fichier similaire).

### 3. Recharger votre terminal

Pour que la commande `neko-script` soit reconnue dans votre terminal, rechargez votre fichier de configuration.

```bash
source ~/.bashrc
```

---

## Exécuter des fichiers .neko

Une fois que **NekoScript** est installé, vous pouvez exécuter vos fichiers **.neko** en utilisant la commande `neko-script`.

### 1. Créez un fichier `.neko`

Écrivez votre code **NekoScript** dans un fichier avec l'extension `.neko`, par exemple `mon_script.neko`.

Exemple de code :

```nekoScript
neko = ("Bonjour, monde !");
compteneko = 5 plus 3
nekAfficher(compteneko)
```

### 2. Exécuter votre fichier `.neko`

Ensuite, pour exécuter ce fichier, ouvrez un terminal et lancez la commande suivante :

```bash
$neko-script mon_script.neko
```

Cela exécutera le fichier et affichera les résultats dans la console.

---

## Création de votre propre bibliothèque/package

**NekoScript** vous permet de créer vos propres bibliothèques/packages et de les publier pour les partager avec la communauté.

### Étapes pour créer un package :

1. **Créez un dossier pour votre bibliothèque/package** (par exemple `MonPackage`).
2. **Écrivez le code source de votre bibliothèque** en utilisant **NekoScript** ou dans un autre langage (par exemple, JavaScript, Python, etc.).
3. **Structure de votre package** :

   * Le fichier de bibliothèque doit avoir l'extension `.neko` si vous utilisez NekoScript.
   * Vous pouvez inclure des fichiers supplémentaires pour le support d'autres langages (par exemple, `mon_package.js` pour JavaScript).

### Exemple de fichier `.neko` pour une bibliothèque :

```nekoScript
// mon_package.neko
nekAfficher("Bienvenue dans mon package NekoScript !")
```

### 4. Publier votre bibliothèque

Une fois que votre package est prêt, vous pouvez le publier sur **NekoScript** pour qu'il soit accessible à tous les utilisateurs. Utilisez la commande suivante pour publier :

```bash
$neko-script publish MonPackage.neko
```

Cela téléchargera votre bibliothèque et la mettra à disposition pour les autres utilisateurs de **NekoScript**.

---

## Téléchargement et gestion des packages

Une fois qu'un package est publié, n'importe quel utilisateur peut l'utiliser dans son propre code en le téléchargeant via la commande `neko-script librairie`.

### 1. Télécharger une bibliothèque

Pour télécharger et utiliser un package dans votre propre projet, vous pouvez utiliser la commande suivante :

```bash
$neko-script librairie MonPackage.neko
```

Cela téléchargera la bibliothèque depuis le dépôt **NekoScript**.

### 2. Importer et utiliser le package

Une fois la bibliothèque téléchargée, vous pouvez l'importer et l'utiliser dans votre propre fichier **.neko**.

Exemple :

```nekoScript
nekImporter("MonPackage.neko")

// Utilisation des fonctions ou variables du package
nekAfficher("Le package a été téléchargé et utilisé !")
```

---

## Exemples de code

Voici quelques exemples de code **NekoScript** pour vous aider à démarrer.

### Exemple 1 : Afficher un message

```nekoScript
neko = ("Hello, world!")
nekAfficher(neko)
```

### Exemple 2 : Calculer une somme

```nekoScript
compteneko = 10 plus 5
nekAfficher(compteneko)  # Affiche 15
```

### Exemple 3 : Créer un site avec **NekoScript**

```nekoScript
neksite.créer, script {
    contenu : ("Mon site web")
    titre : "Page d'exemple"
    lang : "fr"
    couleur-de-fond : "#ff5733"
    style {
        nekAfficher("Style personnalisé ici!")
    }
    script {
        neko = ("Bienvenue sur le site")
        nekAfficher(neko)
    }
}
```

---

## Questions fréquentes (FAQ)

### 1. **Comment savoir si l'installation s'est bien passée ?**

Après avoir exécuté le script d'installation, si tout se passe bien, vous devriez voir un message indiquant que **NekoScript** a été installé avec succès. Si vous avez des problèmes, assurez-vous d'avoir rechargé votre terminal avec la commande `source ~/.bashrc`.

### 2. **Je n'arrive pas à utiliser la commande `neko-script` dans mon terminal. Que faire ?**

Vérifiez que l'alias a bien été ajouté à votre fichier `~/.bashrc` et que vous avez rechargé votre terminal. Si vous utilisez un autre shell (par exemple `zsh`), l'alias doit être ajouté au fichier de configuration correspondant (par exemple `~/.zshrc`).

---

## Contributions

N'hésitez pas à contribuer à **NekoScript** en ajoutant de nouvelles fonctionnalités, en améliorant la documentation, ou en créant de nouveaux packages.

Si vous avez des questions ou des problèmes, vous pouvez ouvrir une issue sur notre [dépôt GitHub](https://github.com/votre-utilisateur/nekoscript).


