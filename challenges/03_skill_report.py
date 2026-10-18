"""Challenge 03 — skill report."""

users = [
    {"name": "Imad", "skills": ["Python", "RPA", "AI"], "active": True},
    {"name": "Sara", "skills": ["UiPath", "Python"], "active": False},
    {"name": "Ali", "skills": ["Python", "FastAPI", "AI"], "active": True},
]

# Build:
# 1. active_names: list[str]
# 2. python_users: list[str]
# 3. skill_counts: dict[str, int]
#
# Expected skill_counts conceptually:
# Python -> 3
# RPA -> 1
# AI -> 2
# UiPath -> 1
# FastAPI -> 1
#
# At least ONE result must use a comprehension.
# Use normal loops where they are clearer.
