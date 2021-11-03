# Import the required libraries and dependencies
import pandas as pd
from pathlib import Path
import streamlit as st

# Define function to read csv's into dataframes
@st.cache
def generate_dataframes():
    crypto_df = pd.read_csv(
        Path("./crypto_df.csv")
    )
    profile_df = pd.read_csv(
        Path("./profile_df.csv")
    )
    return (crypto_df, profile_df)

# Call function to generate dataframes
generate_dataframes()

# Create header for Streamlit page
st.markdown("# Crypto Value Opportunities")

'''
Create sidebar selectboxes and checkboxes to filter and show data by category/sector. Activated checkbox will display filtered dataframe and bar chart.
'''
selected_category = st.sidebar.selectbox(
    "Select a Category",
    set(crypto_df["categories"])
)

if st.sidebar.checkbox("Show Category Data"):
    st.write(crypto_df[crypto_df["categories"] == selected_category])
    st.bar_chart(crypto_df[crypto_df["categories"] == selected_category]["vlad club cost"])

selected_sector = st.sidebar.selectbox(
    "Select a Sector",
    set(crypto_df["sectors"])
)

if st.sidebar.checkbox("Show Sector Data"):
    st.write(crypto_df[crypto_df["sectors"] == selected_sector])
    st.bar_chart(crypto_df[crypto_df["sectors"] == selected_sector]["vlad club cost"])

'''
Create new dataframe to hold user-selected data. Create selectbox and checkbox to choose and show data on specific coins for comparison. Activated checkbox will display selected coins in dataframe and in bar chart. Create one button to add selected coin to dataframe, and another button to clear the dataframe. 
'''
streamlit_df = crypto_df[0:0]
crypto_df.sort_index(axis=0, inplace=True)

selected_name = st.sidebar.selectbox(
    "Choose Coins to Compare",
    crypto_df.index
)

if st.sidebar.button("Add Coin for Comparison"):
    streamlit_df.append(crypto_df[crypto_df.index == selected_name])

if st.sidebar.button("Clear Comparison List"):
    streamlit_df = streamlit_df[0:0]

if st.sidebar.checkbox("Show Comparison Data"):
    st.write(streamlit_df)
    st.bar_chart(streamlit_df["vlad club cost"])

'''
Break down `profile_df` into dictionaries for better Streamlit display. Create selectbox and checkbox to choose and show profile data on specific coins. 
'''
profile_dict = profile_df.to_dict()
tagline = profile_dict["tagline"]
profile = profile_dict["profile"]
links = profile_dict["links"]

profile_data = st.sidebar.selectbox(
    "Select Coin for Profile Info",
    profile_df.index
)

if st.sidebar.checkbox("Show Profile Data"):
    st.write(tagline[tagline["name"] == profile_data])
    st.write(profile[profile["name"] == profile_data])
    st.write(links[links["name"] == profile_data])

st.sidebar.markdown("Data provided by:")
st.sidebar.markdown("Messari.io [link](https://messari.io/)")
st.sidebar.markdown("CoinMarketCap.com [link](https://coinmarketcap.com/)")