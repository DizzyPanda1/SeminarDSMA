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
            Page("pages/returns.py", "Why Returns?", "📈")
        ]
        )
    
