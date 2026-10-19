# Session 01 exercise

name = "Imad"
role = "AI Engineer"
years = 5
score = 8.756

# TODO: print:
# Imad | AI Engineer | 5 years | score=8.76
# Use ONE f-string.

print(f"{name} | {role} | {years} | {float(score):.2f}")

# TODO: convert this string to int and add 10.
raw_count = "32"
raw_count_int = int(raw_count) + 10

# TODO: predict whether each value is truthy or falsy before running.
values = ["", "Python", 0, 1, [], [1], None, False, True]

for value in values:
    print(repr(value), bool(value))
