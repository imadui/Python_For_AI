import requests


def fetch_users(url: str) -> list[dict]:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def summarize_users(users: list[dict]) -> list[dict]:
    return [
        {
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
        }
        for user in users
    ]
