import json
from pathlib import Path


def load_users(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def active_users(users: list[dict]) -> list[dict]:
    return [user for user in users if user.get("active", False)]


def save_users(path: Path, users: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)
