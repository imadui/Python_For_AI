users = [
    {"name": "Imad", "skills": ["Python", "RPA", "AI"], "active": True},
    {"name": "Sara", "skills": ["UiPath", "Python"], "active": False},
    {"name": "Ali", "skills": ["Python", "FastAPI", "AI"], "active": True},
]

active_names = [user["name"] for user in users if user["active"]]
python_users = [user["name"] for user in users if "Python" in user["skills"]]

skill_counts: dict[str, int] = {}

for user in users:
    for skill in user["skills"]:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1

print(active_names)
print(python_users)
print(skill_counts)
