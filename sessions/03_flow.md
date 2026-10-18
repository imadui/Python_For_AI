# Session 03 — Conditions, Loops, Comprehensions

Target: **45–60 minutes**

## Must master

- `if` / `elif` / `else`
- comparisons
- `and`, `or`, `not`
- `for`
- `range`
- `enumerate`
- `zip`
- `break`, `continue`
- list comprehensions
- dict comprehensions

## Conditions

```python
score = 87

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

## Loop over values

```python
for skill in ["Python", "AI", "RPA"]:
    print(skill)
```

## Index + value

```python
for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")
```

## Pair sequences

```python
names = ["Imad", "Sara"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(name, score)
```

## Comprehensions

Instead of:

```python
active_names = []

for user in users:
    if user["active"]:
        active_names.append(user["name"])
```

Prefer when readable:

```python
active_names = [
    user["name"]
    for user in users
    if user["active"]
]
```

Dict comprehension:

```python
scores_by_name = {
    user["name"]: user["score"]
    for user in users
}
```

## Rule

Comprehensions should improve readability. If they become clever, use a normal loop.

## Exercise

```powershell
learning python .\exercises\03_flow.py
```

## Challenge

`challenges/03_skill_report.py`
