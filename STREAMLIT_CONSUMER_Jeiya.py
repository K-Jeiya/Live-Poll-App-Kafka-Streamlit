import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd 
from collections import Counter

# kafka setup 
topic = "live_poll_responses"
bootstrap_servers=['localhost:9092']

# create kafka consumer 
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='jeiya_streamlit_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# list of store messages 
messages = []
# continously read messages from kafka 
for message in consumer:
    data = message.value 
    messages.append(data)
    print(data)
    if len(messages) >= 5:
        break

# convert collected messages into a list of simple rows 
rows = []
for msg in messages:
    row = {"answer_id": msg["answer_id"], 
           "Q1": list(msg["answer_array"][0].values())[0], 
           "Q2": list(msg["answer_array"][1].values())[0], 
           "Q3": list(msg["answer_array"][2].values())[0]}
    rows.append(row)
    # print(rows)

# convert list of rows to dataframs
df = pd.DataFrame(rows)

st.set_page_config(page_title="Live Poll Dashboard", page_icon="📊", layout="wide")

# sidebar
st.sidebar.title("🎤 Event Poll")
st.sidebar.write("Live Polling Visualization")

# streamlit title 
st.title("📊 Live Poll Dashboard - Jeiya")

# 1. KPI in 3 cards horizantally 
col1, col2 = st.columns(2)
with col1: 
    st.metric("Total Responses", len(df["answer_id"].unique()))
with col2:
    st.metric("Unique Questions", df.shape[1] - 1)

# 2. show raw data 
st.markdown("### 📋 Raw Responses")
st.dataframe(df)

# Charts section
st.markdown("### 📈 Poll Charts/Summary")

st.subheader("Q1: Conference Overall Rating (1-5)")
st.bar_chart(df["Q1"].value_counts().sort_index())

st.subheader("Q2: Keynote Speaker Rating")
st.bar_chart(df["Q2"].value_counts())

st.subheader("Q3: Informative Sessions?")
st.bar_chart(df["Q3"].value_counts())

# Stylish footer
st.markdown("""
---
<div style='text-align:center;font-size:14px;color:gray;margin-top:20px;'>
    © 2025 Live Poll Dashboard <br>
    Made with ❤️ by <b>Jeiya Kumari</b>
</div>
""", unsafe_allow_html=True)