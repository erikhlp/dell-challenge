import asyncio
import aiohttp
import json
import pandas as pd

async def fetch_data(api_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None

async def main():
    api_url = "https://restcountries.com/v3.1/all"
    data = await fetch_data(api_url)

    if data:
        names = []
        currency_names = []
        populations = []

        for country in data:
            region = country.get("region", None)
            subregion = country.get("subregion", None)

            if region == "Europe" and subregion == "Northern Europe":
                name = country.get("name", {}).get("official", None)
                currencies = country.get("currencies", None)
                population = country.get("population", None)

                if name and currencies and population is not None:
                    names.append(name)
                    currency_name = next(iter(currencies.values()))['name']
                    currency_names.append(currency_name)
                    populations.append(population)

        df = pd.DataFrame({
            "nation_official_name": names,
            "currency_name": currency_names,
            "population": populations
        })

        print(df)
    else:
        print("Failed to retrieve data from the API.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())