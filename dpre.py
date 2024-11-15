import pandas as pd

# Load the data from the previous stage
data = pd.read_csv('/home/doc-bd-a1/loaded_data.csv')

# Print the column names to verify them
print("Columns in loaded_data.csv:", data.columns)

# Data Cleaning: Fill missing values for numeric columns
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Data Transformation: Square root transformation on numeric columns (example)
for col in numeric_cols:
    data[col] = data[col].apply(lambda x: x if x <= 0 else x ** 0.5)

# Select specific columns with the correct names
data = data[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]  # Corrected column name

# Data Discretization: Binning one of the numeric columns
data['Survived_bin'] = pd.cut(data['Survived'], bins=3, labels=['Low', 'Medium', 'High'])

# Save the preprocessed data
data.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)
print("Preprocessed data saved to res_dpre.csv")
