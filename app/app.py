st.write("App loaded successfully.")

import streamlit as st
import yfinance as yf
import pandas as pd
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Simple Stock Price App")

# Debug message to confirm app is running
st.write("✅ App loaded successfully.")

# Define ticker symbol
tickerSymbol = 'GOOGL'

# Fetch data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')

# Show basic info
st.write("Ticker Symbol:", tickerSymbol)
st.write("Data shape:", tickerDf.shape)
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

# Display charts if data exists
if not tickerDf.empty:
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    st.subheader("Volume")
    st.line_chart(tickerDf.Volume)
else:
    st.warning("⚠️ No data found for the selected ticker and date range.")

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
