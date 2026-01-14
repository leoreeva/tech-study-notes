# Interview prep

## 1. SQL Question (~20–25 minutes for an analytical query)
- GROUP BY, HAVING
    - Conditional aggregation (SUM(CASE WHEN …))
- Window functions (very common)
    - ROW_NUMBER, RANK, DENSE_RANK
    - LAG / LEAD
    - Running totals (SUM() OVER (...))
    - Partitioning vs ordering

Typical question patterns:
- “Top N per group”
- “Find duplicates / latest record per key”
- “Compute metrics over time”
- “Sessionization / rolling metrics”

## 2. Python Question (~20–25 minutes of pure Python problem)
- Data structures
    - Lists, dicts, sets, tuples
    - Dictionary comprehension
    - Sorting with custom keys
- Algorithms & logic
    - Counting / grouping
    - Deduplication
    - Parsing structured data (JSON-like dicts)
    - Basic string manipulation
- Complexity awareness
    - Using hash maps instead of nested loops

Typical question patterns:
- Aggregate records by key
- Transform one data format into another
- Find anomalies / missing values
- Simulate a small ETL step

## 3. Data Engineering Fundamentals (6 Questions, Likely Multiple-Choice or Short Answer)
- ETL / ELT
    - Batch vs streaming
    - Incremental loads
- Data Warehousing
    - OLTP vs OLAP
    - Columnar vs row-based storage
    - Partitioning and clustering
    - Why indexes may or may not exist in warehouses
- Distributed Systems Basics
    - Why data is partitioned
    - What happens when a node fails
    - Eventual consistency (high level)
    - Tradeoffs between consistency, availability, latency
- Data Quality & Reliability
    - Schema enforcement vs schema-on-read
    - Data validation checks
    - Handling late or duplicate data
    - Backfills
- Orchestration & Pipelines
    - DAGs and dependencies
    - Retries vs reprocessing
    - Failure handling strategies
