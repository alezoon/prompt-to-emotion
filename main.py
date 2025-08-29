from src.model import classifier
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Prompt to Emotion",
    layout="wide",
    initial_sidebar_state="collapsed"
)


with st.sidebar:
    st.header("Information")



prompt = st.text_input("Enter a Prompt")
run_button = st.button("Run Emotion Model", type="primary")


if run_button:
    if prompt != '':
        result = classifier(prompt)

    if result is not None:
        emotion = result[0]
        df = pd.DataFrame(emotion)
        df['percentage'] = df['score'] * 100

    fig = px.bar(
        df,
        x = 'label',
        y = 'percentage',
        color = 'label',
        text = df['percentage'].round(1).astype(str) + "%",
        title = "Emotion Bar Chart"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(yaxis_title="Percentage", xaxis_title="Emotion", showlegend=False)

    st.plotly_chart(fig, use_container_width=True)