# Exercise 1

Create a Web Page that looks as similar as possible to the screenshot below.
It should be possible to add a new Filter element in the “Filters” section, using the text input field and the + button.
When the filter elements are too many, a scrollbar will appear on the right side.
You can also delete each Filter element by clicking the X button next to them.
You can use HTML, CSS, vanilla JavaScript, jQuery, Bootstrap or any other styling library and framework.

## Question 1
How would you deploy this web page so that users can access it online? Talk about the infrastructure, the resources,
and the technologies needed.

**Answer**
To deploy this web page, we'll need the following infrastructure, resources, and technologies:
- **Web Hosting Service**: You will need a web hosting service to store the HTML, CSS, and JavaScript files and make them accessible to users on the internet. There are various hosting options available, including shared hosting, virtual private servers (VPS), cloud hosting, and dedicated servers. The choice depends on your expected traffic and budget;
- **Server Configuration**: If we're using a VPS or dedicated server, we'll need to configure the server environment to support our web application. This typically involves setting up a web server like Apache, Nginx, or a cloud service-specific server.
- **SSL Certificate:**: Let's consider securing our website with an SSL certificate to enable HTTPS. This is especially important if our web page handles sensitive information or user data.
- **Upload The Files:**: Once we have a hosting service and server configured, we'll need to upload our HTML, CSS, and JavaScript files to the server. This can typically be done using FTP (File Transfer Protocol) or through a web-based file manager provided by our hosting provider.
- **Database (Optional)**: If our web page requires data storage or user accounts, we may need a database. Common choices include MySQL, PostgreSQL, or a NoSQL database like MongoDB. We have to ensure the database is properly configured and secured.
- **COntent Delivery Network**: A CDN can help improve the performance and scalability of our web page by distributing content to multiple server locations around the world. This reduces latency and speeds up loading times for users in different geographic regions.
- **Backup and Disaster Recovery**: Set up regular backups of our website and server data to prevent data loss in case of server failures or other emergencies.
- **Security Mesasures**: Implement security best practices to protect our website from common web threats, such as SQL injection, XSS (Cross-Site Scripting), and CSRF (Cross-Site Request Forgery). Regularly update our software and apply security patches.
- **DNS Config**: Configure our domain's DNS settings to point to our hosting server's IP address. This allows users to access our website using our domain name.
- **Testinng**: Before making our website live, thoroughly test it to ensure that all features work as expected and that there are no errors or security vulnerabilities.
- **Compliance**: Ensure our website complies with relevant laws and regulations, such as LGPD for data privacy if we collect user data.
- **Documentation**: Keep documentation of our website's configuration, hosting details, and any third-party services we use.

## Question 2
How would you modify the code in order to populate the dropdown menu with values coming from a database? Talk about possible database solutions, and how the backend can interact with the frontend.

**Answer**
To populate a dropdown menu with values coming from a database, we'll need a backend server to interact with the database and provide data to the frontend. Here are the steps to achieve this:
- **Choose a Database Solution**:
 - **SQL Database**: If we're dealing with structured data, we can use SQL databases like MySQL, PostgreSQL, or SQLite.
 - **NoSQL Database**: For unstructured or semi-structured data, consider NoSQL databases like MongoDB.
- **Set Up and Configure the Database**: IWe'll istall and configure the chosen database system on our server or use a cloud-based database service like Amazon RDS or Google Cloud SQL.
Then we'll create a table or collection to store the data for the dropdown menu options.
- **Backend Development**: We'll create a backend application using a server-side language like Node.js, Python (with frameworks like Flask or Django), Ruby (with Ruby on Rails), or PHP.
Establish a connection to the database from our backend code.
Write a query to retrieve the data that should populate the dropdown menu.
- **Expose an API Endpoint**: We'll create an API endpoint on our backend that serves the data from the database. This endpoint should return the data in a structured format, typically JSON.
- **Frontend Development**: Modify our HTML and JavaScript code to include the dropdown menu.
Use JavaScript's fetch or another AJAX library to make an HTTP request to the API endpoint on our backend to fetch the data.
- **Populate the Dropdown**: Once the data is fetched from the backend, we have to loop through the data in JavaScript and dynamically populate the dropdown options.