import streamlit as st
import pickle
import pandas as pd
import requests

# import ML Model
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# Class
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id

        recommended.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended
def recommendd(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_posters

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=0b0d78105881afb968e8a5ea4c4d7489&language=en-us'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# main Body
# title
st.title(':white[Movies Recommender System]')
# selector
select_movie_name = st.selectbox(
    '_What is your test ?_',
    movies['title'].values)





# Button
if st.button('Recommend'):
    names = recommend(select_movie_name)
    posters = recommendd(select_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])