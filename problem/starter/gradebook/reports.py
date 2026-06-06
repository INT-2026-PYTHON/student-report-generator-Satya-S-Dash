"""gradebook.reports — build a printable report from grade records."""
from .stats import average_per_student
from .stats import subjects_offered
from .stats import top_scorer
from .stats import passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    avg = average_per_student(records)
    passing = passing_students(records)
    subjects = subjects_offered(records)
    top = top_scorer(records)
    report = {
        "total_records": len(records),
        "subjects": sorted(subjects),
        "averages": avg,
        "top_scorer": top,
        "passing_students": passing
    }
    return report