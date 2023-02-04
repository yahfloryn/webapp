import pandas as pd
import streamlit as st
import plotly.express as px
from  PIL import Image
import os

folder = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title='Excel Quant')
st.header('ExcelGetData')
st.subheader('Qantitative data Table')

### ---- LOAD DATAFRAME 
excel_file = os.path.join(folder, 'Quant_Database.xlsm')
sheet_name = 'Database'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                    ### --- usecols='A,B,C,F,H,I',
                    usecols='C:H',
                    header=32)
st.dataframe(df)