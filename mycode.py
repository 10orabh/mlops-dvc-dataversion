import pandas as pd
import os

# 1️⃣ Sample data
data = {
    "id": [1, 2, 3, 4],
    "name": ["Aman", "Riya", "Rahul", "Neha"],
    "age": [23, 25, 22, 24],
    "city": ["Indore", "Bhopal", "Delhi", "Pune"]
}

# 2️⃣ Create DataFrame
df = pd.DataFrame(data)

# 4️⃣ Add new row
new_row = {
    "id": 5,
    "name": "Ankit",
    "age": 26,
    "city": "Mumbai"
}


df.loc[len(df)] = new_row
# 4️⃣ Create data folder path
data_dir = "data"

# 5️⃣ Create data folder if not exists
os.makedirs(data_dir, exist_ok=True)

# 6️⃣ Final file path
file_path = os.path.join(data_dir, "sampledata.csv")
# 7️⃣ Save CSV inside data folder
df.to_csv(file_path, index=False)

print("✅ CSV file saved successfully!")
print("📁 Location:", file_path)
