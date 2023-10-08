# Exercise 3
Language: Python
Scrape the S&amp;P 500 companies table from the following Wikipedia page:
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
Save the companies ticker symbols into a list. Cut the list to take only the first 50 elements.
For each ticker symbol in the list, call the following API In order to get the Previous Close value for each company:
https://finance.yahoo.com/quote/AAPL?p=AAPLtsrc=fin-srch
Save this value and the ticker symbol in a Pandas dataframe.
For each ticker symbol also call the following API endpoint in order to get the 200-Day Moving Average value:
https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL
Save this value in a new column of the same dataframe.
Compute a new column in the dataframe called “is_cheap” with a Boolean value which is True if the Previous Close is
lower than the 200-Day Moving Average and False otherwise.
Concatenate all dataframes for all ticker symbols in one.
Display the dataframe on a plot only for the companies where is_cheap = True.
On the X axis should be the Ticker symbol and on the Y axis the Previous Close value.

## Question 1
If the Wikipedia table was lazy loaded, and only appeared after a few seconds from opening the page, what libraries
and strategies could you adopt to get the data?

**Answer**

If the Wikipedia table is lazy-loaded and appears after a few seconds from opening the page, we can adopt the following libraries and strategies to get the data:

**Selenium**: Selenium is a Python library that allows we to automate web browsers. We can use Selenium to interact with the webpage, including waiting for the table to load before scraping it. Selenium can simulate user actions like clicking, scrolling, and waiting for elements to become visible.

**Explicit Wait**: With Selenium, we can implement explicit waits to pause the script until a specific condition is met. We can wait for the table to become visible or loaded before proceeding with the scraping.

## Question 2
If you had to run this script for thousands of companies instead of 500, what kind of patterns, libraries and/or
optimization techniques could you use to keep the process efficient?

**Answer**

When we need to run a script for scraping data from thousands of companies (or a large dataset in general), it's important to consider efficiency and optimization. Here are some patterns, libraries, and techniques to keep the process efficient:

- **Threading or Multiprocessing**: To speed up data retrieval for multiple companies, consider using Python's threading or multiprocessing libraries. These libraries allow we to run multiple scraping tasks concurrently, taking advantage of multi-core processors.

- **Rate Limiting and Politeness**: Be mindful of the website's terms of service and robots.txt file. Implement rate limiting and add pauses between requests to avoid overloading the server and getting blocked. Libraries like requests allow we to set custom headers, including User-Agent, to simulate human-like behavior.

- **Caching**: Implement caching mechanisms to store previously scraped data. If we need to fetch data periodically, this can save time and reduce the load on the website.

- **Batch Processing**: Instead of processing all companies in a single loop, consider processing them in smaller batches. This can help manage memory and make it easier to recover from interruptions.

- **Error Handling**: Implement robust error handling to handle various exceptions that can occur during web scraping. Retry mechanisms can be useful for transient errors.

- **Distributed Scraping**: If the dataset is extremely large, you might consider distributed scraping using a framework like Scrapy. Scrapy can distribute tasks across multiple machines and handle distributed storage.

- **Database Storage**: Store scraped data in a database rather than keeping it in memory. Databases are better suited for managing large datasets and can help with data retrieval and analysis.

- **Parallelism**: If our scraping involves complex computation, consider parallelizing the processing of data after retrieval to speed up analysis.

- **Data Serialization Formats**: Choose efficient data serialization formats like Parquet or Apache Arrow for storing and exchanging data. These formats are optimized for large datasets.

- **Monitoring and Logging**: Implement monitoring and logging to keep track of the scraping progress and identify issues quickly. Tools like Prometheus and Grafana can be useful for monitoring.

- **Content Delivery Networks (CDNs)**: If the website uses a CDN, you may need to route our requests through a proxy server to bypass rate limiting and access data more efficiently.

- **Cloud Services**: We can consider using cloud services like AWS, GCP, or Azure for distributed and scalable web scraping tasks. These platforms offer various tools and services for data processing and storage.

- **Scraping Rules**: We will need to periodically review and update our scraping rules and selectors to adapt to changes in the website's structure.

- **Legal and Ethical Considerations**: We'll have to ensure that our scraping activities comply with legal and ethical standards. Respect the website's terms of service, privacy policy, and copyright restrictions.