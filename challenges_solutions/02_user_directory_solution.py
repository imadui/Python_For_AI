users = [
    {"name": "Imad", "skills": ["Python", "RPA"], "active": True},
    {"name": "Sara", "skills": ["UiPath", "SQL"], "active": False},
    {"name": "Ali", "skills": ["Python", "FastAPI", "AI"], "active": True},
]

users[0]["skills"].append("Agents")

active_names = [user["name"] for user in users if user["active"]]
skill_counts = {user["name"]: len(user["skills"]) for user in users}

for user in users:
    print(f"{user['name']} -> {user.get('company', 'unknown')}")

print(active_names)
print(skill_counts)
print(users[2]["skills"][1])
