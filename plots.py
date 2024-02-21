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
            Page("plots.py", "3D Plots", "📊"),
            Page("returns.py", "Returns", "📦")
        ]
        )
    

datasets = {
    "Hiking" : pd.read_csv("Hiking.csv"),
    "Biking" : pd.read_csv("Biking.csv"),
    "Fitness" : pd.read_csv("Fitness.csv"),
    "Snow" : pd.read_csv("Snow.csv"),
    "Water" : pd.read_csv("Water.csv")
}





with st.container():
    col1, col2 = st.columns([1, 1])
    dpt = col1.selectbox(
        "Choose a department",
        ("Hiking", "Biking", "Snow", "Water", "Fitness")
    )
    data = datasets[dpt]
    type = col2.radio("Choose the type of plot", [1,2], horizontal=True)

if type==1:
    with st.container():
        note = st.slider("select the score:", 1,5)
        data = data[data.note == note]
        fig = px.scatter_3d(
            data, x='x', y='y', z='z',
            color=data["topic_name"] ,
            hover_data=['translated', 'turnover'])
        fig.update_traces(marker_size=4)

        st.plotly_chart(fig, use_container_width=True)

elif type==2:
    with st.container():
        fig = px.scatter_3d(
            data, x='x1', y='y1', z='note',
            color=data["topic_name"] ,
            hover_data=['translated', 'turnover'])
        fig.update_traces(marker_size=4)

        st.plotly_chart(fig, use_container_width=True)

elif type==3:
    with st.container():
        topic =  st.selectbox("select the score:", list(data.topic_name.unique()) )
        data = data[data.topic_name == topic]
        note = st.slider("select the score:", 1,5)
        data = data[data.note == note]
        fig = px.scatter_3d(
            data, x='x', y='y', z='z',
            color=data["the_to_type"],
            hover_data=['translated', 'turnover'])
        fig.update_traces(marker_size=4)

        st.plotly_chart(fig, use_container_width=True)
