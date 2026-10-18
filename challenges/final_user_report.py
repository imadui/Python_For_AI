"""Final integration challenge.

Do NOT use the network in build_report().
Keeping transformation logic separate makes it easy to test.
"""


def build_report(users: list[dict]) -> dict:
    """Build a report from user dictionaries.

    Return:
    {
        "total": int,
        "active_count": int,
        "active_names": list[str],
        "skills": dict[str, int],
    }

    Rules:
    - Missing `active` means False.
    - Missing `skills` means [].
    - Count every skill occurrence.
    - Sort active_names alphabetically.
    - Do not mutate input.
    """
    raise NotImplementedError
