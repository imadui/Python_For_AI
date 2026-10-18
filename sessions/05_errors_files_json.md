# Session 05 — Exceptions, Files, JSON

Target: **60 minutes**

## Must master

- specific exceptions
- `try` / `except`
- `raise`
- `finally` concept
- `pathlib.Path`
- text read/write
- `with`
- JSON `load`, `loads`, `dump`, `dumps`

## Specific exceptions

Avoid:

```python
try:
    ...
except:
    ...
```

Prefer:

```python
try:
    age = int(raw_age)
except ValueError as exc:
    print(f"Invalid age: {exc}")
```

## Raise when input is invalid

```python
def validate_age(age: int) -> None:
    if age < 0:
        raise ValueError("age cannot be negative")
```

## pathlib

```python
from pathlib import Path

path = Path("data") / "user.json"
```

Read text:

```python
text = path.read_text(encoding="utf-8")
```

Write text:

```python
path.write_text("hello", encoding="utf-8")
```

## JSON

```python
import json

user = {"name": "Imad", "skills": ["Python", "AI"]}

text = json.dumps(user, indent=2)
same_user = json.loads(text)
```

File:

```python
with Path("user.json").open("w", encoding="utf-8") as file:
    json.dump(user, file, indent=2)
```

## Critical distinction

- `dumps` = object → string
- `loads` = string → object
- `dump` = object → file
- `load` = file → object

## Exercise

```powershell
learning python .\exercises\05_errors_files_json.py
```

## Challenge

`challenges/05_json_pipeline.py`
