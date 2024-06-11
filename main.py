import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

st.title('Crpyto Tracker')
st.sidebar.title('Options')
crypto_mapping = st.sidebar.selectbox('Select a cryptocurrency',['BTC','ETH','LTC'])
st.sidebar.date_input('Start Date',date.today() - relativedelta(months=1))
st.sidebar.selectbox("Select a time period",['1d','5d','1m','3m','6m'])
selected_value = st.sidebar.selectbox("Select a value to display",['Open','Close','High','Low','Volume'])

if st.sidebar.button('Track Crypto Currency '):
    crypto_history = yf.download(crypto_mapping, start = st.sidebar.date_input('Start Date'), end = st.sidebar.date_input('End Date') )
    fig = px.line(crypto_history,x=crypto_history.index,y = selected_value, title = f'{crypto_mapping}{selected_value}price')
    st.plotly_chart(fig)

crypto_data = yf.Ticker(crypto_mapping)