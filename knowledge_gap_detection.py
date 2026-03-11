# Knowledge Gap Detection System
# This program identifies topics where a learner is weak based on quiz scores

def detect_knowledge_gaps(scores, threshold=60):
    weak_topics = []

    for topic, score in scores.items():
        if score < threshold:
            weak_topics.append(topic)

    return weak_topics


# Example quiz scores of a learner
quiz_scores = {
    "Variables": 85,
    "Data Types": 70,
    "Operators": 65,
    "Functions": 45,
    "Loops": 50
}

# Detect weak topics
weak_areas = detect_knowledge_gaps(quiz_scores)

# Output result
if weak_areas:
    print("Recommended topics to review:")
    for topic in weak_areas:
        print("-", topic)
else:
    print("Great! No weak areas detected.")
