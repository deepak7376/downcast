import downcast as dc
import os
import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import joblib

jena = pd.read_csv("./jena_climate_2009_2016.csv")
jena_bd = np.round(jena.memory_usage().sum()/(1024*1024),1)
jena = dc.downcast(jena)
jena_ad = np.round(jena.memory_usage().sum()/(1024*1024),1)

dic = {'DataFrame':['jena'],
       'Before downcasting':[jena_bd],
       'After downcasting':[jena_ad]}

memory = pd.DataFrame(dic)
memory = pd.melt(memory, id_vars='DataFrame', var_name='Status', value_name='Memory (MB)')
memory.sort_values('Memory (MB)',inplace=True)
fig = px.bar(memory, x='DataFrame', y='Memory (MB)', color='Status', barmode='group', text='Memory (MB)')
fig.update_traces(texttemplate='%{text} MB', textposition='outside')
fig.update_layout(template='seaborn', title='Effect of Downcasting')
fig.show()