# 🍽️ Mess Food Analytics Dashboard

## 📌 Project Overview
This project presents an end-to-end data engineering pipeline for analyzing hostel mess food consumption patterns using simulated data. It demonstrates data ingestion, processing, storage, and visualization through a simple web dashboard.

---

## ⚙️ Features
- Data ingestion from CSV files
- Data cleaning and transformation using Python (Pandas)
- Storage using SQLite database
- SQL-based data analysis
- Interactive dashboard using Streamlit

---

## 🏗️ Project Structure

mess-food-analytics/
│
├── data/
│   └── meal_data.csv
│
├── scripts/
│   ├── etl_pipeline.py
│   └── queries.py
│
├── app/
│   └── app.py
│
├── mess.db
├── requirements.txt
└── README.md

---

## 🚀 How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run ETL pipeline
```bash
python scripts/etl_pipeline.py
```

### 3. Launch dashboard
```bash
streamlit run app/app.py
```

---

## 📊 Dataset
The dataset used in this project is simulated to represent realistic hostel food consumption patterns, including food items, ratings, and student energy levels.

---

## 🛠️ Technologies Used
- Python
- Pandas
- SQLite
- Streamlit
- Matplotlib

---

## 📈 Key Insights
- Identifies most popular food items
- Analyzes average ratings per food
- Shows satisfaction distribution
- Visualizes food consumption trends

---

## 🔮 Future Enhancements
- Real-time data ingestion using APIs or Kafka
- Large-scale processing using Apache Spark
- Deployment on cloud platforms (AWS/GCP/Azure)
- Advanced analytics and machine learning integration

---

## ✅ Conclusion
This project successfully demonstrates a complete data pipeline from raw data ingestion to final visualization through a user-friendly dashboard interface.