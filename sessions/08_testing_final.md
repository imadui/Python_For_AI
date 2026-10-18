# Session 08 — pytest + Final Integration Challenge

Target: **60–90 minutes**

## Must master

- simple `assert`
- pytest test functions
- arrange → act → assert
- test normal path
- test edge case
- keep business logic testable without network

## Small test

Application:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Test:

```python
def test_add():
    assert add(2, 3) == 5
```

Run:

```powershell
learning python -m pytest
```

## Arrange / Act / Assert

```python
def test_active_user_names():
    # Arrange
    users = [
        {"name": "Imad", "active": True},
        {"name": "Sara", "active": False},
    ]

    # Act
    result = active_user_names(users)

    # Assert
    assert result == ["Imad"]
```

## Final challenge

Complete:

`challenges/final_user_report.py`

Then:

```powershell
learning python -m pytest tests\test_final_user_report.py -v
```

Do not open the solution until the tests pass or you have made a serious attempt.

## Graduation bar

You are ready to move to Pydantic / FastAPI when you can:

- read nested list/dict data without confusion,
- transform it with loops/comprehensions,
- write typed functions,
- serialize JSON,
- handle expected exceptions,
- split code into modules,
- understand a basic class,
- call an API safely,
- write a few tests,
- explain all of the above without AI writing the code for you.
