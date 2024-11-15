import pandas as pd

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Generate EDA insights with the correct column names (replace 'column1', 'column2', etc.)
insights = [
    f"Total records: {len(data)}",
    f"Mean of column1: {data['Survived'].mean()}",       # Update 'column1' to a relevant numeric column
    f"Median of column2: {data['Pclass'].median()}",   # Update 'column2' to a relevant numeric column
    f"Unique values in column3: {data['SibSp'].nunique()}",  # Update 'column3' if relevant
]

# Save insights to text files
for i, insight in enumerate(insights, start=1):
    with open(f"/home/doc-bd-a1/eda-in-{i}.txt", "w") as file:
        file.write(insight)

print("EDA insights saved to eda-in-1.txt, eda-in-2.txt, etc.")
