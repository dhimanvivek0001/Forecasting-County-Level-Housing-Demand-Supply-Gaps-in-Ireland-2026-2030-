# Forecasting County-Level Housing Demand–Supply Gaps in Ireland (2026–2030)

<p align="center">
  <img src="assets/logo.svg" alt="Project logo" width="140" />
</p>

<p align="center">
  <strong>A data-driven decision-support framework for housing planning and policy in Ireland.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-academic%20project-success">
  <img alt="Domain" src="https://img.shields.io/badge/domain-housing%20analytics-2ea44f">
  <img alt="Methods" src="https://img.shields.io/badge/methods-ETS%20%7C%20SARIMA%20%7C%20XGBoost-orange">
</p>

## Repository name
`housing-demand-supply-ireland`

## Recommended GitHub description
County-level forecasting of housing demand–supply gaps in Ireland using ETS, SARIMA, XGBoost, SHAP, and hierarchical reconciliation.

## Recommended topics
`housing-analytics` `forecasting` `time-series` `xgboost` `shap` `ireland` `public-policy` `urban-planning` `data-science` `housing-market`

## Executive summary
This repository packages a final year project that forecasts county-level housing completions in Ireland and estimates future housing demand–supply gaps for 2026–2030. The project integrates eight public datasets into a county-by-quarter panel covering 26 counties and compares six forecasting models under rolling-origin cross-validation. Exponential Smoothing (ETS) is the best-performing model, while XGBoost adds interpretable machine-learning insights through SHAP analysis. Demand projections show a substantial divergence between a constant-headship scenario and a convergence-to-UK-headship scenario, with national demand potentially approaching 60,000 homes per year.

## Key findings
- **Best forecasting model:** ETS delivered the strongest accuracy under rolling-origin cross-validation.
- **Most important supply drivers:** Lagged completions, population, rent pressure, and commencement activity.
- **Demand sensitivity:** Headship-rate assumptions materially change national demand estimates.
- **Policy signal:** The 2025 fall in commencements is a potential warning sign for 2026–2027 delivery.
- **Geographic priority areas:** Cork, Galway, and Tipperary emerge as the most significant projected shortfall counties under the moderate scenario.

## Results at a glance
| Area | Headline result |
|---|---|
| Panel design | 1,560 observations across 26 counties |
| Forecast horizon | 2026–2030 |
| Best model | ETS |
| Best mean MAE | 141.3 |
| Best median MAE | 61.1 |
| Reconciliation uplift | 2.2% MAE improvement |
| Constant-headship demand | ~31,203 homes/year |
| Convergence-headship demand | ~60,013 homes/year |
| Moderate-scenario national gap | ~12,813 homes/year by 2028 |

## Tech stack
- **Language:** Python
- **Core libraries:** pandas, numpy, matplotlib, seaborn, statsmodels, pmdarima, xgboost, lightgbm, shap, scipy, scikit-learn
- **Outputs:** figures, comparison tables, explainability plots, scenario charts, county rankings
- **Workflow:** data cleaning → feature engineering → forecasting → explainability → scenario analysis → policy interpretation

## Repository structure
```text
housing-demand-supply-ireland/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── workflows/
│   │   └── python-ci.yml
│   └── pull_request_template.md
├── assets/
│   └── logo.svg
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── README.md
├── docs/
│   ├── analysis_tables.md
│   ├── executive_summary.md
│   ├── figures_manifest.md
│   ├── findings_and_policy.md
│   ├── methodology.md
│   ├── repository_information.md
│   └── roadmap.md
├── notebooks/
│   ├── Housing_Project.ipynb
│   └── README.md
├── outputs/
│   ├── figures/
│   │   └── .gitkeep
│   └── tables/
│       └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   └── prepare_data.py
│   ├── forecasting/
│   │   ├── __init__.py
│   │   ├── benchmark_models.py
│   │   ├── ml_models.py
│   │   └── rolling_cv.py
│   ├── reconciliation/
│   │   ├── __init__.py
│   │   └── reconcile.py
│   └── visualization/
│       ├── __init__.py
│       └── charts.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Suggested GitHub release title
**v1.0.0 — Final Year Project Submission Repository**

## Suggested social / portfolio title
**Forecasting Ireland’s County-Level Housing Demand–Supply Gap with Time-Series and Explainable ML**

## How to use this repository
1. Place source CSV files into `data/raw/`.
2. Reproduce the cleaned county-quarter panel.
3. Run forecasting experiments and rolling-origin evaluation.
4. Generate SHAP explainability outputs and scenario charts.
5. Export figures and tables into `outputs/` for reporting.

## Reproducibility notes
This repository is structured to be publication-ready and recruiter-friendly. It separates documentation, notebooks, outputs, and reusable source code so the work can be evaluated as both an academic submission and a portfolio project.

## Citation
If you use or adapt this repository, cite the accompanying study title:

> Forecasting County-Level Housing Demand–Supply Gaps in Ireland (2026–2030): A Data-Driven Decision-Support Framework for Planning and Policy
