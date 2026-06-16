def get_profile():
    return {
        "name": "Соня С.",
        "group": "РПО-02",
        "role": "student",
        "skills": ["Git", "VS Code", "Python", "Procrastination"]
    }


def print_profile():
    profile = get_profile()
    print(f"Студент: {profile['name']}")
    print(f"Группа: {profile['group']}")
    print("Навыки:", ", ".join(profile["skills"]))