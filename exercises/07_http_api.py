import requests

URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(url: str) -> list[dict]:
    """TODO:
    GET url with timeout=10.
    Raise for bad HTTP status.
    Return response JSON.
    """
    raise NotImplementedError


def extract_names(users: list[dict]) -> list[str]:
    """TODO: return all user names."""
    raise NotImplementedError


if __name__ == "__main__":
    try:
        users = fetch_users(URL)
        print(extract_names(users))
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
