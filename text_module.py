def analyze_text(text):

    words = text.split()
    word_count = len(words)

    fillers = ["um", "uh", "like", "you know", "basically"]
    filler_count = sum(1 for w in words if w.lower() in fillers)

    avg_word_length = (
        sum(len(w) for w in words) / word_count
        if word_count > 0 else 0
    )

    return {
        "word_count": word_count,
        "filler_count": filler_count,
        "avg_word_length": avg_word_length
    }


def extract_skills(text):

    skills_list = [
        "python", "java", "c++", "machine learning",
        "communication", "teamwork", "leadership"
    ]

    words = text.lower().split()

    found_skills = [skill for skill in skills_list if skill in words]

    return found_skills if found_skills else ["Basic Communication"]