"""Challenge 05 — JSON pipeline."""

import json
from pathlib import Path

INPUT = Path("challenges") / "users_input.json"
OUTPUT = Path("challenges") / "active_users_output.json"


def load_users(path: Path) -> list[dict]:
    raise NotImplementedError


def active_users(users: list[dict]) -> list[dict]:
    raise NotImplementedError


def save_users(path: Path, users: list[dict]) -> None:
    raise NotImplementedError


def main() -> None:
    try:
        users = load_users(INPUT)
        result = active_users(users)
        save_users(OUTPUT, result)
        print(f"Saved {len(result)} active users")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Pipeline failed: {exc}")


if __name__ == "__main__":
    main()
