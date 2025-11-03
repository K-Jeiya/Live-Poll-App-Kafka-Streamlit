# 🗳️ Live Poll App – Real-Time Streaming with Kafka & Streamlit

A real-time poll visualization app built with Apache Kafka, Python, and Streamlit.  
This project demonstrates how data streaming and live dashboards can be integrated to visualize audience poll responses dynamically as they arrive.

---

### 🎯 Overview
The Live Poll App simulates live audience voting where poll responses are produced by a Kafka producer and visualized instantly through a Streamlit dashboard.  
It represents a complete data engineering mini-project combining **data ingestion**, **stream processing**, and **real-time analytics**.

---

### ⚙️ Features
- Real-time updates: Poll responses stream live through Kafka.
- Dynamic charts: Bar charts for each question auto-update on new data.
- KPI metric: Displays total response count using Streamlit metric widget.
- Data table: Shows all responses in a live-updating table.
- Footer: “App created by Jeiya Kumari” for branding and ownership.
- Clean and modern Streamlit dashboard layout.

---

### 🧩 Project Structure
| File | Description |
|------|--------------|
| `PollResponseAPI.py` | Generates fake poll responses for Kafka testing. |
| `KAFKA_PRODUCER_Jeiya.py` | Kafka producer script that sends data to topic. |
| `STREAMLIT_CONSUMER_Jeiya.py` | Streamlit consumer app that reads Kafka data and updates dashboard. |

---

### 🧠 Tech Stack
- **Apache Kafka** – Message streaming and real-time data flow  
- **Python** – Core programming and producer logic  
- **Streamlit** – Live dashboard and data visualization  
- **JSON** – Poll data schema  
- **Localhost / Kafka Server** – Backend message broker setup

---

### 🚀 How to Run the App

```bash
# 1. Start Zookeeper and Kafka services
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

# 2. Create a Kafka topic
kafka-topics.sh --create --topic poll-responses --bootstrap-server localhost:9092

# 3. Run the producer (simulates poll data)
python KAFKA_PRODUCER_Jeiya.py

# 4. Run the consumer dashboard
streamlit run STREAMLIT_CONSUMER_Jeiya.py
