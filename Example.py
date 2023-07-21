#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import numpy as np
#!pip install plost
import plost
from PIL import Image

# Page setting
st.set_page_config(layout="wide")

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

# Data
seattle_weather = pd.read_csv('MA_Public_Schools_datadict.csv')
stocks = pd.read_csv('MA_Public_Schools_2017.csv')

# Row A
a1, a2, a3 = st.columns(3)
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')

