"""Challenge 07 — API users."""

import requests

URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(url: str) -> list[dict]:
    # TODO:
    # requests.get(..., timeout=10)
    # raise_for_status()
    # response.json()
    raise NotImplementedError


def summarize_users(users: list[dict]) -> list[dict]:
    # Return ONLY:
    # [
    #   {"name": "...", "email": "...", "city": "..."},
    #   ...
    # ]
    #
    # City is nested under:
    # user["address"]["city"]
    raise NotImplementedError


def main() -> None:
    try:
        users = fetch_users(URL)
        for user in summarize_users(users):
            print(f"{user['name']} | {user['email']} | {user['city']}")
    except requests.RequestException as exc:
        print(f"API error: {exc}")


if __name__ == "__main__":
    main()
