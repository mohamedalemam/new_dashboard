import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('tips.csv')

st.set_page_config(page_title= 'Tips Dashboard',
                   layout= 'wide',
                   initial_sidebar_state= 'expanded')

# Sidebar
st.sidebar.header('Tips Dashboard')
st.sidebar.image('Putting.jpg')
st.sidebar.write("this dashboard is using dataset tips")

# Body

# row 1
a1, a2, a3, a4 = st.columns(4)

a1.metric("Max of Total Bill", df['total_bill'].max())
a2.metric("Min of Total Bill", df['total_bill'].min())
a3.metric("Max of Tips", df['tip'].max())
a4.metric("Min of Tips", df['tip'].min())

cat_filtering = st.sidebar.selectbox('Categorical Filtering', [None, 'sex', 'smoker', 'day', 'time'])
num_filtering = st.sidebar.selectbox('Numerical Filtering', [None, 'total_bill', 'tip'])
st.sidebar.write("")
st.sidebar.markdown("this dashboard created by [Mohamed Alemam](https://www.youtube.com/channel/UCzDyvjVaOqfPnpQAfP8dTWQ)")

# row 2

fig = px.scatter(data_frame= df,
                 x= 'total_bill',
                 y= 'tip',
                 color= cat_filtering,
                 size= num_filtering)
st.plotly_chart(fig, use_container_width= True)

# row 3
c1, c2, c3 = st.columns((4, 3, 3))

with c1:
    st.text('Sex vs Total Bill')
    fig = px.bar(data_frame= df, x= 'sex', y= 'total_bill', color= cat_filtering)
    st.plotly_chart(fig, use_container_width= True)

with c2:
    st.text('Smoker/non smoker vs Tips')
    fig = px.pie(data_frame= df, names= 'smoker', values= 'tip', color= cat_filtering)
    st.plotly_chart(fig, use_container_width= True)

with c3:
    st.text('Day vs. Tips')
    fig = px.pie(data_frame= df, names='day', values='tip', color= cat_filtering, hole= 0.3)
    st.plotly_chart(fig, use_container_width= True)
