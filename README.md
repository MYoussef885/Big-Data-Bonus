### Big Data Assignment



### **Requirements**
- **Docker**
- **Dataset**: SVMtrain.csv

---

### **Project Structure**
- **Dockerfile**: Defines the Docker container setup with the necessary packages.
- **load.py**: Loads the dataset and saves it as `loaded_data.csv`.
- **dpre.py**: Handles data cleaning, transformation, dimensionality reduction, and discretization, saving the results as `res_dpre.csv`.
- **eda.py**: Conducts exploratory data analysis and saves insights in `eda-in-1.txt`, `eda-in-2.txt`, and `eda-in-3.txt`.
- **vis.py**: Generates visualizations and saves them as `vis.png`.
- **model.py**: Applies K-means clustering with `k=3` and saves the cluster counts in `k.txt`.

---

### **Setup and Execution**

#### 1. **Build the Docker Image**
From the directory containing the Dockerfile, run:
```bash
docker build -t bd-a1-image .
```

---

#### 2. **Run the Docker Container**
Start the container and access the shell:
```bash
docker run -it --name bd-a1-container bd-a1-image
```

---

#### 3. **Execute the Pipeline**
Inside the container, navigate to `/home/doc-bd-a1/` and execute the following scripts in sequence:

1. **Load the Data**  
   ```bash
   python3 load.py /home/doc-bd-a1/SVMtrain.csv
   ```

2. **Preprocess the Data**
   ```bash
   python3 dpre.py
   ```

3. **Perform EDA**
   ```bash
   python3 eda.py
   ```

4. **Generate Visualization**
   ```bash
   python3 vis.py
   ```

5. **Apply K-means Clustering**
   ```bash
   python3 model.py
   ```

---

#### 4. **Copy Output Files to Your Local Machine**
After running the pipeline, copy the generated files from the container to the `service-result` directory on your machine:
```bash
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt service-result/
```

---

### **Output Files**
- **res_dpre.csv**: Preprocessed dataset.
- **eda-in-1.txt**, **eda-in-2.txt**, **eda-in-3.txt**: Results of the exploratory data analysis.
- **vis.png**: Visualization plot.
- **k.txt**: Cluster counts from K-means clustering.

---

### **Troubleshooting**
- Verify that all Python scripts are located in the `/home/doc-bd-a1/` directory within the container before execution.
- Use Unix-style file paths for datasets and output files (e.g., `/home/doc-bd-a1/SVMtrain.csv`).

---

### **Bonus (Optional)**

1. **Push Docker Image to Docker Hub**  
   ```bash
   docker tag bd-a1-image mohamed885/bd-a1-image
   docker push mohamed885/bd-a1-image
   ```

2. **Upload the Project to GitHub**  
   - Create a new repository on GitHub.
   - Add your project files, commit, and push them to the repository.
