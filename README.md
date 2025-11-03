# 🗳️ Live Poll App – Real-Time Streaming with Kafka & Streamlit

A real-time poll visualization app built with **Apache Kafka**, **Python**, and **Streamlit**.  
This project demonstrates how live data can be streamed, processed, and visualized instantly through an interactive dashboard.

---

### 🎯 Overview
The **Live Poll App** simulates a real-world scenario where audience votes are streamed live using Kafka and visualized dynamically in Streamlit.  
It’s a hands-on example of **real-time data engineering** combining ingestion, stream processing, and visualization.

---

### ⚙️ Features
- 🔄 **Real-Time Updates** – Poll data streams live via Kafka
- 📊 **Dynamic Charts** – Auto-updating bar charts for each question
- 🧮 **KPI Metrics** – Shows total response count in real time
- 🧾 **Data Table** – Displays all responses as they arrive
- 🧑‍💻 **Footer Branding** – “App created by Jeiya Kumari”
- 🎨 **Clean Streamlit Dashboard** – Simple, elegant, and responsive UI

---

### 🧩 Project Structure
| File | Description |
|------|--------------|
| `PollResponseAPI.py` | Simulates fake poll responses for Kafka. |
| `KAFKA_PRODUCER_Jeiya.py` | Sends poll responses to Kafka topic. |
| `STREAMLIT_CONSUMER_Jeiya.py` | Streamlit app consuming Kafka messages & visualizing data. |

---

### 🧠 Tech Stack
- **Apache Kafka** → Real-time data streaming  
- **Python 3.x** → Core scripting language  
- **Streamlit** → Live dashboard and visualization  
- **JSON** → Poll data structure  
- **Kafka Broker / Zookeeper** → Backend message infrastructure

---

### 🚀 How to Run the App

```bash
# Step 1: Start Zookeeper and Kafka
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

# Step 2: Create a Kafka topic
kafka-topics.sh --create --topic poll-responses --bootstrap-server localhost:9092

# Step 3: Run the Producer (simulated data generator)
python KAFKA_PRODUCER_Jeiya.py

# Step 4: Run the Streamlit Dashboard (Consumer)
streamlit run STREAMLIT_CONSUMER_Jeiya.py
```
---

### 👩‍💻 Developer Information
**Name:** Jeiya Kumari  
📍 **Location:** Karachi, Pakistan  
📧 **Email:** [jeiyakumari@gmail.com](mailto:jeiyakumari@gmail.com)  
🔗 **LinkedIn:** [linkedin.com/in/jeiyakumari](https://www.linkedin.com/in/jeiyakumari/)  
🌐 **Portfolio:** [k-jeiya.github.io/Jeiya-Portfolio](https://k-jeiya.github.io/Jeiya-Portfolio/)

---

### 🧰 Tools Used
- Visual Studio Code  
- Apache Kafka  
- Streamlit  
- Python 3.x  
- JSON  
- GitHub  
- Command Line Interface  

---

### 🏷️ Tags
#Kafka #Streamlit #Python #DataEngineering #RealTimeData #Streaming #ProducerConsumer #Visualization #Dashboard #EventStreaming #ETL #BigData #JeiyaKumari #LivePollApp #DataPipeline #ApacheKafka #PythonProjects #StreamlitApp #AIProjects #TechPortfolio  

---

### 📚 Project Type
🗂️ **Data Engineering** · ⚙️ **Streaming Analytics** · 📡 **Real-Time Processing** · 🧩 **End-to-End Pipeline**

---

### ⭐ Summary
The **Live Poll App** demonstrates the real-time flow of data from production to visualization —  
Kafka produces messages, Streamlit consumes them, and users see instant live updates.  
It’s a professional example of **event-driven data streaming, Python integration, and live analytics**,  
perfect for showcasing **data engineering and dashboarding skills** in your portfolio.

---

💡 _“Built with ❤️ and caffeine by Jeiya Kumari”_
