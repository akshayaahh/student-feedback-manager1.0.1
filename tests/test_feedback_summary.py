import pytest
from feedback_summary import summarize_feedback

def test_summary_basic():
    data = [
        {'name': 'Alice', 'score': 90, 'grade': 'A'},
        {'name': 'Bob', 'score': 85, 'grade': 'B'},
        {'name': 'Charlie', 'score': 90, 'grade': 'A'},
        {'name': 'David', 'score': 70, 'grade': 'C'}
    ]
    result = summarize_feedback(data)
    assert result['top_score'] == 90
    assert set(result['top_scorers']) == {'Alice', 'Charlie'}
    assert result['grade_counts'] == {'A': 2, 'B': 1, 'C': 1}

def test_summary_empty():
    result = summarize_feedback([])
    assert result['top_score'] is None
    assert result['top_scorers'] == []
    assert result['grade_counts'] == {}
