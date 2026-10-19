# Session 03 exercise

users = [
    {"name": "Imad", "score": 95, "active": True},
    {"name": "Sara", "score": 72, "active": False},
    {"name": "Ali", "score": 88, "active": True},
]

# TODO 1: normal loop -> collect active user names.

for user in users:
    if user["active"]:
        print(user["name"])

# TODO 2: write the same transformation using a list comprehension.

# TODO 3: create a dict:
# {"Imad": "excellent", "Sara": "review", "Ali": "good"}
# Rules:
# >= 90 excellent
# >= 80 good
# otherwise review

grade = ""
grade_dict = {}

for user in users:
    if user["score"] >= 90:
        grade = "excellent"
    elif user["score"] >= 80:
        grade = "good"
    else:
        grade = "review"
    grade_dict[user["name"]] = grade

print(grade_dict)




# TODO 4: use enumerate to print numbered user names.

for num, user in enumerate(users):
    print(f"{num + 1}. {user['name']}")




# TODO 5: print only active users, skipping inactive ones with continue.

for user in users:
    if not user["active"]:
        continue
    print(user["name"])
