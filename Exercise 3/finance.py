import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the S&P 500 companies
table = soup.find('table', {'class': 'wikitable sortable'})

# Initialize an empty list to store ticker symbols, previous close values, and 200-Day Moving Averages
data_list = []

# Loop through the rows of the table and extract ticker symbols for the first 50 companies
for row in table.find_all('tr')[1:51]:  # Skip the header row and limit to 50 companies
    columns = row.find_all('td')
    if len(columns) >= 2:
        ticker_symbol = columns[0].text.strip()
        # Construct the Yahoo Finance API URLs for each company
        quote_url = f"https://finance.yahoo.com/quote/{ticker_symbol}?p={ticker_symbol}"
        statistics_url = f"https://finance.yahoo.com/quote/{ticker_symbol}/key-statistics?p={ticker_symbol}"
        
        # Send an HTTP GET request to get the Previous Close value
        quote_response = requests.get(quote_url)
        quote_soup = BeautifulSoup(quote_response.content, 'html.parser')
        previous_close_element = quote_soup.find('td', {'data-test': 'OPEN-value'})
        if previous_close_element:
            previous_close = previous_close_element.text.strip()
        else:
            previous_close = None
        
        # Send an HTTP GET request to get the 200-Day Moving Average value
        statistics_response = requests.get(statistics_url)
        statistics_soup = BeautifulSoup(statistics_response.content, 'html.parser')
        moving_average_element = statistics_soup.find('td', {'data-test': 'OPEN_200-value'})
        if moving_average_element:
            moving_average_200 = moving_average_element.text.strip()
        else:
            moving_average_200 = None
        
        # Append the data to the list
        data_list.append({'Ticker': ticker_symbol, 'Previous Close': previous_close, '200-Day Moving Average': moving_average_200})

# Create a Pandas DataFrame from the data list
df = pd.DataFrame(data_list)

# Convert 'Previous Close' and '200-Day Moving Average' columns to numeric values
df['Previous Close'] = pd.to_numeric(df['Previous Close'], errors='coerce')
df['200-Day Moving Average'] = pd.to_numeric(df['200-Day Moving Average'], errors='coerce')

# Compute the 'is_cheap' column based on the condition
df['is_cheap'] = df['Previous Close'] < df['200-Day Moving Average']

# Display the modified DataFrame
print(df)

# Filter the dataframe to include only rows where is_cheap = True
cheap_df = df[df['is_cheap'] == True]

# Create a plot for the filtered dataframe
plt.figure(figsize=(12, 6))
plt.bar(cheap_df['Ticker Symbol'], cheap_df['Previous Close'])
plt.xlabel('Ticker Symbol')
plt.ylabel('Previous Close Value')
plt.title('Companies Where is_cheap = True')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the plot
plt.show()
