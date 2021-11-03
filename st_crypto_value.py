# Import the required libraries and dependencies
import pandas as pd
from pathlib import Path
import streamlit as st

# Read csv's into dataframes
crypto_df = pd.read_csv(
    Path("./crypto_df.csv")
)
profile_df = pd.read_csv(
    Path("./profile_df.csv")
)

# Set "name" as index for both dataframes
crypto_df.set_index("name", inplace=True)
profile_df.set_index("name", inplace=True)

# Create header for Streamlit page
st.markdown("# Crypto Value Opportunities")

# Create sidebar selectbox to filter data by category
selected_category = st.sidebar.selectbox(
    "Select a Category",
    set(crypto_df["categories"])
)
# Create sidebar checkbox to show data by category.
if st.sidebar.checkbox("Show Category Data"):
    st.write(crypto_df[crypto_df["categories"] == selected_category])
    st.bar_chart(crypto_df[crypto_df["categories"] == selected_category]["vlad club cost"])

# # Create sidebar selectbox to filter data by sector.
selected_sector = st.sidebar.selectbox(
    "Select a Sector",
    set(crypto_df["sectors"])
)

# Create sidebar checkbox to show data by sector.
if st.sidebar.checkbox("Show Sector Data"):
    st.write(crypto_df[crypto_df["sectors"] == selected_sector])
    st.bar_chart(crypto_df[crypto_df["sectors"] == selected_sector]["vlad club cost"])

# Create new dataframe to hold user-selected data.
streamlit_df = crypto_df[0:0]
crypto_df.sort_index(axis=0, inplace=True)

# Create selectbox to choose data on specific coins for comparison.
selected_name = st.sidebar.selectbox(
    "Choose Coins to Compare",
    crypto_df.index
)

# Create a button to add selected coin to dataframe.
if st.sidebar.button("Add Coin for Comparison"):
    streamlit_df.append(crypto_df[crypto_df.index == selected_name])

# Create a button to clear the dataframe.
if st.sidebar.button("Clear Comparison List"):
    streamlit_df = streamlit_df[0:0]

# Create checkbox to show data on specific coins for comparison.
if st.sidebar.checkbox("Show Comparison Data"):
    st.write(streamlit_df)
    st.bar_chart(streamlit_df["vlad club cost"])

# Break down `profile_df` into dictionaries for better Streamlit display.  
profile_dict = profile_df.to_dict()
tagline = profile_dict["tagline"]
profile = profile_dict["profile"]
links = profile_dict["links"]

# Create selectbox to choose profile data on specific coins.
profile_data = st.sidebar.selectbox(
    "Select Coin for Profile Info",
    profile_df.index
)

# Create checkbox to show profile data on specific coins.
if st.sidebar.checkbox("Show Profile Data"):
    st.write(tagline[tagline["name"] == profile_data])
    st.write(profile[profile["name"] == profile_data])
    st.write(links[links["name"] == profile_data])

# Write data sources and links at bottom of sidebar.
st.sidebar.markdown("Data provided by:")
st.sidebar.markdown("Messari.io [link](https://messari.io/)")
st.sidebar.markdown("CoinMarketCap.com [link](https://coinmarketcap.com/)")