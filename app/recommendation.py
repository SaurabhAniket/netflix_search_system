from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(title, df):
    # Define a TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Fit and transform the descriptions
    tfidf_matrix = tfidf.fit_transform(df['description'])
    
    # Compute cosine similarity between all movies
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find the index of the movie that matches the title
    idx = df[df['title'].str.contains(title, case=False, na=False)].index[0]
    
    # Get pairwise similarity scores of all movies with the input movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 most similar movies
    sim_scores = sim_scores[1:6]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top 5 most similar movies
    return df['title'].iloc[movie_indices]
