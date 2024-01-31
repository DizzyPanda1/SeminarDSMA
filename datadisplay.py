import pandas as pd 
import streamlit as st

import plotly.express as px

try:
    data = pd.read_csv("cleanedtranslations.csv",  engine="python")
except pd.errors.ParserError as e:
    print("Error reading CSV file:", e)
    # Add additional debugging information, if needed
    # For example, you can print the problematic row
    with open("cleanedtranslations.csv", "r") as file:
        lines = file.readlines()
        problematic_row = lines[2]  # Assuming the issue is in the third line
        print("Problematic row:", problematic_row)
    # Handle the exception or exit gracefully
    st.error("Error reading CSV file. Please check the file format.")
    st.stop()


turnover = pd.read_csv("turnover_by_label.csv")
returns = pd.read_csv("returns_by_label.csv")

lab = st.selectbox('Passion Brand:', options = data.label.unique())

subset = data[data.label == lab]
metrics = st.container()
mcol1, mcol2, mcol3 = metrics.columns(3)


mcol1.metric("Number of Reviews: ", len(subset['label']))
mcol2.metric("Negative To Positive Ratio: ", round(len(subset[subset.note <=3])/len(subset[subset.note >3]), 3))
mcol3.metric("Average Score: ", round(subset.note.mean(), 2))

counter = subset.groupby([pd.to_datetime(subset['the_date_transaction']).dt.isocalendar().week, pd.to_datetime(subset['the_date_transaction']).dt.isocalendar().year]).body.count().reset_index(drop = False)


main = st.container()
col1, col2 = main.columns([2,1])


fig= px.line(counter,x = counter.index,  y= "body", title = "Number of reviews per day")

fig.update_layout(
    xaxis_title="Date", yaxis_title="Reviews"
)

notechart = subset.groupby("note", ).note.count()
fig3 = px.bar(notechart, y = "note", title = "Note Distribution", color=notechart.index ,color_continuous_scale='matter')


col1.plotly_chart(fig)
stars = col1.selectbox("Stars: ", options = [1,2,3,4,5])
sub = subset[subset.note == stars]

acounter= sub.groupby(pd.to_datetime(sub['the_date_transaction']).dt.date).note.count().reset_index(drop = False)
fig2 = px.bar(acounter,x = acounter['the_date_transaction'],  y= "note", title = f"Number of {stars} star reviews per day")
col1.plotly_chart(fig2)
col2.plotly_chart(fig3, use_container_width=True)


second = st.container()


turnover_sub = turnover[turnover['label'] == lab]
returns_sub = returns[returns['label'] == lab]

fig4 = px.line(turnover_sub, x= "the_date_transaction", y = "turnover")

fig5 =  px.line(returns_sub, x= "the_date_transaction", y ="turnover_x" ,title = f"Daily Returns for {lab}",  color_discrete_sequence=['orangered'])
fig6 =  px.line(returns_sub, x= "the_date_transaction", y ="turnover_y",title = f"Daily Sales for {lab}", color_discrete_sequence=['lightgreen'])

fig5.update_layout(
    xaxis_title="Date", yaxis_title="Returns"
)

fig6.update_layout(
    xaxis_title="Date", yaxis_title="Sales"
)
second.plotly_chart(fig4)
second.plotly_chart(fig5)
second.plotly_chart(fig6)


