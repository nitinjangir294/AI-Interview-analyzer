def generate_feedback(data):

    feedback = []

    if data["word_count"] < 5:
        feedback.append("Answer is too short")
    elif data["word_count"] > 30:
        feedback.append("Try to be more concise")
    else:
        feedback.append("Good answer length")

    if data["filler_count"] > 3:
        feedback.append("Avoid using filler words")
    else:
        feedback.append("Good fluency")

    if data["avg_word_length"] < 4:
        feedback.append("Use more descriptive words")
    else:
        feedback.append("Good vocabulary")

    score = (
        (data["word_count"] / 30) +
        (1 - data["filler_count"] / 10) +
        (data["avg_word_length"] / 10)
    ) / 3

    score = max(0, min(score * 10, 10))

    return round(score, 2), feedback