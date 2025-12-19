import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=abef22da3fc010360a31325a0b6e2157&language=en-US")
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]


def recommend(option):
    movie_index = movies[movies["title"] == option].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        #getting poster from an api by logging in tmdb
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open("moviesdict.pkl", 'rb'))
movies= pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_option = st.selectbox(
    "How would you like to watch?", movies["title"].values)

if st.button("Recommend"):
    names,posters = recommend(selected_option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])
