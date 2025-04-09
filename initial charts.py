import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned dataset
df = pd.read_csv("filtered_dataset.csv")

numeric_cols = df.select_dtypes(include='number').columns

# Summary of numerical data
print(df.describe())

# Summary of categorical data (if any)
print(df.describe(include='object'))

# Histogram for SAT scores
plt.figure(figsize=(8, 5))
sns.histplot(df['SAT_AVG'].dropna(), kde=True)
plt.title("Distribution of Average SAT Scores")
plt.xlabel("SAT_AVG")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: SAT vs Admission Rate
plt.figure(figsize=(8, 5))
sns.scatterplot(x='SAT_AVG', y='ADM_RATE_ALL', data=df)
plt.title("SAT Score vs Admission Rate")
plt.xlabel("Average SAT Score")
plt.ylabel("Admission Rate")
plt.show()

# Correlation heatmap (numerical features only)
plt.figure(figsize=(12, 10))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.show()
