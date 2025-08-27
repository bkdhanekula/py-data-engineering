# Project Details

## 01 - Data Wrangling with Pandas
**Goal:** Load messy CSV/Parquet, clean, type-cast, dedupe, join, and export clean dataset.
**Success criteria:** Unit tests for transforms; data quality checks (nulls, ranges); README with before/after row counts.

## 02 - API to Data Lake Pipeline
**Goal:** Fetch paginated REST API, apply schema validation, write partitioned parquet (by date), and maintain idempotency.
**Success criteria:** Retry + backoff, saved raw JSON + curated Parquet, simple data dictionary, tests for schema drift.

## 03 - Spark Batch ETL
**Goal:** Bronze→Silver→Gold pipeline using PySpark (local or S3). Handle late-arriving data and small lookups.
**Success criteria:** Unit tests with `pytest`; checkpointing; job parameters; run logs; partition pruning demo.

## 04 - Kafka Streaming
**Goal:** Simulate event stream; streaming transforms (windowing, watermarking); sink to parquet or console.
**Success criteria:** Exactly-once-ish via idempotent producer; consumer offset mgmt; reproducible docker-compose.

## 05 - Airflow + AWS Pipeline
**Goal:** Orchestrate end-to-end DAG: extract (API) → transform (Spark/Pandas) → load (S3/Glue/Athena). Add SLA alert.
**Success criteria:** DAG passes `airflow dags test`; parametrized dates; success/failure callbacks; docstring & graph view.
