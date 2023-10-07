import requests
import json
import pandas as pd

# Define the API URL
api_url = "https://restcountries.com/v3.1/all"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = json.loads(response.text)
    
    # Initialize empty lists for each field
    names = []
    currency_names = []
    populations = []
    
    for country in data:
        region = country.get("region", None)
        subregion = country.get("subregion", None)
        
        # Check if the country is in Northern Europe
        if region == "Europe" and subregion == "Northern Europe":
            # Extract the desired fields
            name = country.get("name", {}).get("official", None)
            currencies = country.get("currencies", None)
            population = country.get("population", None)

            # Check if all desired fields are available
            if name and currencies and population is not None:
                names.append(name)
                
                # Extract the "name" key from the nested dictionary "currencies"
                # currency_name = currencies.get("0", {}).get("1", {}).get("name")
                currency_name = next(iter(currencies.values()))['name']
                currency_names.append(currency_name)

                
                
                populations.append(population)

    # Create a Pandas DataFrame with the three columns
    df = pd.DataFrame({
        "nation_official_name": names,
        "currency_name": currency_names,
        "population": populations
    })
    
    # Display the DataFrame
    print(df)
else:
    print("Failed to retrieve data from the API.")