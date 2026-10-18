import json  # noqa: F401
from pathlib import Path

output = Path("tmp") / "users.json"
output.parent.mkdir(exist_ok=True)

users = [
    {"name": "Imad", "active": True},
    {"name": "Sara", "active": False},
]

# TODO 1:
# Write users to output as formatted JSON.

# TODO 2:
# Read the JSON file back into Python.

# TODO 3:
# Write:
#   def parse_age(raw_age: str) -> int
# Raise ValueError if the age is negative.
# Let int() raise ValueError for invalid text.

# TODO 4:
# Call parse_age with:
# "34"
# "abc"
# "-2"
# Catch ValueError specifically and print a useful message.
