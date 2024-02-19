import streamlit as st
import pandas as pd 
from st_pages import Page, add_page_title, show_pages
import plotly.express as px

st.set_page_config(layout="wide")
with st.sidebar:
    st.title("Decathlon Project - Group 6")

    show_pages(
        [
            Page("finaldashboard.py", "Report", "🏠"),
            Page("pages/plots.py", "3D Plots", "📈"),
            Page("pages/returns.py", "Returns", "📈")
        ]
        )
    

returns = pd.read_csv("returns_by_label.csv")
lab = st.selectbox("Choose a department: ", ['Hiking', 'Biking', 'Snow Sports', 'Water Sports', 'Fitness and Yoga'])
data = returns[returns.label == lab]
st.plotly_chart(px.line(data, x= "the_date_transaction", y ="turnovery",title = f"Daily Sales for {lab}", color_discrete_sequence=['lightgreen']),  use_container_width=True)
st.plotly_chart(px.line(data, x= "the_date_transaction", y ="turnoverx" ,title = f"Daily Returns for {lab}",  color_discrete_sequence=['orangered']), use_container_width=True)
