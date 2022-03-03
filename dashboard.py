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

df=pd.read_csv('https://raw.githubusercontent.com/subham27-07/Studio-LNGR/main/sensors_output2.csv')

st.title ("StudioLNGR AMPS system Dashboard")
# st.sidebar.title("Analysis of Tweets")
st.markdown("This application is a Streamlit dashboard used to AMPS system")
# st.sidebar.markdown("This application is a Strea

st.write(df.head(10))

# select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='1')


# if select == 'SoilMoisture':

#     fig = px.scatter(df, x=df['Soil Moisture'], y=df['Date'], marginal_x="histogram", marginal_y="rug", width=700,height=900)

#     # z= spectra_df['score'].plot()
#     st.plotly_chart(fig)


# select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'))

# if select == 'VOC':

#     fig = px.line(df, x=df['Date'], y=df['Temeprature1','Humidity1','Temperature2','Humidity2','Soil Moisture','VOC','CO2'],color=df['Temeprature1','Humidity1','Temperature2','Humidity2','Soil Moisture','VOC','CO2'], width=700,height=900)

#     # z= spectra_df['score'].plot()
#     st.write(fig)

# select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='2')

# if select == 'CO2':

#     fig = px.scatter(df, x=df['CO2'], y=df['Date'], marginal_x="histogram", marginal_y="rug", width=700,height=900)

#     # z= spectra_df['score'].plot()
#     st.plotly_chart(fig)

# select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='3')

# if select == 'Temeprature1 & Humidity1':
    
pd.options.plotting.backend = "plotly"
df.plot(x='Date', y=[ 'Temperature1','Humidity1','Temperature2','Humidity2','Soil Moisture','VOC','CO2'])
df_melt = df.melt(id_vars='Date', value_vars=['Temperature1','Humidity1','Temperature2','Humidity2','Soil Moisture','VOC','CO2'])
fig=px.line(df_melt, x='Date' , y='value' , color='variable',width=1200,height=500)
    
st.plotly_chart(fig)
    


# select= st.selectbox( '',('Temeprature1 & Humidity1','Temeprature2 & Humidity2' , 'SoilMoisture', 'VOC', 'CO2'), key='4')
# if select == 'Temeprature2 & Humidity2':
#     pd.options.plotting.backend = "plotly"
#     df.plot(x=[ 'Temperature2', 'Humidity2'], y='Date')
#     df_melt = df.melt(id_vars='Date', value_vars=['Temperature2', 'Humidity2'])
#     fig=px.line(df_melt, x='Date' , y='value' , color='variable')
#     st.plotly_chart(fig)




fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Date'], y=df['Temperature1'],
                    mode='lines+markers',
                    name='Temperature1'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Humidity1'],
                    mode='lines+markers',
                    name='Humidity1'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Temperature2'],
                    mode='lines+markers',
                    name='Temperature2'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Humidity2'],
                    mode='lines+markers',
                    name='Humidity2'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['Soil Moisture'],
                    mode='lines+markers',
                    name='Soil Moisture'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['VOC'],
                    mode='lines+markers',
                    name='VOC'))

fig.add_trace(go.Scatter(x=df['Date'], y=df['CO2'],
                    mode='lines+markers',
                    name='CO2'))



# fig.show()
st.write(fig)
