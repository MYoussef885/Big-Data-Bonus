import sys
import pandas as pd

def load_data(file_path):
    # Load the dataset
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        print(f"Data preview:\n{data.head()}")
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)
    return data

if __name__ == "__main__":
    # Get the file path from command-line arguments
    file_path = sys.argv[1]
    # Load the dataset
    data = load_data(file_path)
    # Save the loaded data for the next stage
    output_path = '/home/doc-bd-a1/loaded_data.csv'
    data.to_csv(output_path, index=False)
    print(f"Data loaded and saved to {output_path}")
