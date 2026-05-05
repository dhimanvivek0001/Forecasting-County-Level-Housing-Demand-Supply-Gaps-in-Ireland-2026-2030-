"""Utility helpers for the housing forecasting project."""
from __future__ import annotations

import pandas as pd


def parse_quarter(label: str) -> pd.Timestamp:
    """Convert a quarter label like '2024Q1' into a pandas timestamp."""
    year = int(label[:4])
    quarter = int(label[-1])
    month = {1: 1, 2: 4, 3: 7, 4: 10}[quarter]
    return pd.Timestamp(year=year, month=month, day=1)
