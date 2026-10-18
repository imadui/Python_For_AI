# Python Core Cheat Sheet

## Variables

```python
name = "Imad"
age = 34
active = True
score = 9.5
missing = None
```

## f-strings

```python
print(f"{name} is {age} years old")
print(f"Score: {score:.2f}")
```

## List

```python
skills = ["Python", "RPA"]
skills.append("AI")
skills.extend(["FastAPI", "RAG"])

first = skills[0]
last = skills[-1]
subset = skills[1:3]
```

## Dict

```python
user = {"name": "Imad", "active": True}

name = user["name"]
role = user.get("role", "unknown")

user["role"] = "AI Engineer"

for key, value in user.items():
    print(key, value)
```

## Nested data

```python
users = [
    {"name": "Imad", "skills": ["Python", "AI"]},
    {"name": "Sara", "skills": ["RPA"]},
]

print(users[0]["skills"][1])
```

## Conditions

```python
if score >= 10:
    result = "pass"
elif score >= 8:
    result = "almost"
else:
    result = "retry"
```

## Loops

```python
for index, skill in enumerate(skills, start=1):
    print(index, skill)
```

## Comprehensions

```python
names = [user["name"] for user in users]
active = [user for user in users if user.get("active")]
```

## Functions

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

## Exceptions

```python
try:
    value = int("42")
except ValueError as exc:
    print(f"Invalid number: {exc}")
```

## JSON

```python
import json

text = json.dumps(user)
user_again = json.loads(text)
```

## Files

```python
from pathlib import Path

path = Path("data.json")
path.write_text("hello", encoding="utf-8")
text = path.read_text(encoding="utf-8")
```

## HTTP

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)
response.raise_for_status()
data = response.json()
```
