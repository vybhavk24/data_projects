## House Price Prediction

A machine learning project to predict house prices using regression models.  
Dataset used: [Kaggle California housing prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices).

---

### Project Workflow

1. **Data Loading & Exploration**  
   - Basic inspection, missing value analysis, correlation study.  

2. **Data Preprocessing**  
   - Handling missing values, encoding categorical variables, feature scaling.  

3. **Model Building**  
   - Trained and compared regression models: Linear Regression, Ridge Regression, Lasso Regression and Linear Regression with log-transformed target (log1p)

4. **Evaluation & Comparison**  
   - Compared models using RMSE, MAE, and R².  
   - Visualized performance.  

5. **Best Model Selection**  
   - Selected the best-performing model and saved it using `joblib`.  

---

### Results

- **Best Model**: Linear Regression 
- **Performance**: Achieved the highest Test R², outperforming Ridge, Lasso, and log-transformed models.