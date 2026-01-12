# Interview prep

## 1. SQL Question (~20–25 minutes for a medium-difficulty analytical query)
Core topics:
- Joins
    - INNER vs LEFT vs RIGHT
    - Joining on multiple keys
    - Handling missing / NULL values
    - Aggregations
- GROUP BY, HAVING
    - COUNT vs COUNT(DISTINCT)
    - Conditional aggregation (SUM(CASE WHEN …))
- Window functions (very common)
    - ROW_NUMBER, RANK, DENSE_RANK
    - LAG / LEAD
    - Running totals (SUM() OVER (...))
    - Partitioning vs ordering
- Date & time
    - Grouping by day/week/month
    - Filtering by date ranges
    - Time-based windows

Typical question patterns:
- “Top N per group”
- “Find duplicates / latest record per key”
- “Compute metrics over time”
- “Sessionization / rolling metrics”


## 2. Python Question (~20–25 minutes of pure Python problem)
Core topics:
- Data structures
    - Lists, dicts, sets, tuples
    - Dictionary comprehension
    - Sorting with custom keys
- Algorithms & logic
    - Counting / grouping
    - Deduplication
    - Parsing structured data (JSON-like dicts)
    - Basic string manipulation
- Functions
    - Writing clean functions
    - Handling edge cases
    - Input/output expectations
- Complexity awareness
    - Knowing when something is O(n²) vs O(n)
    - Using hash maps instead of nested loops

Typical question patterns:
- Aggregate records by key
- Transform one data format into another
- Find anomalies / missing values
- Simulate a small ETL step

## 3. Data Engineering Fundamentals (6 Questions, Likely Multiple-Choice or Short Answer)

High-priority topics:
- Data Modeling
    - Star vs snowflake schema
    - Fact vs dimension tables
    - Normalization vs denormalization
    - Slowly Changing Dimensions (Type 1 vs Type 2)
- ETL / ELT
    - Difference between ETL and ELT
    - Batch vs streaming
    - Idempotency
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

