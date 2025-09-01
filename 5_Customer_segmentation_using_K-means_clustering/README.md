## Customer Segmentation Using K-Means Clustering

### Project Overview
This project performs customer segmentation on the "Mall_Customers.csv" dataset using the K-Means clustering algorithm. The goal is to group customers based on their demographic and behavioral features (age, annual income, and spending score) to identify distinct customer segments for targeted marketing strategies. 
The project is implemented in a Jupyter Notebook (`Customer_segmentation_using_K-means.ipynb`) using Python and includes data preprocessing, exploratory data analysis (EDA), clustering, evaluation, and visualization.

### Dataset
- **Source**: [Mall_Customers.csv](https://www.kaggle.com/code/mattop/mall-customers-k-means-clustering/input)
- **Columns**:
  - `CustomerID`: Unique identifier for each customer.
  - `Gender`: Customer's gender (Male/Female).
  - `Age`: Customer's age.
  - `Annual Income (k$)`: Annual income in thousands of dollars.
  - `Spending Score (1-100)`: Score assigned based on customer spending behavior.

### Project Structure
- **`Customer_segmentation_using_K-means.ipynb`**: Main Jupyter Notebook containing the entire workflow.
- **`outputs_kmeans_customer_segmentation/`**: Directory for output files, including:
  - `mall_customers_with_segments.csv`: Dataset with cluster labels.
  - `clusters_2d_income_spending.png`: 2D scatter plot of clusters (income vs. spending score).
  - `clusters_3d_pca2.png`: 2D PCA projection of 3D clusters (age, income, spending score).
  - Other visualizations (e.g., elbow plot, silhouette scores, histograms).

### Dependencies
The project uses the following Python libraries:
- `numpy`: Numerical operations.
- `pandas`: Data manipulation and analysis.
- `matplotlib`: 2D and 3D visualizations.
- `mpl_toolkits.mplot3d`: 3D plotting.
- `sklearn`: Machine learning tools (StandardScaler, KMeans, silhouette_score, PCA).
- `warnings`: Suppresses unnecessary warnings.

### Workflow
1. **Setup**:
   - Import libraries and configure settings (random seed for reproducibility, Matplotlib style, Pandas display options).
2. **Data Loading and Cleaning**:
   - Load `Mall_Customers.csv` into a Pandas DataFrame.
   - Standardize column names (lowercase, underscores, remove special characters).
   - Rename specific columns (e.g., "genre" to "gender", "annual_income_k$" to "annual_income_k").
   - Clean gender column values (strip spaces, convert to title case).
3. **Exploratory Data Analysis (EDA)**:
   - Check dataset structure, missing values, duplicates, and statistical summaries.
   - Visualize distributions of numerical features (age, income, spending score) using histograms.
4. **Data Preprocessing**:
   - Select numerical features for clustering: `age`, `annual_income_k`, `spending_score`.
   - Standardize features using `StandardScaler` to ensure equal contribution to clustering.
5. **K-Means Clustering**:
   - Perform clustering on 2D features (income, spending score) and 3D features (age, income, spending score).
   - Use the elbow method and silhouette scores to determine the optimal number of clusters (`k`).
   - Fit K-Means models and assign cluster labels to the dataset.
6. **Evaluation**:
   - Compute silhouette scores to assess cluster quality.
   - Visualize clusters using 2D scatter plots and 3D PCA projections.
7. **Outputs**:
   - Save the segmented dataset with cluster labels as CSV.
   - Save visualizations as PNG files for further analysis.

### Key Features
- **Reproducibility**: Fixed random state (`42`) ensures consistent results.
- **Robustness**: Handles dataset variations (e.g., column name differences) with conditional checks.
- **Visualizations**: Includes histograms, elbow plots, silhouette plots, 2D scatter plots, and 3D PCA projections.
- **Evaluation**: Uses silhouette scores to validate cluster quality.
- **Output Artifacts**: Saves segmented data and visualizations for easy sharing and analysis.

### Output Files
- **CSV**: `mall_customers_with_segments.csv` (dataset with cluster labels).
- **Images**:
  - `clusters_2d_income_spending.png`: 2D cluster plot (income vs. spending score).
  - `clusters_3d_pca2.png`: PCA projection of 3D clusters.
  - Additional plots (e.g., elbow method, silhouette scores) as generated during execution.

### Contact
For questions or feedback, please reach me via [Gmail](vybhavkvviet@gmail.com)