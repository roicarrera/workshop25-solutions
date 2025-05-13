def classify_grade(score):
    """
    Classifies a numeric score into a letter grade.
    - 101 <= score <= 110: A+
    - 90 <= score <= 100: A
    - 80 <= score < 90: B
    - 70 <= score < 80: C
    - 60 <= score < 70: D
    - 0 <= score < 60: F
    - score must be an integer (not float)
    Any score < 0 or > 110 raises ValueError.
    Any non-integer input raises TypeError.
    """
    if not isinstance(score, int):
        raise TypeError("Score must be an integer")
    if score < 0 or score > 110:
        raise ValueError("Score must be between 0 and 110")

    if score > 100:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
