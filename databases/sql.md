# SQL

Relational stuff: normalization, joins, complex queries...

## SQL queries

... basic stuff...

### Useful more advanced stuff for analytical engineers:
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