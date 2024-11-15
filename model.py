import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Load the preprocessed data
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Encode non-numeric data in the 'Sex' column
if 'Sex' in data.columns:
    le_sex = LabelEncoder()
    data['Sex'] = le_sex.fit_transform(data['Sex'])  # Convert 'Sex' to numeric values (e.g., Male -> 0, Female -> 1)

# Verify all required features are present
required_columns = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    raise ValueError(f"Missing required columns in the dataset: {missing_columns}")

# Select features for clustering
features = data[required_columns]

# Apply K-means clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)  # Adding random_state for reproducibility
data['cluster'] = kmeans.fit_predict(features)

# Save the count of records in each cluster
cluster_counts = data['cluster'].value_counts()
with open('/home/doc-bd-a1/k.txt', 'w') as file:
    file.write(str(cluster_counts))

print("Cluster counts saved to k.txt")
