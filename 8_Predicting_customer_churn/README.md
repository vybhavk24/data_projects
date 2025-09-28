## Customer Churn Prediction

### Project Overview

This project builds a machine learning pipeline to predict customer churn for a telecommunications company using structured customer data. Customer churn occurs when customers cancel or do not renew their subscriptions, which directly impacts company revenue. The goal is to predict whether a customer is likely to churn based on their service usage, account information, and demographics, enabling proactive customer retention strategies.

---

### Dataset

- The dataset used is the **Telco Customer Churn Dataset**, which contains customer demographic information, account details, and service usage.
- Key features include tenure, monthly and total charges, contract type, payment method, internet service, and various service-related attributes.
- The target variable `Churn` indicates whether the customer has churned (`Yes` or `No`).

---

### Exploratory Data Analysis (EDA)

- The dataset was first loaded and examined for missing values and data types.
- The `TotalCharges` column was converted to numeric, with missing values imputed using the median.
- The `customerID` column was dropped as it provides no predictive value.
- Target distribution showed ~26.5% churn rate, indicating class imbalance.
- Churn rates by contract type revealed higher churn for month-to-month contracts (~42.7%) vs. one year (~11.3%) or two year (~2.8%) contracts.
- Numeric and categorical feature columns were identified to enable tailored preprocessing.

---

### Data Preprocessing

- Numeric features (`tenure`, `MonthlyCharges`, `TotalCharges`, `SeniorCitizen`) were imputed with median values and standardized using `StandardScaler`.
- Categorical features were imputed with the most frequent value and one-hot encoded.
- Scikit-learn's `ColumnTransformer` was used to apply these transformations appropriately for each feature type.

---

### Modeling

- Data was split into training (80%) and test (20%) sets with stratified sampling to preserve class distribution.
- Two main models were evaluated:
  - **Logistic Regression** with balanced class weights.
  - **Random Forest Classifier** with hyperparameter tuning via `RandomizedSearchCV` optimizing ROC AUC.
- The Random Forest model's best parameters included 100 trees with max depth 8, minimum samples split 5, and leaf size 1.
- Model evaluation metrics included accuracy, precision, recall, f1-score, and ROC AUC.
- Confusion matrices and ROC curves were used for visual performance analysis.

---

### Addressing Class Imbalance

- Synthetic Minority Over-sampling Technique (SMOTE) was integrated into the pipeline using `imblearn` to augment the minority class in training.
- SMOTE-enhanced Random Forest achieved improved balance in precision and recall metrics for the churn class.
- The SMOTE pipeline offered better trade-off performance on test data compared to models without it.

---

### Feature Importance

- Feature importance from the Random Forest model revealed that top factors influencing churn included:
  - Tenure
  - Contract type (especially month-to-month contracts)
  - TotalCharges
  - OnlineSecurity status
  - MonthlyCharges
  - InternetService type
- These insights align with domain expectations and can guide targeted retention efforts.

---

### Deployment

- The final trained model pipeline, including preprocessing and classifier, was saved using `joblib` for reuse.
- A feature schema JSON was stored to validate input data on inference.
- A Flask web application was developed to:
  - Provide a web form interface for manual churn prediction.
  - Expose a REST API endpoint accepting JSON inputs for programmatic access.
- The Flask app sanitizes and processes inputs, performs predictions with the saved pipeline, and returns results with churn probability and classification.
- Frontend templates (`index.html` and `result.html`) use Bootstrap for a responsive, user-friendly UI.

---

### How to Run the Project

1. **Environment setup**:  
   - Create and activate a Conda environment with required packages: pandas, scikit-learn, imbalanced-learn, Flask, joblib, etc.  
   - Example command to run the Flask app locally:  
     ```
     conda activate churn
     python -m flask run
     ```
2. **Access the web app**:  
   - Open a browser and visit `http://127.0.0.1:5000` to input customer data and receive churn predictions.  
3. **API usage**:  
   - Send JSON requests to `/api/predict` endpoint with required features and receive JSON response with predictions.

---

### Results Summary

- Churn class distribution showed about 26.5% customers churned.
- Logistic Regression baseline achieved ~74% accuracy and ROC AUC ~0.84.
- Tuned Random Forest improved accuracy to ~76% with similar ROC AUC.
- SMOTE-enhanced Random Forest improved balanced classification scores.
- Top predictors highlighted contract type, tenure, and charges.
- The saved pipeline enables consistent, reproducible inference through the Flask app.

---

### Future Work

- Experiment with additional models like XGBoost, LightGBM, or deep learning approaches.
- Incorporate more business-specific features if available (e.g., customer service interactions).
- Develop dashboards to visualize churn risk and feature contributions.
- Deploy the app with authentication and logging for production use.
- Integrate with customer relationship management (CRM) systems for automated intervention.

---

### Acknowledgments

- Dataset sourced from [Telco Customer Churn Dataset](https://www.kaggle.com/code/danishmubashar/telco-customer-churn-99-acc/input).
- Uses open-source tools including scikit-learn, imbalanced-learn, Flask, Bootstrap.
- Developed as a complete end-to-end churn prediction demo combining machine learning and deployment.