import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

st.title("Movie Recommendation System")



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        ## fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl' , 'rb'))

select_movie_name  = st.selectbox(
    'Select the movie' ,
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(select_movie_name)

    for i in recommendations:
        st.write(i)
