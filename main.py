import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime,date
#from dateuil.relativedelta import relativedelta
st.title('Crpyto Tracker')

st.sidebar.title('Options')
st.sidebar.selectbox('Select a cryptocurrency',['BTC','ETH','LTC'])