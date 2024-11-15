import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Update 'columnX' and 'columnY' with actual column names from SVMtrain.csv
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Pclass', y='Survived', data=data)  # Replace 'columnX' and 'columnY'
plt.title("Scatter Plot of Pclass vs Survived")  # Update title accordingly
plt.savefig("/home/doc-bd-a1/vis.png")

print("Visualization saved as vis.png")
