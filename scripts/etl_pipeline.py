import pandas as pd
import sqlite3

# Load data
df = pd.read_csv("data/meal_data.csv")

# Clean
df['food_item'] = df['food_item'].str.strip()

# Transform
def categorize(rating):
    if rating >= 4:
        return "Good"
    elif rating == 3:
        return "Average"
    else:
        return "Poor"

df['satisfaction'] = df['rating'].apply(categorize)

# Load into DB
conn = sqlite3.connect("mess.db")
df.to_sql("meals", conn, if_exists="replace", index=False)

conn.close()

print("ETL Completed!")