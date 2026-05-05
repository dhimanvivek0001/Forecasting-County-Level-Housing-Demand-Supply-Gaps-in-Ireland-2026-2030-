"""Project configuration."""
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = ROOT_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"

COUNTIES = [
    "Carlow", "Cavan", "Clare", "Cork", "Donegal", "Dublin", "Galway",
    "Kerry", "Kildare", "Kilkenny", "Laois", "Leitrim", "Limerick", "Longford",
    "Louth", "Mayo", "Meath", "Monaghan", "Offaly", "Roscommon", "Sligo",
    "Tipperary", "Waterford", "Westmeath", "Wexford", "Wicklow",
]
