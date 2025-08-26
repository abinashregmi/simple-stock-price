import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Simple Stock Price App")
st.write("✅ App loaded successfully.")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')

st.write("Ticker Symbol:", tickerSymbol)
st.write("Data shape:", tickerDf.shape)

if not tickerDf.empty:
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    st.subheader("Volume")
    st.line_chart(tickerDf.Volume)
else:
    st.warning("⚠️ No data found for the selected ticker and date range.")
