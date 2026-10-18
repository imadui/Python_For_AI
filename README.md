# Python Basics For Beginners

A concise, practice-first Python fundamentals course designed to build the Python skills that matter most before moving into backend, API, automation, and AI engineering.

Repository: `imadui/Python-Basics-For-Beginners`

## Philosophy

Do not study Python as a list of features.

For every session:

1. Read the short session note.
2. Type the examples yourself.
3. Complete the small exercise.
4. Do the challenge without looking at the solution.
5. Run the code and explain why it works.
6. Only then compare with `solutions/`.

If you can complete a session challenge without help and explain your code, move on.

## What to master vs. what to only recognize

### Master
- Variables, basic types, `None`, truthiness
- f-strings
- Lists
- Dictionaries
- Nested `list[dict]` / `dict[list]` structures
- Conditionals and loops
- `enumerate`, `zip`
- List and dict comprehensions
- Functions, parameters, return values
- Type hints
- Specific exception handling
- Files with `pathlib`
- JSON serialization/deserialization
- Modules and imports
- Basic classes and composition
- HTTP APIs with `requests`
- Small tests with `pytest`

### Recognize, but do not over-study yet
- Tuples
- Sets
- `*args` / `**kwargs`
- Inheritance
- Decorators
- Generators
- Advanced packaging
- NumPy arrays

## Why no "arrays" session?

In everyday Python application code, `list` is the general-purpose sequence you will use most often.

```python
users = ["Imad", "Sara", "Ali"]
```

A `tuple` is not an array replacement; it is an immutable sequence.

```python
coordinates = (33.57, -7.59)
```

True typed arrays exist (`array`, NumPy arrays), but they are more relevant to numerical computing, data science, and ML. They are intentionally deferred here.

## Course map

| Session | Focus | Target time |
|---|---|---:|
| 01 | Core syntax, values, types, f-strings | 30–40 min |
| 02 | Lists + dictionaries + nested data | 60 min |
| 03 | Conditionals, loops, comprehensions | 45–60 min |
| 04 | Functions + type hints | 60 min |
| 05 | Exceptions + files + JSON | 60 min |
| 06 | Modules + classes + composition | 60 min |
| 07 | HTTP APIs + JSON responses | 60 min |
| 08 | pytest + final integration challenge | 60–90 min |

Approximate total: **7–8 focused hours**, not weeks.

## Start

Run the diagnostic first:

```powershell
learning python .\exercises\00_diagnostic.py
```

Then open:

`docs/START_HERE.md`

## Useful commands

```powershell
learning python .\exercises\01_core.py
learning python .\challenges\01_profile_card.py
learning python -m pytest
learning python -m ruff check .
```

## Dependency setup

The existing project `.venv` should be reused:

```powershell
learning pip install -r requirements.txt
learning pip check
```

If the `learning` launcher is unavailable:

```powershell
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

## Rule for AI assistance

Try first.

Use AI for:
- hints,
- explaining an error,
- reviewing your solution,
- proposing tests.

Do not ask AI to solve a challenge before you have made a real attempt.

## License

MIT
