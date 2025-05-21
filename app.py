import streamlit as st
import plotly.express as px 

st.title("Mi segunda publicación")
st.header("Introducción")
st.write("Primera publicación en Streamlit")

fig = px.bar(x=["A", "B", "C"], y=[1, 3, 2])
st.plotly_chart(fig)
