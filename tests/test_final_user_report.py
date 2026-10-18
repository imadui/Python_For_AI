from challenges.final_user_report import build_report


def test_build_report_happy_path():
    users = [
        {"name": "Imad", "active": True, "skills": ["Python", "AI"]},
        {"name": "Sara", "active": False, "skills": ["UiPath"]},
        {"name": "Ali", "active": True, "skills": ["Python"]},
    ]

    result = build_report(users)

    assert result == {
        "total": 3,
        "active_count": 2,
        "active_names": ["Ali", "Imad"],
        "skills": {
            "Python": 2,
            "AI": 1,
            "UiPath": 1,
        },
    }


def test_build_report_handles_missing_optional_keys():
    users = [
        {"name": "Imad"},
        {"name": "Ali", "active": True},
    ]

    result = build_report(users)

    assert result["total"] == 2
    assert result["active_count"] == 1
    assert result["active_names"] == ["Ali"]
    assert result["skills"] == {}


def test_build_report_does_not_mutate_input():
    users = [{"name": "Imad", "active": True, "skills": ["Python"]}]
    snapshot = [{"name": "Imad", "active": True, "skills": ["Python"]}]

    build_report(users)

    assert users == snapshot
