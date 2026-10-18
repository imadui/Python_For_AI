# Python ↔ JSON Mental Model

Memorize this mapping:

| JSON | Python |
|---|---|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` / `float` |
| boolean | `bool` |
| null | `None` |

Example JSON:

```json
{
  "name": "Imad",
  "skills": ["Python", "AI"],
  "active": true
}
```

Equivalent Python:

```python
user = {
    "name": "Imad",
    "skills": ["Python", "AI"],
    "active": True,
}
```

## Serialize

Python → JSON text:

```python
json_text = json.dumps(user)
```

## Deserialize

JSON text → Python:

```python
user = json.loads(json_text)
```

## Files

```python
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent=2)

with open("user.json", encoding="utf-8") as file:
    user = json.load(file)
```

The distinction matters:

- `dump` / `load` → files
- `dumps` / `loads` → strings
