"""10-minute diagnostic.

Do not use AI or solutions.
If this feels easy, move quickly through Sessions 01 and 02.
"""

users = [
    {"name": "Imad", "skills": ["Python", "RPA"], "active": True},
    {"name": "Sara", "skills": ["UiPath"], "active": False},
    {"name": "Ali", "skills": ["Python", "AI"], "active": True},
]

# TODO 1:
# Create a list containing only the names of active users.

active_users =[]

for user in users:
    if user["active"]:
        active_users.append(user["name"])

print(active_users)
#OR
for active_user in active_users:
    print(active_user)



# TODO 2:
# Create a dictionary where each user name maps to their number of skills.

skills_dict={}

for user in users:
    skills_dict[user["name"]] = len(user["skills"])

print(skills_dict)


# TODO 3:
# Write:
#   def users_with_skill(users: list[dict], skill: str) -> list[str]
# It must return user names containing the requested skill.

def users_with_skill(users: list[dict], skill: str) -> list[str]:
    skilled_people_list = []
    for user in users:
        if skill in user["skills"]:
            skilled_people_list.append(user["name"])
    return skilled_people_list

users_with_skill(users, "Python")

# TODO 4:
# Print this sentence with an f-string:
# "2 active users found"

print(f"{len(active_users)} active users found")

# TODO 5:
# Serialize `users` to JSON text and deserialize it back to Python.

import json

users_text = json.dumps(users)

users_json = json.loads(users_text)

print(users_text)
print(users_json)

print(f"user_text is of type {type(users_text)}, and user_json is of type {type(users_json)}.")


print("Complete the TODOs, then explain every line.")
