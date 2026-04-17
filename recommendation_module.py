import webbrowser

def recommend_improvements(skills, score, feedback):

    recommendations = []
    learning_links = []

    skill_resources = {
        "python": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
        "java": "https://www.youtube.com/watch?v=grEKMHGYyns",
        "c++": "https://www.youtube.com/watch?v=vLnPwxZdW4Y",
        "machine learning": "https://www.youtube.com/watch?v=GwIo3gDZCVQ",
        "communication": "https://www.youtube.com/watch?v=HAnw168huqA",
        "teamwork": "https://www.youtube.com/watch?v=3boKz0Exros",
        "leadership": "https://www.youtube.com/watch?v=6z5m3Zf3pF8"
    }

    important_skills = ["python", "communication", "teamwork"]

    for skill in important_skills:
        if skill not in skills:
            recommendations.append(f"Learn {skill}")
            learning_links.append((skill, skill_resources[skill]))

    if score < 5:
        recommendations.append("Practice mock interviews")
    elif score < 7:
        recommendations.append("Improve answer clarity")

  
    for f in feedback:
        if "filler" in f.lower():
            recommendations.append("Practice speaking without pauses")
        if "short" in f.lower():
            recommendations.append("Give detailed answers")

    return list(set(recommendations)), learning_links


def open_learning_resources(learning_links):

    if not learning_links:
        print("\nNo learning resources needed. Good job!")
        return

    print("\nLearning Resources Available:")

    for i, (skill, link) in enumerate(learning_links, 1):
        print(f"{i}. {skill} → {link}")

    choice = input("\nEnter number to open course (or press Enter to skip): ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(learning_links):
            webbrowser.open(learning_links[index][1])