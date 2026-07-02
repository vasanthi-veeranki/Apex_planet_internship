import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/vasan/Downloads/vasanthi/cleaned_superstore.csv")

# Display first rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Check duplicates
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("C:/Users/vasan/Downloads/vasanthi/cleaned_superstore.csv", index=False)

print("Data cleaning completed successfully!")