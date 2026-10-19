import json  # noqa: F401
from pathlib import Path

output = Path("tmp") / "users.json"
output.parent.mkdir(exist_ok=True)
output.touch()

users = [
    {"name": "Imad", "active": True},
    {"name": "Sara", "active": False},
]

# TODO 1:
# Write users to output as formatted JSON.
#
# EXPLICATIONS :
# - Path("tmp") / "users.json" : construit le chemin relatif du fichier.
# - output.parent : récupère le dossier parent (tmp).
# - mkdir(exist_ok=True) : crée le dossier s'il n'existe pas.
# - touch() : crée un fichier vide s'il n'existe pas (facultatif avec "w").
# - users : liste Python contenant deux dictionnaires.
# - open("w") : ouvre le fichier en écriture et écrase son ancien contenu.
# - with ... as f : gère l'ouverture et la fermeture automatique du fichier.
# - json.dump(users, f) : écrit l'objet Python dans le fichier au format JSON.
# - indent=2 : formate le JSON avec une indentation de 2 espaces.
# - True/False : sont convertis automatiquement en true/false dans le JSON.
# - read_text() : lit le fichier et retourne son contenu sous forme de str.
# - json.load(f) : permettrait de relire le JSON comme objet Python.

with output.open("w") as f:
    json.dump(users, f, indent=2)

output.read_text()



# TODO 2:
# Read the JSON file back into Python.

pythonObject = json.loads(output.read_text())

#OR
with output.open("r") as f:
    pythonObject = json.load(f)

print(python_object)

# TODO 3:
# - raw_age: str : reçoit l'âge sous forme de texte.
# - -> int : indique que la fonction retourne un entier.
# - int(raw_age) : convertit la chaîne en entier.
# - int("abc") : déclenche automatiquement ValueError.
# - raise ValueError : rejette un âge négatif.
# - return : retourne l'entier si tout est correct.

def parse_age(raw_age: str) -> int:
    age = int(raw_age)
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


# TODO 4:
# - for : parcourt les âges à tester.
# - try : exécute la fonction.
# - except ValueError : intercepte les erreurs de conversion
#   ainsi que les âges négatifs.
# - as exc : récupère le message de l'exception.
# - print(parse_age(age)) : affiche l'âge valide.

new_list = ["34", "abc", "-2"]

for age in new_list:
    print(f"Parsing {age}....")
    try:
        print(parse_age(age))
    except ValueError as exc:
        print(exc)