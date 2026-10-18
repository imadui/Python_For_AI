# Session 06 — Modules + Classes + Composition

Target: **60 minutes**

## Modules — must master

Given:

```text
project/
├── app.py
└── helpers.py
```

`helpers.py`:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

`app.py`:

```python
from helpers import greet

print(greet("Imad"))
```

## Main guard

```python
def main() -> None:
    print("Run application")


if __name__ == "__main__":
    main()
```

Understand why this prevents application code from running automatically when a module is imported.

## Classes — must understand

```python
class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def describe(self) -> str:
        return f"{self.name} - {self.role}"
```

Usage:

```python
user = User("Imad", "AI Engineer")
print(user.describe())
```

## Composition — prioritize

```python
class EmailClient:
    def send(self, message: str) -> None:
        print(message)


class NotificationService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client
```

Composition is more important for your immediate goals than building deep inheritance trees.

## Inheritance — recognize

Know what it is, but do not over-study it yet.

## Dataclasses — optional preview

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    role: str
```

Useful for data-oriented objects. Pydantic comes later.

## Exercise

```powershell
learning python .\exercises\06_modules_oop.py
```

## Challenge

`challenges/06_tool_registry.py`
