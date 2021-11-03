# Import the required libraries and dependencies
import os
import pandas as pd
from requests import Session
from dotenv import load_dotenv
import json
from six.moves import urllib

load_dotenv()

cmc_api_key = os.getenv("X-CMC_PRO_API_KEY")

# API call
parsed_url = "https://data.messari.io/api/v2/assets?limit=500"
parsed_bytes = urllib.request.urlopen(parsed_url).read()
        
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'500',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmc_api_key,
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
data = json.loads(response.text)

# Create empty list for each desired variable
symbol = []
slug = []
marketcap_rank = []
marketcap_usd = []
categories = []
sectors = []
price_usd = []
tagline = []
profile = []
links = []
max_supply = []
circulating_supply = []
volume_24h = []
volume_change_24h = []
percent_change_1h = []
percent_change_24h = []
percent_change_7d = []
percent_change_30d = []
percent_change_60d = []
percent_change_90d = []

# Loop through Messari json instance and load values into lists by type
for row in json.loads(parsed_bytes)["data"]:
    symbol.append(row["symbol"])
    slug.append(row["slug"])
    marketcap_rank.append(row["metrics"]["marketcap"]["rank"])
    marketcap_usd.append(row["metrics"]["marketcap"]["current_marketcap_usd"])
    categories.append(row["metrics"]["misc_data"]["categories"])
    sectors.append(row["metrics"]["misc_data"]["sectors"])
    price_usd.append(row["metrics"]["market_data"]["price_usd"])
    tagline.append(row["profile"]["general"]["overview"]["tagline"])
    profile.append(row["profile"]["general"]["overview"]["project_details"])
    links.append(row["profile"]["general"]["overview"]["official_links"])
    
# Loop through CoinMarketCap json instance and load values into lists by type
for row in data["data"]:
    max_supply.append(row["max_supply"])
    circulating_supply.append(row["circulating_supply"])
    volume_24h.append(row["quote"]["USD"]["volume_24h"])
    volume_change_24h.append(row["quote"]["USD"]["volume_change_24h"])
    percent_change_1h.append(row["quote"]["USD"]["percent_change_1h"])
    percent_change_24h.append(row["quote"]["USD"]["percent_change_24h"])
    percent_change_7d.append(row["quote"]["USD"]["percent_change_7d"])
    percent_change_30d.append(row["quote"]["USD"]["percent_change_30d"])
    percent_change_60d.append(row["quote"]["USD"]["percent_change_60d"])
    percent_change_90d.append(row["quote"]["USD"]["percent_change_90d"])

# Add lists to dictionary
crypto = {
    "symbol": symbol,
    "name": slug,
    "marketcap rank": marketcap_rank,
    "marketcap usd": marketcap_usd,
    "categories": categories,
    "sectors": sectors,
    "price usd": price_usd,
    "tagline": tagline,
    "profile": profile,
    "links": links,
    "max supply": max_supply,
    "circulating supply": circulating_supply,
    "volume 24h": volume_24h,
    "volume chg 24h": volume_change_24h,
    "pct chg 1h": percent_change_1h,
    "pct chg 24h": percent_change_24h,
    "pct chg 7d": percent_change_7d,
    "pct chg 30d": percent_change_30d,
    "pct chg 60d": percent_change_60d,
    "pct chg 90d": percent_change_90d
}

# Convert dictionary to dataframe and drop rows with null values
crypto_df = pd.DataFrame(crypto)
crypto_df = crypto_df.dropna()
crypto_df = crypto_df[crypto_df.notnull()]
crypto_df.drop(labels=0, inplace=True)

# Create dataframes from descriptive columns of first df
profile_df = crypto_df[["name", "tagline", "profile", "links"]]

# Establish "vlad club cost" column
crypto_df["vlad club cost"] = crypto_df["max supply"] * .0001 * crypto_df["price usd"]

# Change "categories" and "sectors" column datatypes from lists to strings
crypto_df["categories"] = crypto_df["categories"].explode()
crypto_df["sectors"] = crypto_df["sectors"].explode()

# Remove unnecessary columns and rows from dataframes
crypto_df = crypto_df.drop(columns=["tagline", "profile", "links"])

# Move `vlad club cost` column forward for better visibility
crypto_df = crypto_df[["name", "symbol", "vlad club cost", "marketcap rank", "marketcap usd", "categories", "sectors", "price usd", "max supply", "circulating supply", "volume 24h", "volume chg 24h", "pct chg 1h", "pct chg 24h", "pct chg 7d", "pct chg 30d", "pct chg 60d", "pct chg 90d"]]

# Set float decimal count to 2
pd.options.display.float_format = "{:,.2f}".format

# Set "name" as index for both dataframes
crypto_df.set_index("name", inplace=True)
profile_df.set_index("name", inplace=True)

# Remove row with problematic category from both dataframes
crypto_df = crypto_df.drop("bitcoin-gold", axis=0)
profile_df = profile_df.drop("bitcoin-gold", axis=0)

# Convert dataframes to csv files
crypto_df.to_csv("crypto_df.csv")
profile_df.to_csv("profile_df.csv")