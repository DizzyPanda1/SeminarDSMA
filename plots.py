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
            Page("pages/plots.py", "3D Plots", "📊"),
            Page("pages/returns.py", "Returns", "📦")
        ]
        )
    

    

with st.container():
    col1, col2 = st.columns([1, 1])
    dpt = col1.selectbox(
        "Choose a department",
        ("Hiking", "Biking", "Snow", "Water", "Fitness")
    )
    data = pd.read_csv(f"Subsets/{dpt}.csv")
    type = col2.radio("Choose the type of plot", [1,2], horizontal=True)

if type==1:
    with st.container():
        note = st.slider("select the score:", 1,5)
        data = data[data.note == note]
        fig = px.scatter_3d(
            data, x='x', y='y', z='z',
            color=data["topics"] ,
            hover_data=['translated', 'turnover'])
        fig.update_traces(marker_size=4)

        st.plotly_chart(fig, use_container_width=True)
elif type==2:
    with st.container():
        fig = px.scatter_3d(
            data, x='x1', y='y1', z='note',
            color=data["topics"] ,
            hover_data=['translated', 'turnover'])
        fig.update_traces(marker_size=4)

        st.plotly_chart(fig, use_container_width=True)