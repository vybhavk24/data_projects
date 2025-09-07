import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel

# Load artifacts

@st.cache(allow_output_mutation=True)
def load_artifacts():
    tfidf = pickle.load(open('tfidf_vectorizer.pkl','rb'))
    svd = pickle.load(open('svd_model.pkl','rb'))
    movies = pd.read_pickle('movies_df.pkl')
    # Recompute content matrix
    content_matrix = tfidf.transform(movies['content'])
    cos_sim = linear_kernel(content_matrix, content_matrix)
    return tfidf, svd, movies, cos_sim

tfidf, svd, movies, cos_sim = load_artifacts()

st.title('🎬 Movie Recommender Demo')

user_id = st.number_input('Enter user id (integer):', min_value=1, value=1)
mode = st.radio('Mode:', ['Collaborative (SVD)', 'Content-based', 'Hybrid'])

# Hybrid function

def hybrid_recommendations(title, user_id, movies, svd, cos_sim, alpha=0.5, top_n=10):
    # --- Content-based part ---
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    content_indices = [i[0] for i in sim_scores]
    content_scores = [i[1] for i in sim_scores]

    # Collaborative part
    collab_scores = []
    for i in content_indices:
        try:
            est = svd.predict(user_id, movies.iloc[i]['movieId']).est
        except:
            est = 0
        collab_scores.append(est)

    # Combine
    final_scores = []
    for c, cb in zip(collab_scores, content_scores):
        final_scores.append(alpha * c + (1 - alpha) * cb)

    # Ranking movies
    ranked = sorted(zip(content_indices, final_scores), key=lambda x: x[1], reverse=True)
    return movies.iloc[[i[0] for i in ranked]][['title','genres']].head(top_n)

# Mode selection

if st.button('Get Recommendations'):
    if mode == 'Collaborative (SVD)':
        trainset = svd.trainset if hasattr(svd,'trainset') else None
        all_ids = movies['movieId'].unique()
        preds = []
        for mid in all_ids:
            try:
                est = svd.predict(user_id, mid).est
                preds.append((mid, est))
            except:
                pass
        preds = sorted(preds, key=lambda x: x[1], reverse=True)[:10]
        df = pd.DataFrame(preds, columns=['movieId','est']).merge(movies[['movieId','title']], on='movieId')
        st.table(df)

    elif mode == 'Content-based':
        title = st.selectbox('Pick a movie:', movies['title'].values)
        idx = movies[movies['title']==title].index[0]
        sim_scores = list(enumerate(cos_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
        ids = [i[0] for i in sim_scores]
        st.table(movies.iloc[ids][['title','genres']])

    elif mode == 'Hybrid':
        title = st.selectbox('Pick a movie for hybrid mode:', movies['title'].values)
        alpha = st.slider("Weight for Collaborative (0 = only Content, 1 = only Collaborative):", 
                          0.0, 1.0, 0.5)
        if title:
            recs = hybrid_recommendations(title, user_id, movies, svd, cos_sim, alpha=alpha)
            st.table(recs)