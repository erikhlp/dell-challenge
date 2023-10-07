# Exercise 2
Language: Python

Use the following public REST API.
https://restcountries.com/
Get data only for Northern European countries, and filter only for the following fields:
name
currencies
population
The API call should be asynchronous and encapsulated in a function.
Load the JSON response into a dictionary and then turn it into a single index Pandas dataframe.
The columns should be “nation_official_name”, “currency_name” and “population”.
The dataframe should look like this:
![Dataframe](dataframe.png)
then connect to a hypothetical Postgres Database and load the dataframe to a new table, in REPLACE mode.

## Question 1
If you didn’t know the structure of the JSON, and there was an arbitrary level of nesting of arrays and dictionaries,
how would you need to change the code to dynamically unnest the data into a single-indexed dataframe?

**Answer**
If the structure of the JSON data is unknown and we need to dynamically unnest it into a single-indexed DataFrame, we can use a recursive function to flatten the nested structure.


## Question 2
If you had to scale this application to read and load data for hundreds of countries and refresh the database every
few minutes, what strategies could be used in terms of coding patterns, technologies, resources and infrastructure?

**Answer**
To scale the application to read and load data for hundreds of countries and refresh the database every few minutes, we can consider several strategies in terms of coding patterns, technologies, resources, and infrastructure:

- **Asynchronous Processing**: Use asynchronous programming to efficiently handle multiple API requests concurrently. We can leverage Python's asyncio library to manage asynchronous tasks and aiohttp for asynchronous HTTP requests.
- **Batch Processing**: Instead of fetching data for all countries in a single request, break it down into smaller batches or chunks. Fetch data for a subset of countries at a time to prevent overloading the API or our system.
- **Caching**: Implement a caching mechanism to store previously fetched data temporarily. This can reduce the number of API requests and improve response times. Web can use in-memory caching (e.g., Redis) or simple file-based caching.
- **Database Optimization**: Optimize the database operations. Ensure our database schema is efficient, use appropriate indexing, and consider database-specific optimizations. PostgreSQL, for example, offers various performance tuning options.
- **Database Connection Pooling**: Use a connection pool to efficiently manage database connections. Libraries like SQLAlchemy provide built-in connection pooling capabilities.
- **Load Balancing**: If we anticipate a high volume of requests, consider deploying the application on multiple servers behind a load balancer to distribute the load evenly and ensure redundancy.
- **Background Jobs**: Implement a task scheduling system to periodically fetch and update data. Libraries like Celery or task queues in cloud platforms (e.g., AWS SQS) can help with background job processing.
- **Logging and Monitoring**: Implement proper logging and monitoring to track the application's performance and troubleshoot issues. Tools like Prometheus, Grafana, or application-specific logging solutions can be beneficial.
- **Error Handling and Retry Mechanism**: Implement robust error handling and retry mechanisms for API requests. Handle temporary failures gracefully and retry them after a brief delay.
- **Docker and Container Orchestration**: Use Docker containers to package our application and its dependencies. Deploy containers using container orchestration platforms like Kubernetes or Docker Compose for easier scaling and management.
- **Cloud Services**: Consider leveraging cloud services such as AWS, Azure, or Google Cloud. These platforms provide managed database services, serverless computing, and auto-scaling capabilities that can simplify scaling and resource management.
- **Scheduled Tasks**: Use cron jobs or scheduled tasks to trigger the data refresh process at specified intervals.
- **Horizontal Scaling**: If the application's load continues to grow, we can horizontally scale by adding more servers or containers to distribute the load.
- **Throttling and Rate Limiting**: Respect API rate limits imposed by the data source. Implement rate limiting and throttling mechanisms to avoid overloading the API.
- **Testing and Benchmarking**: Continuously test and benchmark our application to identify bottlenecks and areas for improvement. Tools like Apache JMeter or Gatling can help simulate high loads for testing.
- **Security**: Ensure proper security measures are in place to protect sensitive data, both in transit and at rest.
- **Documentation**: Maintain comprehensive documentation for our application, including code comments, deployment instructions, and troubleshooting guides.
- **Cost Optimization**: Monitor and optimize resource usage to manage costs effectively, especially when using cloud services.
Scaling an application involves a combination of architectural decisions, code optimizations, and infrastructure management. The specific strategies you choose will depend on your project's requirements, available resources, and the technology stack you are using.