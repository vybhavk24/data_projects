## Movie Recommender System

A Movie Recommender System built using the MovieLens dataset. This project implements and compares three recommendation approaches: Collaborative Filtering (SVD), Content-based Filtering (TF-IDF + Cosine Similarity), and a Hybrid Recommender that combines both.

---

### Features

- **Collaborative Filtering (SVD)**  
  Learns user preferences from rating patterns to deliver personalized movie recommendations.
  
- **Content-based Filtering**  
  Recommends movies similar to a selected title based on metadata such as genres and user tags.
  
- **Hybrid Recommender**  
  Blends collaborative and content-based scores with adjustable weights for more robust, tailored recommendations.
  
- **Interactive Streamlit App**  
  Offers a simple user interface to explore and test recommendations by entering a user ID or selecting a movie title.

---

### Project Structure

```
Movie_Recommender_System/
│
├── Dataset/                   # MovieLens dataset CSV files
│   ├── movies.csv
│   ├── ratings.csv
│   ├── tags.csv
│   └── links.csv
│
├── Movie_recommender.ipynb    # Jupyter Notebook for data preprocessing, model training, and exploration
├── app.py                     # Streamlit app for demo and interaction
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer model
├── svd_model.pkl              # Saved trained SVD model
├── movies_df.pkl              # Preprocessed movies DataFrame with metadata and features
└── README.md                  # This documentation
```

---

### Installation & Setup

1. **Clone the Repository**

```
use git clone
cd 6_Movie_Recommender_System
```

2. **Create and Activate Virtual Environment** (recommended)

```
conda create -n movie_recommender python=3.10 -y
conda activate movie_recommender
```

3. **Install Dependencies**

```
pip install scikit-surprise
```

> *Note:* Installing `scikit-surprise` can be tricky on macOS. If it fails, try:  
> pip install --no-binary :all: scikit-surprise

4. **Download Dataset**  
Place the MovieLens CSV files inside the `Dataset/` folder.  
This project uses the [MovieLens latest Dataset small](https://grouplens.org/datasets/movielens/) dataset (the methodology works with the 25M dataset if hardware resources allow).

5. **Train Models**  
Open and run all cells in `Movie_recommender.ipynb` to:  
  - Preprocess the dataset  
  - Train the TF-IDF model for content similarity  
  - Train the SVD model for collaborative filtering  
  - Save models as `.pkl` files for reuse in the Streamlit app

6. **Run the Streamlit App**

```
streamlit run app.py
```

Access the app at [http://localhost:8501](http://localhost:8501)

---

### 🚀 Usage

- **Collaborative (SVD):** Enter a user ID to get personalized recommendations based on collaborative filtering.  
- **Content-based:** Select a movie title to find similar movies based on genres and tags.  
- **Hybrid:** Combines both collaborative and content-based approaches with an interactive slider for weighting.

---

### Skills & Tools Highlighted

- **Machine Learning:** Recommender systems (Collaborative, Content-based, Hybrid)  
- **Libraries:** scikit-learn, scikit-surprise, pandas, streamlit  
- **Evaluation Metrics:** RMSE, Precision@k (demonstrated in notebook)  
- **Deployment:** Interactive local Streamlit app interface

---

### Future Improvements

- Add movie posters and more metadata visualization in the Streamlit app  
- Deploy the app online (e.g., Streamlit Cloud, HuggingFace Spaces)  
- Incorporate implicit feedback for recommendations  
- Explore neural recommender systems (e.g., DeepFM, AutoEncoders)

---

Feel free to explore, contribute, and extend this Movie Recommender project!