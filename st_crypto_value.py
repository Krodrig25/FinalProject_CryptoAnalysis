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
coin1_df = crypto_df[0:0]
coin2_df = crypto_df[0:0]
coin3_df = crypto_df[0:0]
crypto_df.sort_index(axis=0, inplace=True)

# Create selectboxes to choose data on specific coins for comparison.
selected_name1 = st.sidebar.selectbox(
    "Choose First Coin to Compare",
    crypto_df.index
)

selected_name2 = st.sidebar.selectbox(
    "Choose Second Coin to Compare",
    crypto_df.index
)
selected_name3 = st.sidebar.selectbox(
    "Choose Third Coin to Compare",
    crypto_df.index
)

# Create a button to add selected coin to dataframe.
if st.sidebar.button("Add Coins for Comparison"):
    coin1_df = pd.concat([streamlit_df, crypto_df[crypto_df.index == selected_name1]])
    coin2_df = pd.concat([streamlit_df, crypto_df[crypto_df.index == selected_name2]])
    coin3_df = pd.concat([streamlit_df, crypto_df[crypto_df.index == selected_name3]])

# Create checkbox to show data on specific coins for comparison.
if st.sidebar.checkbox("Show Comparison Data"):
    st.write(coin1_df)
    st.write(coin2_df)
    st.write(coin3_df)

# Write data sources and links at bottom of sidebar.
st.sidebar.markdown("Data provided by:")
st.sidebar.markdown("Messari.io [link](https://messari.io/)")
st.sidebar.markdown("CoinMarketCap.com [link](https://coinmarketcap.com/)")