import pandas as pd
import os

# -----------------------------
# Create processed folder
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# Load dataset
# -----------------------------
file_path = "data/shopnest_fashion_dataset_500_products.xlsx"

df = pd.read_excel(file_path)

print("Dataset Loaded Successfully!\n")

# -----------------------------
# Dataset Information
# -----------------------------
print("Shape :", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Remove duplicate rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Fill missing values
# -----------------------------
for column in df.columns:

    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(df[column].median())

    else:
        df[column] = df[column].fillna("Unknown")

# -----------------------------
# Clean column names
# -----------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# -----------------------------
# Save cleaned dataset
# -----------------------------
output_path = "data/processed/cleaned_fashion_products.xlsx"

df.to_excel(output_path, index=False)

print("\nDataset Cleaned Successfully!")
print("Saved at :", output_path)