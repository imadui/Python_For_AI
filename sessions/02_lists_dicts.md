# Session 02 — Lists + Dictionaries

Target: **60 minutes**

This is the most important beginner session for API/AI application work.

## Lists — must master

Create:

```python
skills = ["Python", "RPA", "AI"]
```

Access:

```python
skills[0]
skills[-1]
skills[1:3]
```

Modify:

```python
skills.append("FastAPI")
skills.extend(["RAG", "Agents"])
skills.remove("RPA")
```

Membership:

```python
if "Python" in skills:
    ...
```

Iterate:

```python
for skill in skills:
    print(skill)
```

## Dictionaries — must master

Create:

```python
user = {
    "name": "Imad",
    "role": "AI Engineer",
    "active": True,
}
```

Access:

```python
user["name"]
user.get("company")
user.get("company", "unknown")
```

Modify:

```python
user["role"] = "AI Tech Lead"
user["country"] = "Morocco"
```

Iterate:

```python
for key, value in user.items():
    print(f"{key}: {value}")
```

## Nested structures — absolutely master

```python
users = [
    {
        "name": "Imad",
        "skills": ["Python", "AI"],
    },
    {
        "name": "Sara",
        "skills": ["UiPath", "RPA"],
    },
]

print(users[0]["skills"][1])
```

Be comfortable reading expressions such as:

```python
response["data"]["users"][0]["skills"]
```

## Mutation awareness

Assignment can point to the same list:

```python
a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
```

Simple copy:

```python
b = a.copy()
```

You only need to understand the concept now; deep-copy edge cases can wait.

## Tuple — recognize

```python
point = (10, 20)
```

Ordered and immutable.

## Set — recognize

```python
unique_ids = {1, 2, 3}
```

Useful for uniqueness and membership.

## Arrays

Do not stop here for arrays. For application Python, `list` is your main general-purpose sequence.

NumPy arrays come later when numerical/ML workloads require them.

## Exercise

```powershell
learning python .\exercises\02_lists_dicts.py
```

## Challenge

`challenges/02_user_directory.py`

If you can solve it without opening the solution, move on.
