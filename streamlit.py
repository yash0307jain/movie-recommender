# Importing the required libraries
import streamlit as st
import pickle
import pandas as pf

# Loading the movies dataframe which is modified from the actual csv after cleaning and preprocessing
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies_df = pf.DataFrame(movies_dict)
movies_list = movies_df["title"].values

# Similarity matrix which consist the relation between movies
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation function which is responsible to provide the recommended movies
def recommender(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    similarity_percentage = similarity[movie_index]
    recommended_movies = sorted(list(enumerate(similarity_percentage)), reverse=True, key=lambda x:x[1])[1:6]
    
    movies = []
    for index in recommended_movies:
        movies.append(movies_df.iloc[index[0]].title)
        
    return movies

# Title of the template
st.title("Movie Recommendation System")

# Dropdown to display the movies list
option = st.selectbox("Select the movie", movies_list)

if st.button("Recommend"):
    recommendations = recommender(option)
    for movie in recommendations:
        st.write(movie)

