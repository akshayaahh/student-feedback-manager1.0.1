def summarize_feedback(feedback_data):
    """
    feedback_data: List of dicts with keys: 'name', 'score', 'grade'
    Returns: dict with top_score, top_scorers, grade_counts
    """
    if not feedback_data:
        return {
            "top_score": None,
            "top_scorers": [],
            "grade_counts": {}
        }

    top_score = max(item['score'] for item in feedback_data)
    top_scorers = [item['name'] for item in feedback_data if item['score'] == top_score]

    grade_counts = {}
    for item in feedback_data:
        grade = item['grade']
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

    return {
        "top_score": top_score,
        "top_scorers": top_scorers,
        "grade_counts": grade_counts
    }
