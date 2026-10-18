def normalize_name(name: str) -> str:
    return name.strip().title()


def normalize_skills(skills: list[str]) -> list[str]:
    return [skill.strip().title() for skill in skills]


def normalize_user(user: dict) -> dict:
    return {
        **user,
        "name": normalize_name(user["name"]),
        "skills": normalize_skills(user.get("skills", [])),
    }


def normalize_users(users: list[dict]) -> list[dict]:
    return [normalize_user(user) for user in users]
