# s24-stat-tech-analysis

# Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# How to gather data

We have an option of two models: `two-link` and `pendulum`.

```bash
python3 collect_data --model two-link
```

Data will be saved to `data/` directory.

## How to change control algorithm

You can change control algorithm in corresponding `{MODEL}.py` file.

## Analysis

Analysis is done in [analysis.ipynb](analysis.ipynb) notebook.
