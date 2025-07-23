## Titanic Data Cleaning & Exploration

This is a beginner-friendly data analysis project I worked on using the Titanic dataset from Kaggle. The goal was to explore and understand survival patterns through basic data cleaning, preprocessing, and visualization — all using core Python libraries like Pandas, NumPy, Matplotlib, and Seaborn.

---

### What I Wanted to Learn

I wanted to get hands-on with:
- Handling missing data properly
- Encoding categorical features the right way
- Visualizing real-world data
- Drawing meaningful insights from basic exploratory analysis

This project lays the groundwork for any future work in data analytics or machine learning.

---

### Dataset Info

- Source: [Titanic - Machine Learning from Disaster (Kaggle)](https://www.kaggle.com/datasets/hesh97/titanicdataset-traincsv)
- File used: `train.csv`
- Columns: Passenger details like age, gender, ticket class, survival status, etc.

---

### What I Did (Step-by-Step)

1. **Explored the dataset**  
   - Checked shape, column types, nulls, and basic stats.

2. **Cleaned the data**  
   - Filled missing `Age` with the median  
   - Filled missing `Embarked` with the mode  
   - Dropped `Cabin`, `Name`, `Ticket`, and `PassengerId` for simplicity

3. **Encoded categorical features**  
   - Used one-hot encoding for `Sex` and `Embarked` columns

4. **Visualized survival patterns**  
   - Survival by gender, class, and age distribution  
   - Heatmap of feature correlation  
   - Combined group survival (`Pclass` vs `Sex`) to spot more nuanced trends

---

### Some Insights

- **Females had a significantly higher survival rate** than males.
- **First-class passengers** had the best survival chances.
- Passengers aged between **20 to 40** formed the largest group on board.
- Survival was heavily influenced by a mix of **gender and class** — for example, **females in 1st class had the highest chance** of survival.

---

### Tools & Libraries

- `pandas` and `numpy` for data wrangling  
- `seaborn` and `matplotlib` for plotting  
- Jupyter Notebook for the full workflow

---

### What This Project Shows

This isn't just about the Titanic — it’s about learning to treat messy real-world data with respect, clean it up, and draw actionable insights. This project helped me build the foundational mindset I’ll carry forward in future analytics, data science, and machine learning work.

---

### Next Steps (In-future)

Not part of this phase, but I might come back and:
- Build a basic predictive model (like logistic regression)
- Try deploying insights as a Streamlit dashboard
- Compare this cleaned data with test.csv and submit a prediction to Kaggle :)

---

Thanks for reading!  
– Vybhav K