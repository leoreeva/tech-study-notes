# Distributed systems

Distributed systems generally consist of multiple interconnected devices or computers that work together to perform a task that is beyond the capacity of a single system. These systems work by collaborating, sharing resources and coordinating processes to handle complex workloads. 

![Distributed systems](images/distributed_systems.png)
*[(Image source)](https://www.splunk.com/en_us/blog/learn/distributed-systems.html)*

### Types
There are many models and architectures of distributed systems in use today. Most common:
- **Client-server architecture**, the most traditional and simple type of distributed system, involve a multitude of networked computers that interact with a central server for data storage, data processing, or other common goal.
- **Multi-Tier architecture**: Builds on client-server by further dividing server roles, isolating data processing and management tasks to separate nodes for efficiency and scalability.
- **Peer-to-peer architecture** distribute workloads among hundreds or thousands of computers all running the same software. Every node has the full application stack, offering high redundancy. Nodes synchronize with each other, ensuring system persistence even if some nodes fail.

### Key characteristics
- **Scalability**. The ability to grow as the size of the workload increases is an essential feature of distributed systems, accomplished by adding additional processing units or nodes to the network as needed.
- **Concurrency**. Distributed system components run simultaneously. They’re also characterized by the lack of a “global clock,” when tasks occur out of sequence and at different rates.
- **Availability and fault tolerance**. If one node fails, the remaining nodes can continue to operate without disrupting the overall computation.
- **Heterogeneity**. In most distributed systems, the nodes and components are often asynchronous, with different hardware, middleware, software and operating systems. This allows the distributed systems to be extended with the addition of new components.
- **Replication**. Distributed systems enable shared information and messaging, ensuring consistency between redundant resources, such as software or hardware components, thus improving fault tolerance, reliability, and accessibility.
- **Transparency**. The end user sees a distributed system as a single computational unit (a single app) rather than as its underlying parts, allowing users to interact with a single logical device rather than being concerned with the system’s architecture.

<br>

## Scalability
Scalability refers to the ability to grow or expand something efficiently while maintaining the performance. Scalability is about handling growth while preserving or enhancing performance and reliability. It’s not just about “getting bigger”, it’s about doing so in a way that aligns with your goals ensuring a seamless experience for everyone involved. 

There are different strategies to this.

![Scaling](images/scaling.png)
*[(Image source)](https://media.geeksforgeeks.org/wp-content/uploads/20240208100939/hvs-v.webp)*

### Vertical Scaling (scaling up)
It refers to adding more power (CPU, RAM, Storage) to your existing servers. While this can be a quick solution to handle a growing workload but it is limited to certain extent of the server. It can’t go beyond at certain limit. Sometimes it could be an expensive solution and may requires downtime for upgrades. Vertical Scaling are simple to implement without much changes required in the system architecture, however it is limited by hardware constraint and single point of failure.

Examples: 
- Upgrading a database server from 16 GB RAM to 64 GB RAM.
- Moving from a single-core processor to a multi-core processor.

### Horizontal Scaling (scaling out)
This means adding more instances or nodes to your system and distributing the load on multiple nodes. By doing this, organizations can handle increased demand efficiently, ensure high availability, and minimize the risk of bottlenecks. With horizontal scaling you can get virtually unlimited scalability with High availability and Fault tolerance, but it requires changes in the architecture like load balancing, maintaining sync nodes etc. Horizontal scaling is also more cost-effective and elastic (dynamic scaling up or down based on demand is easier)

Examples:
- Adding more servers to a web server cluster to handle additional requests
- Sharding a database to distribute data across multiple machines.

### Diagonal Scaling
A hybrid approach that combines vertical and horizontal scaling. Start by scaling vertically to a threshold, then scale horizontally as needed.


<br>


## Database scaling
When an application increase it user base, the database can struggle to handle the increasing load, resulting in slower response times, longer query execution, and eventual system crashes. Traditional relational databases work well initially but tend to show their limits in terms of scalability as they reach hardware limits (CPU, disk, memory).

Scaling a database means increasing read/write traffic, handling larger data volumes properly, having high availability and fault tolerance. 

### Sharding: Distributing Data Across Multiple Servers
Challenges Faced:
Data Growth: When a single database server can no longer hold all the data.
Increased Traffic: A single database struggling with too many read/write operations simultaneously.
Uneven Load Distribution: Some parts of the database getting hit harder than others, causing performance issues.
What is Sharding?
Sharding is a database partitioning technique where data is split into smaller, more manageable chunks (called shards) and stored across multiple servers. Each shard holds a subset of the data, and together, they make up the complete dataset.

For example, instead of storing all user data on one server, you could shard users based on their geographical region, dividing users from the US, Europe, and Asia into different shards.

How I Solved the Problem with Sharding:

To handle increasing data volumes and high traffic, I implemented range-based sharding in one of our projects where user data was growing exponentially.

Range-based Sharding: I partitioned data based on a specific key, such as user ID or date ranges. This allowed the system to split the data logically, with users from different regions or time zones distributed across different shards.
Shard Management: We used a shard manager to direct traffic to the appropriate database shard based on user queries. For example, if a user from Europe logs in, the shard manager directs the request to the EU-based shard.
Key Benefits of Sharding:

Horizontal Scalability: We were able to add more database servers (shards) as needed, distributing both the data and the load across multiple nodes.
Fault Isolation: If one shard went down, only a portion of the data and requests were affected, rather than the entire system.
Optimized Query Performance: Since each shard had a smaller subset of data, queries ran faster because they were operating on a reduced dataset.
Challenges in Sharding:

Complexity: Sharding adds complexity to the system. Querying across multiple shards, managing shard key selection, and handling resharding (moving data between shards) require careful planning.
Data Skew: If shards are not evenly distributed, some servers might be overloaded while others remain underutilized.

### Replication: Ensuring High Availability and Load Balancing
Challenges Faced:
High Read Traffic: A single database server struggling to handle high-volume read queries.
Downtime Risk: The need for high availability to ensure the system stays operational even if one database server fails.
What is Replication?
Replication involves copying data from one database (called the primary) to one or more databases (called replicas). The replicas act as backups and can also be used to distribute read traffic.

In a typical setup:

Primary Database: Handles all write operations.
Replica Databases: Handle read operations, reducing the load on the primary database.
How I Solved the Problem with Replication:

When facing high read traffic, I used master-slave replication (now commonly known as primary-replica replication).

Master-Slave Replication: The primary (master) database handled all write operations (such as user data updates), while the replicas (slaves) were used to serve read requests.
Read/Write Separation: I implemented a load balancer to direct read requests to the replica databases and write requests to the primary database. This allowed us to scale reads horizontally by adding more replicas when needed.
Key Benefits of Replication:

Load Distribution: By distributing read traffic to replicas, we reduced the load on the primary database, ensuring faster response times for both read and write queries.
High Availability: In case the primary database went down, one of the replicas could be promoted to act as the new primary, ensuring minimal downtime.
Fault Tolerance: Replication provided a real-time backup of the primary database, ensuring data redundancy.
Challenges in Replication:

Replication Lag: There’s often a slight delay between writing data to the primary database and propagating it to the replicas. This can lead to inconsistencies for read-heavy applications where real-time data is critical.
Handling Failover: Promoting a replica to a primary during an outage needs careful coordination, especially in avoiding split-brain scenarios (where two databases mistakenly assume they’re both primaries).

### Caching: Reducing Database Load and Improving Latency
Challenges Faced:
Frequent Access to the Same Data: Certain queries were being repeatedly executed, putting unnecessary load on the database.
Slow Response Times: Database queries, especially those involving complex joins or large datasets, were taking too long to return results.
What is Caching?
Caching involves storing frequently accessed data in a faster, temporary storage layer (typically in-memory) to reduce the load on the database and improve response times.

How I Solved the Problem with Caching:

To improve performance and reduce the strain on the database, I implemented caching with Redis.

In-memory Cache: Redis was used as an in-memory data store to cache frequently accessed data. For instance, user profiles that were being repeatedly accessed were cached in Redis, allowing the application to retrieve the data quickly without querying the database.
Cache Expiry: To avoid serving stale data, I implemented TTL (Time to Live) policies where cache entries automatically expired after a set period, ensuring that the cache was refreshed with updated data.
Key Benefits of Caching:

Improved Latency: By caching frequently accessed data, we significantly reduced query response times, as the cache is faster than querying the database.
Reduced Load on the Database: With fewer queries hitting the database, its overall performance improved, allowing it to focus on more critical tasks.
Cost Efficiency: By serving data from the cache, we were able to reduce the need for additional database instances, saving on infrastructure costs.
Challenges in Caching:

Cache Invalidation: Ensuring the cache is always up-to-date is tricky. If the data in the cache becomes outdated, it can lead to users seeing stale information.
Cache Misses: If the data is not in the cache (cache miss), the application still needs to query the database, potentially causing a performance drop.

<br>

## Load balancing

Load balancing is the process of distributing incoming network traffic across a set of resources, ensuring the performance and reliability of the system. This provides the flexibility to add or subtract resources as demand dictates.

![Load balancing](images/load_balancing.png)
*[(Image source)](https://www.geeksforgeeks.org/what-is-load-balancer-system-design/)*

There are three main problems that it solves:

- Single Point of Failure: if the server goes down or something happens to the server the whole application would be interrupted and it would become unavailable for the users for a certain period
- Overloaded Servers: there would be a limitation on the number of requests that a web server can handle
- Limited Scalability: without a load balancer, adding more servers to share the traffic is complicated. All requests are stuck with one server, and adding new servers won’t automatically solve the load issue

A load balancer can sit in front of the servers and direct client requests across all servers capable of serving them, optimizing speed and capacity use. This prevents one server from getting too busy and slowing down. If a server goes down, the load balancer redirects traffic to the remaining online servers. When we add a new server, the load balancer automatically starts sending requests to it.

### Algorithms
We need a load-balancing algorithm to decide which request should be redirected to which backend server.

- **Static Load Balancing Algorithms** involves predetermined assignment of tasks or resources without considering real-time variations in the system. This approach relies on a fixed allocation of workloads to servers or resources, and it doesn't adapt to changes during runtime. Might work well in situations that are more predictable
    - Round Robin
    - Weighted Round-Robin
    - Source IP hash

- **Dynamic Load Balancing Algorithms** make judgments in real time, regarding the distribution of incoming network traffic or computing burden among several servers or resources. This method adjusts to the system's shifting circumstances, including changes in resource availability, network traffic, and server load
    - Least Connection Method
    - Least Response Time Method

<br>

## aaa
aaa

<br>


## stuff to add...

Distributed Systems
- event-driven architecture
- message queues (Kafka, RabbitMQ)

synchronisation, replication, architecture styles, network technology, queues, messaging, 

la concorrenza in java  (tutta la roba sul quaderno; poi differenza thread vs process vs container...)