"""
utils.py
--------
Reusable, testable functions shared across all notebooks in this project.

Design decision: keeping logic here rather than inline in notebooks means
it can be unit tested with pytest and linted with ruff. Notebooks import
and call these functions, keeping them focused on narrative and results
rather than implementation detail.
"""

import pandas as pd

EXPECTED_COLUMNS = [
    "Current Programme (Aptem)",
    "Apprenticeship Level",
    "Achievement Date (ILR)",
    "EPAO",
    "aptem__UserILRSummary_GradingOutcome",
    "Age Bracket",
]


def validate_schema(df: pd.DataFrame) -> None:
    """
    Confirm the DataFrame contains all expected columns.

    Raises ValueError early with a clear message if columns are missing,
    rather than allowing a silent failure six steps later when a renamed
    column causes a cryptic KeyError mid-pipeline.
    """
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing expected columns: {missing}. "
            f"Check the source file hasn't been re-exported with renamed columns."
        )

    extra = set(df.columns) - set(EXPECTED_COLUMNS)
    if extra:
        print(f"Note: unexpected extra columns found: {extra}")