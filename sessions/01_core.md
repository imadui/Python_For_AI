# Session 01 — Core Syntax, Types, f-strings

Target: **30–40 minutes**

## Must master

- assignment
- `str`, `int`, `float`, `bool`, `None`
- `type()`
- basic conversion: `int()`, `str()`, `float()`
- truthiness
- f-strings
- simple expressions

## Core examples

```python
name = "Imad"
years = 5
active = True

print(f"{name} has {years} years of experience")
```

Expressions can go inside `{}`:

```python
a = 5
b = 7

print(f"Total: {a + b}")
```

Formatting:

```python
price = 12.3456
print(f"Price: {price:.2f}")
```

## Truthiness

These are falsy:

```python
False
None
0
0.0
""
[]
{}
set()
```

Example:

```python
name = ""

if name:
    print(name)
else:
    print("No name")
```

## Do not over-study

Skip deep dives into:
- binary representation
- every string method
- operator trivia

Learn methods when you need them.

## Exercise

Run:

```powershell
learning python .\exercises\01_core.py
```

## Challenge

Build:

`challenges/01_profile_card.py`

You are done when you can produce the requested output using only f-strings and normal Python variables.
