# py-data-engineering

A curated portfolio of **data engineering** projects in Python: ingestion, transformation, streaming, orchestration, and cloud.

[![CI](https://img.shields.io/github/actions/workflow/status/<your-username>/py-data-engineering/ci.yml?branch=main)](./.github/workflows/ci.yml)
![License](https://img.shields.io/badge/license-MIT-blue)

## Highlights
- Reproducible projects with tests, linting, and docs.
- Focus: **Pandas, Spark, Kafka, Airflow, AWS** (S3/Glue/Lambda/EMR).
- Consistent template for each project (`src/`, `tests/`, README).

## Getting Started
```bash
git clone https://github.com/<your-username>/py-data-engineering.git
cd py-data-engineering

# choose one: requirements OR Poetry
pip install -r requirements.txt
# or
poetry install
```

## Project Index
| # | Project | Area | Summary |
|---|--------|------|---------|
| 01 | Data Wrangling with Pandas | Data | Clean/transform CSV/Parquet; profiling & EDA. |
| 02 | API to Data Lake Pipeline | Ingestion | Pull REST data, validate, land to parquet, partitioned. |
| 03 | Spark Batch ETL | Big Data | S3/Local bronze→silver→gold using Spark; unit tests. |
| 04 | Kafka Streaming | Streaming | Producer/consumer, exactly-once-ish, watermarking demo. |
| 05 | Airflow + AWS Pipeline | Orchestration | DAG: extract→transform→load, S3/Glue/Athena, alerts. |

See details in [`/docs/projects.md`](./docs/projects.md).

## Conventions
- **Code style:** `ruff` + `black`
- **Tests:** `pytest`
- **Pre-commit:** format & lint before commit
- **Versioning:** semantic (0.1.0)

## Quality Checks
```bash
make format   # black
make lint     # ruff
make test     # pytest
```

## License
MIT © <Your Name>
