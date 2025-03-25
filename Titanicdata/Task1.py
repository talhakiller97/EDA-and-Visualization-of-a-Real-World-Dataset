import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display the first few rows and general information about the dataset
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
df.info()


print("\nMissing values per column:")
print(df.isnull().sum())

# Impute 'Age' with the median value
df['Age'].fillna(df['Age'].median(), inplace=True)

df.dropna(subset=['Embarked'], inplace=True)
df.dropna(subset=['Cabin'], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)



# Checking for duplicates
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

#Identify and manage outliers using IQR for 'Fare'
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers in 'Fare'
df_filtered = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]

# Display dataset shape before and after removing outliers
print("\nShape of dataset before and after removing outliers:")
print(f"Before: {df.shape}")
print(f"After: {df_filtered.shape}")


# Bar chart for 'Survived'
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived')
plt.title('Survival Count')
plt.show()

# Bar chart for 'Pclass'
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Pclass')
plt.title('Class Distribution')
plt.show()

# Bar chart for 'Sex'
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Sex')
plt.title('Gender Distribution')
plt.show()



# Histogram for 'Age'
plt.figure(figsize=(6, 4))
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Histogram for 'Fare'
plt.figure(figsize=(6, 4))
sns.histplot(df['Fare'], kde=True)
plt.title('Fare Distribution')
plt.show()

# Correlation heatmap for numeric features
corr_matrix = df[['Age', 'Fare', 'Pclass', 'SibSp', 'Parch']].corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Step 4: Summarize Insights

# My Findings:
print("\nExploratory Data Analysis Insights:")
print("1. Survival Rate: The survival rate was approximately 38%, with more women surviving than men.")
print("2. Age Distribution: The majority of passengers were between 20 and 40 years old, with a few younger children and older adults.")
print("3. Fare Distribution: The majority of fares were concentrated in the lower range, but there were a few passengers who paid very high fares.")
print("4. Correlations: There’s a negative correlation between 'Fare' and 'Pclass' (higher class corresponds to higher fare), and a small positive correlation between 'SibSp' and 'Parch' (the number of siblings/spouses aboard and parents/children aboard).")
