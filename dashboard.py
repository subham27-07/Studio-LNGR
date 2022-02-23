import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import plotly.express as px


from copy import deepcopy
from bertopic import BERTopic

import networkx as nx


from nltk.featstruct import _default_fs_class
from numpy import e
import streamlit as st

import streamlit.components.v1 as components
from PIL import Image
# import pandas as pd
# import tweepy as tw
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.decomposition import LatentDirichletAllocation as LDA
import matplotlib.pyplot as plt
import altair as alt
import time
import setuptools

import time

import datetime
from datetime import datetime

df=pd.read_csv('sensors_output2.csv')

st.title ("StudioLNGR AMPS system Dashboard")
# st.sidebar.title("Analysis of Tweets")
st.markdown("This application is a Streamlit dashboard used to AMPS system")
# st.sidebar.markdown("This application is a Strea

st.write(df)

select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='1')


if select == 'SoilMoisture':

    fig = px.scatter(df, x=df['Soil Moisture'], y=df['Date'], marginal_x="histogram", marginal_y="rug", width=700,height=900)

    # z= spectra_df['score'].plot()
    st.plotly_chart(fig)


select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'))

if select == 'VOC':

    fig = px.bar(df, x=df['Date'], y=df['VOC'])

    # z= spectra_df['score'].plot()
    st.plotly_chart(fig)

select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='2')

if select == 'CO2':

    fig = px.scatter(df, x=df['CO2'], y=df['Date'], marginal_x="histogram", marginal_y="rug", width=700,height=900)

    # z= spectra_df['score'].plot()
    st.plotly_chart(fig)

select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='3')

if select == 'Temeprature1 & Humidity1':
    pd.options.plotting.backend = "plotly"
    df.plot(x=[ 'Temperature1', 'Humidity1'], y='Date')
    df_melt = df.melt(id_vars='Date', value_vars=['Temperature1', 'Humidity1'])
    fig=px.line(df_melt, x='Date' , y='value' , color='variable')
    st.plotly_chart(fig)


select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='4')
if select == 'Temeprature2 & Humidity2':
    pd.options.plotting.backend = "plotly"
    df.plot(x=[ 'Temperature2', 'Humidity2'], y='Date')
    df_melt = df.melt(id_vars='Date', value_vars=['Temperature2', 'Humidity2'])
    fig=px.line(df_melt, x='Date' , y='value' , color='variable')
    st.plotly_chart(fig)


