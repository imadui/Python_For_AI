def build_report(users: list[dict]) -> dict:
    active_names: list[str] = []
    skill_counts: dict[str, int] = {}

    for user in users:
        if user.get("active", False):
            active_names.append(user["name"])

        for skill in user.get("skills", []):
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    return {
        "total": len(users),
        "active_count": len(active_names),
        "active_names": sorted(active_names),
        "skills": skill_counts,
    }
