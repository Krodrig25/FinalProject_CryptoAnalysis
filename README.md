# Crypto Analysis Final Project 

Ryan Scott & Kevin Rodriguez

Software utilized:

  •	Jupyter Notebook
  
  •	Virtual Studio Code
  
  •	Tableau
  
  •	Streamlit

This project is an attempt to analyze cryptocurrencies qualitatively. This technology is still very young and the general public is largely ignorant of the capabilities of these assets. They are primarily treated as speculative assets, and as such there is already a large amount of technical trading data available online. However, there is very little aggregated information on the fundamental value of these assets.

There are thousands of coins now in existence, so it's no small task to evaluate and compare them, but luckily there are API's that have the useful info we needed, particulary Messari.io. We also accessed CoinMarketCap.com for recent price and volume data.

Because we used Streamlit, this project is divided into two files: one for the API pulls and data parsing that produces csv files to work with locally, the other to run the Streamlit application with the CSV file data. We began with everything in a single file, however every time a Streamlit option changed, it refreshed and caused another API pull. It wasn't long before we had exhausted our day's allowance of pulls. Thus, we divided them into 2 files.

The first file, `api_data_parse.py` imports the libraries and dependancies, pulls from the API's, and parses the data to create two csv files, one with quantitative measures, the other with coin profile data and links.

