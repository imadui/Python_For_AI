# Session 04 — Functions + Type Hints

Target: **60 minutes**

## Must master

- `def`
- parameters
- positional vs keyword arguments
- defaults
- `return`
- functions that return data instead of printing
- type hints
- decomposition into small functions
- local scope

## Function

```python
def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Call:

```python
name = full_name("Imad", "Berjamy")
```

Keyword arguments:

```python
name = full_name(
    first_name="Imad",
    last_name="Berjamy",
)
```

Default:

```python
def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix} {name}"
```

## Prefer return over print

Less reusable:

```python
def calculate_total(values):
    print(sum(values))
```

Better:

```python
def calculate_total(values: list[float]) -> float:
    return sum(values)
```

Then the caller decides what to do:

```python
total = calculate_total([10.0, 20.0])
print(total)
```

## Type hints

```python
def active_user_names(users: list[dict]) -> list[str]:
    ...
```

Hints improve:
- readability,
- editor support,
- static analysis,
- API/model design later.

They do not automatically enforce runtime types.

## Recognize only

You should recognize:

```python
def example(*args, **kwargs):
    ...
```

Do not spend much time on them yet.

## Exercise

```powershell
learning python .\exercises\04_functions_typing.py
```

## Challenge

`challenges/04_transform_users.py`
