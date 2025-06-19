def rank_excuse(excuse: str, urgency: str) -> int:
    score = 0
    word_count = len(excuse.split())

    if 15 <= word_count <= 35:
        score += 3

    if urgency.lower() == "high" and any(word in excuse.lower() for word in ["urgent", "emergency", "immediately", "sudden"]):
        score += 3
    elif urgency.lower() == "low" and not any(word in excuse.lower() for word in ["urgent", "emergency"]):
        score += 3

    if excuse.count(".") <= 2:
        score += 2

    natural_starts = ["I'm sorry", "I couldn't", "I had to", "Due to", "Unfortunately"]
    if any(excuse.lower().startswith(start.lower()) for start in natural_starts):
        score += 2

    return min(score, 10)
