import streamlit as st
import warnings
import pandas as pd
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)
st.set_page_config(page_title="Simplex Dashboard", page_icon=":bar_chart:", layout="wide")
warnings.filterwarnings('ignore')

st.title(" :bar_chart: Simplex Dashboard")
@st.cache_data
def load_data(file_path):
   
    df = pd.read_excel(file_path)
    return df

file_path = "Gurugram.xlsx" 
df = load_data(file_path)

search_term = st.text_input("Search by Property ID")

filtered_df = df[df['Property_ID'].str.contains(search_term)]
st.dataframe(filtered_df)