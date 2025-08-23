# Views
[(Docs)](https://docs.snowflake.com/en/user-guide/views-introduction)

A view allows the result of a query to be accessed as if it were a table. The query is specified in the CREATE VIEW statement. 

```sql
CREATE VIEW doctor_view AS
    SELECT patient_ID, patient_name, diagnosis, treatment FROM hospital_table;
```

Views can be used almost anywhere that a table can be used (joins, subqueries, etc.)


## Types of views
Snowflake supports two types of views:
- **Non-materialized views** (usually simply referred to as “views”). Most common type, they are basically a named definition of a query. The results are created by executing the query at the time that the view is referenced in a query, and they're not stored for future use. 
- **Materialized views**. Results get stored, almost as if it was a table. This allows faster access, but requires storage space and active maintenance, both of which incur additional costs. In addition, they cache results, making them more performant than tables.

**Guidelines** for choosing between them:
| Choose materialized, if ALL are true | Choose regular, if ANY is true |
| ---- | ---- |
| The query results from the view don’t change often (almost always means that the underlying/base table for the view, or a subset of it, doesn’t change often) | The results of the view change often |
| The results of the view are used often (significantly more often than the query results change) | The results are not used often (relative to the rate at which the results change) |
| The query consumes a lot of resources (typically time or credits, but sometimes storage for intermediate results) | The query is not resource intensive so it is not costly to re-run it |


## Secure views
Both non-materialized and materialized views can be defined as secure. Secure views have advantages over standard views, including improved data privacy and data sharing; however, they also have some performance impacts to take into consideration.

For a non-secure view, **internal optimizations** can indirectly expose data; secure views do not utilize these optimizations, ensuring that users have no access to the underlying data. Also, non-secure **view definition** is visible to other users. With secure views, the view definition and details are visible only to authorized users (i.e. users who are granted the role that owns the view).

Views should be defined as secure when they are specifically designated for data privacy (i.e. to limit access to sensitive data that should not be exposed to all users of the underlying tables). Secure views should not be used for views that are defined solely for query convenience, such as views created to simplify queries for which users do not need to understand the underlying data representation. Secure views can execute more slowly than non-secure views.


## Recursive views (non-materialized only)
A non-materialized can refer to itself


## Advantages & Limitations
| Advantages | Limitations |
| --- | --- |
| Views enable writing more modular code | The definition for a view cannot be updated (i.e. you cannot use ALTER VIEW to change it), you must recreate the view with the a new definition |
| Views allow granting access to a subset of a table | Changes to a table are not automatically propagated to views created on that table. For example, if you drop a column in a table, the views on that table might become invalid |
| Materialized views can improve performances | Snowflake recommends excluding the ORDER BY clause from most view definitions, because it would add unnecessary costs |
| / | The definition for a view is limited to 95KB |
| / | Nesting levels are limited to a maximum of 20. An attempt to create a view that is nested more than 20 times will fail |
