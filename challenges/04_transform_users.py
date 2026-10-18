"""Challenge 04 — functions + typing."""

users = [
    {"name": "  imad ", "skills": ["python", "AI"], "active": True},
    {"name": "SARA", "skills": ["UIPATH"], "active": False},
]


def normalize_name(name: str) -> str:
    """Return a stripped, title-cased name."""
    raise NotImplementedError


def normalize_skills(skills: list[str]) -> list[str]:
    """Return normalized skill names."""
    raise NotImplementedError


def normalize_user(user: dict) -> dict:
    """Return a NEW normalized user dictionary."""
    raise NotImplementedError


def normalize_users(users: list[dict]) -> list[dict]:
    """Return normalized users."""
    raise NotImplementedError


# Requirement:
# Do not mutate the original list/dicts.
