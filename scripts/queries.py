import sqlite3

conn = sqlite3.connect("mess.db")
cursor = conn.cursor()

# Avg rating
print("\nAverage Rating per Food:")
for row in cursor.execute("""
SELECT food_item, AVG(rating)
FROM meals
GROUP BY food_item
"""):
    print(row)

# Satisfaction count
print("\nSatisfaction Count:")
for row in cursor.execute("""
SELECT satisfaction, COUNT(*)
FROM meals
GROUP BY satisfaction
"""):
    print(row)

conn.close()