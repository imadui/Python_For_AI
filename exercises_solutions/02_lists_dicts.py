# Session 02 exercise

from configparser import Error


users = [
    {"name": "Imad", "skills": ["Python", "RPA"], "active": True},
    {"name": "Sara", "skills": ["UiPath"], "active": False},
]

# TODO 1: add "AI" to Imad's skills.
users[0]["skills"].append("AI")

print(users)

# TODO 2: add a new user:
# {"name": "Ali", "skills": ["Python", "FastAPI"], "active": True}

new_user = {"name": "Ali", "skills": ["Python", "FastAPI"], "active": True}

users.append(new_user)

print(users)



# TODO 3: print Sara's first skill.
users[1]["skills"][0]

# TODO 4: safely read the missing "company" key from Imad.
# Return "unknown" instead of raising KeyError.

try:
    print(users[0]["Company"])
except KeyError as exception:
    print(f"unknown error: {exception}")


# TODO 5: loop through users and print:
# Imad -> 3 skills
# Sara -> 1 skills
# Ali -> 2 skills

for user in users:
    print(f"{user['name']} -> {len(user['skills'])} skills")
