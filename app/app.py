import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Simple Stock Price App")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')

st.write("Ticker Symbol:", tickerSymbol)
st.write("Data shape:", tickerDf.shape)

if not tickerDf.empty:
    st.write("## Closing Price")
    st.line_chart(tickerDf.Close)

    st.write("## Volume Price")
    st.line_chart(tickerDf.Volume)
else:
    st.warning("No data found for the selected ticker and date range.")
