# Python — Files, Folders, Paths, `.env` & JSON

Fiche pratique : opérations courantes avec `pathlib`, `python-dotenv`, `json` et `shutil`, avec des commentaires courts.

## Préparation

Installer la dépendance une seule fois :

```powershell
python -m pip install python-dotenv
```

Créer un fichier **`.env`** à la racine du projet :

```dotenv
desktop_path=C:\Users\imad.eddine.berjamy\Desktop
```

Ajouter `.env` dans **`.gitignore`** pour éviter de publier des informations sensibles :

```gitignore
.env
```

## Script complet

Les trois variantes de chemin sont présentées au début : activer **une seule** ligne `base = ...`. Le script crée un dossier `Python_Demo` et manipule des fichiers de test à l'intérieur.

```python
# ==========================================================
# PYTHON — FILES, FOLDERS, ENV & JSON
# ==========================================================

from pathlib import Path       # Gestion des fichiers et dossiers
from dotenv import load_dotenv # Chargement du fichier .env
import os                      # Variables d'environnement
import json                    # Conversion JSON
import shutil                  # Copie et déplacement


# ==========================================================
# 1. ENV & PATHS
# ==========================================================

load_dotenv()                                # Charge les variables du .env
desktop = os.getenv("desktop_path")          # Lit desktop_path dans le .env

# Trois façons de définir le dossier principal (choisir UNE ligne) :

# A. Chemin relatif Python : basé sur le dossier de travail courant
# base = Path("Python_Demo")

# B. Chemin Windows écrit directement (r = raw string)
# base = Path(r"C:\Users\imad.eddine.berjamy\Desktop\Python_Demo")

# C. Chemin Windows construit depuis le .env (fr = f-string + raw)
base = Path(fr"{desktop}\Python_Demo")

print(Path.cwd())                            # Affiche le dossier courant
print(base.resolve())                        # Affiche le chemin absolu


# ==========================================================
# 2. FOLDERS — CRÉER & VÉRIFIER
# ==========================================================

base.mkdir(exist_ok=True)                    # Crée le dossier s'il n'existe pas

data = base / "data"                        # Chemin du sous-dossier data
data.mkdir(exist_ok=True)                    # Crée data

archive = base / "archive"                  # Chemin du sous-dossier archive
archive.mkdir(exist_ok=True)                 # Crée archive

print(data.exists())                         # True si le chemin existe
print(data.is_dir())                         # True si c'est un dossier

# Pour créer plusieurs niveaux de dossiers en une fois :
# Path(r"C:\temp\a\b").mkdir(parents=True, exist_ok=True)


# ==========================================================
# 3. FILES — CRÉER & VÉRIFIER
# ==========================================================

file = data / "test.txt"                     # Chemin du fichier
file.touch()                                 # Crée le fichier s'il est absent

print(file.exists())                         # True si le chemin existe
print(file.is_file())                        # True si c'est un fichier


# ==========================================================
# 4. WRITE — OVERWRITE (ÉCRASER)
# ==========================================================

file.write_text("Hello Python\n", encoding="utf-8")
# Remplace tout le contenu du fichier (équivalent au mode "w")

# Alternative avec open :
# with file.open("w", encoding="utf-8") as f:
#     f.write("Hello Python\n")


# ==========================================================
# 5. WRITE — APPEND (AJOUTER À LA FIN)
# ==========================================================

with file.open("a", encoding="utf-8") as f:  # "a" = append
    f.write("New line\n")                    # Ajoute une ligne à la fin
    f.write("Another line\n")                # \n = retour à la ligne


# ==========================================================
# 6. READ — FILE TO TEXT / LIST
# ==========================================================

text = file.read_text(encoding="utf-8")     # Fichier -> str
lines = text.splitlines()                    # Texte -> liste de lignes

print(text)                                  # Affiche le contenu entier
print(lines)                                 # Affiche les lignes en liste

# Alternative : lire ligne par ligne
# with file.open("r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# ==========================================================
# 7. JSON — PYTHON OBJECT <-> JSON STRING
# ==========================================================

user = {                                     # Dictionnaire Python
    "name": "Imad",
    "age": 34,
    "skills": ["Python", "AI"]
}

json_text = json.dumps(user)                 # dict -> chaîne JSON (str)
python_obj = json.loads(json_text)           # Chaîne JSON -> dict

print(json_text)                             # Affiche la chaîne JSON
print(python_obj["name"])                   # Lit la clé "name"


# ==========================================================
# 8. JSON — PYTHON OBJECT <-> JSON FILE
# ==========================================================

json_file = data / "user.json"               # Chemin du fichier JSON

with json_file.open("w", encoding="utf-8") as f:  # Ouvre en écriture
    json.dump(user, f)                       # dict -> fichier JSON

with json_file.open("r", encoding="utf-8") as f:  # Ouvre en lecture
    loaded_user = json.load(f)               # Fichier JSON -> dict

print(loaded_user)                           # Affiche le dictionnaire


# ==========================================================
# 9. COPIER UN FICHIER
# ==========================================================

copy = archive / "test_copy.txt"             # Chemin de la copie
shutil.copy2(file, copy)                     # Copie et conserve l'original


# ==========================================================
# 10. RENOMMER UN FICHIER
# ==========================================================

renamed = archive / "renamed.txt"            # Nouveau nom
copy.rename(renamed)                        # Renomme le fichier


# ==========================================================
# 11. DÉPLACER UN FICHIER
# ==========================================================

destination = data / "renamed.txt"           # Nouvel emplacement
shutil.move(renamed, destination)            # Déplace le fichier


# ==========================================================
# 12. SUPPRIMER UN FICHIER
# ==========================================================

destination.unlink()                        # Supprime le fichier déplacé


# ==========================================================
# 13. MÉMO
# ==========================================================

# PATHS
# r"..."           -> Raw string : conserve les backslashes \
# f"..."           -> Insère des variables
# fr"..."          -> Combine les deux
# Path("a") / "b"  -> Assemble les chemins

# FILES & FOLDERS
# touch()          -> Créer un fichier s'il est absent
# mkdir()          -> Créer un dossier
# exists()         -> Vérifier l'existence d'un chemin
# is_file()        -> Vérifier si c'est un fichier
# is_dir()         -> Vérifier si c'est un dossier
# read_text()      -> Lire tout le texte
# write_text()     -> Écrire en écrasant
# unlink()         -> Supprimer un fichier
# rename()         -> Renommer ou déplacer

# OPEN MODES
# "r" -> Read       : lire
# "w" -> Write      : écraser
# "a" -> Append     : ajouter à la fin
# "x" -> Create     : créer uniquement si absent
# with             : fermer automatiquement le fichier

# JSON
# dumps()          -> Objet Python vers chaîne JSON
# loads()          -> Chaîne JSON vers objet Python
# dump()           -> Objet Python vers fichier JSON
# load()           -> Fichier JSON vers objet Python

# SHUTIL
# copy2()          -> Copier un fichier
# move()           -> Déplacer un fichier

# ENV
# load_dotenv()    -> Charger le .env
# os.getenv()      -> Lire une variable d'environnement
```

## Remarques

- **`Path("Python_Demo")`** est relatif au *dossier de travail courant*, pas forcément au dossier qui contient le script.
- Sous Windows, **`r"C:\..."`** garde les `\` littéraux dans une chaîne écrite directement dans Python. Pour une variable provenant de `.env`, **`fr"{desktop}\Python_Demo"`** permet de combiner interpolation et chemin Windows.
- L'opérateur `/` de `Path` assemble des chemins : sur Windows, `Path` utilise le séparateur Windows.
- **`encoding="utf-8"`** est conservé pour une lecture/écriture de texte fiable sous Windows.
- `mkdir(exist_ok=True)` facilite la réexécution. L'exemple de renommage et déplacement suppose que les destinations ne contiennent pas déjà un fichier du même nom.
