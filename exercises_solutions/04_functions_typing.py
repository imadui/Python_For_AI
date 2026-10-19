# Session 04 exercise

users = [
    {"name": "Imad", "skills": ["Python", "AI"], "active": True},
    {"name": "Sara", "skills": ["UiPath"], "active": False},
    {"name": "Ali", "skills": ["Python", "FastAPI"], "active": True},
]


# TODO: add type hints and implement.
def active_user_names(users: list[dict]) -> list[str]:
    active_user_names = []
    for user in users:
        if not user["active"]:
            continue
        active_user_names.append(user["name"])
    return active_user_names


# TODO: add type hints and implement.
def users_with_skill(users: list[dict], skill: str) -> list[str]:
    skilled = []
    for user in users:
        if skill in user["skills"]:
            skilled.append(user["name"])
    return skilled



# TODO: add type hints and implement.
# Return a NEW dictionary; do not mutate the original user.
def add_skill(user: [dict], skill: [str]) -> [dict]:
    new_user = user.copy()
    new_user["skills"] = user["skills"].copy()
    new_user["skills"].append(skill)
    return new_user

new_user = add_skill(users[2], "rust")

print(new_user)

print(users[2])


# TODO: call each function and print its RETURN VALUE.
