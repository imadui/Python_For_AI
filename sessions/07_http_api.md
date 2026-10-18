# Session 07 — HTTP APIs + JSON Responses

Target: **60 minutes**

## Must master

- GET request
- query params
- timeout
- status code concept
- `raise_for_status()`
- JSON response
- request exception handling
- transform API data into your own Python structure

## Basic request

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)

response.raise_for_status()

users = response.json()
```

`users` is now normal Python data, usually a `list` / `dict` structure.

## Query params

```python
response = requests.get(
    "https://example.com/search",
    params={"q": "python"},
    timeout=10,
)
```

## Error handling

```python
import requests

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as exc:
    print(f"Request failed: {exc}")
```

## Boundary rule

Keep transport logic separate from transformation logic.

Good:

```python
def fetch_users(url: str) -> list[dict]:
    ...

def extract_names(users: list[dict]) -> list[str]:
    ...
```

This makes your logic easier to test.

## Exercise

```powershell
learning python .\exercises\07_http_api.py
```

## Challenge

`challenges/07_api_users.py`
