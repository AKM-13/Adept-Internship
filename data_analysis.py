import pandas as pd
from sklearn.model_selection import train_test_split

file_path = 'C:\Users\Admin\OneDrive\Desktop\internship\stackoverflow_full.csv'  
df = pd.read_csv(file_path)

mean = df.mean()
median = df.median()
mode = df.mode().iloc[0]
min_value = df.min()
max_value = df.max()
distinct_count = df.nunique()
total_count = df.count()
stats = df.describe(percentiles=[0.75])

print("Mean:\n", mean)
print("Median:\n", median)
print("Mode:\n", mode)
print("Min:\n", min_value)
print("Max:\n", max_value)
print("Distinct Count:\n", distinct_count)
print("Total Count:\n", total_count)
print("Statistics including 75th percentile:\n", stats)

def assess_correlation(df, col1, col2):
    correlation = df[col1].corr(df[col2])
    return correlation

col1 = 'PreviousSal'  
col2 = 'YearsCode'  
correlation_value = assess_correlation(df, col1, col2)
print(f"Correlation between {col1} and {col2}: {correlation_value}")


train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print("Training Set:\n", train_df.head())
print("Testing Set:\n", test_df.head())
