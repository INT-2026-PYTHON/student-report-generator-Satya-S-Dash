"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    total = {}
    count = {}
    for i in records:
        name = i["name"]
        score = i["score"]
        if name not in total:
            total[name] = 0
            count[name] = 0
        total[name] += score
        count[name] += 1
        average = {}
    for i in total:
        average[i] = total[i] / count[i]
    round(average,2)
    return average


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    subjects = set()
    for i in records:
        subjects.add(i["subject"])
    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    avg = average_per_student(records)
    top_name = ""
    top_avg = 0
    for i in avg:
        if avg[i] > top_avg:
            top_name = i
            top_avg = avg[i]
    return (top_name, top_avg)


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    avg = average_per_student(records)
    passing = []
    for i in avg:
        if avg[i] >= threshold:
            passing.append(i)
    for i in range(len(passing)):
        for j in range(i + 1, len(passing)):
            if passing[i] > passing[j]:
                temp = passing[i]
                passing[i] = passing[j]
                passing[j] = temp
    return passing
