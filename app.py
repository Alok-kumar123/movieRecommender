import streamlit as st
import pickle
import pandas as pd
import requests

import bz2

 
 

# Decompress and load the data
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
#movies_dict= decompress('cmovie_dict.pkl')
movies=pd.DataFrame(movies_dict)


def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a00c6b817d63726063a55c529daefec&language=en-US'.format(movie_id))
    data=response.json()
    
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recomended_movies=[]
    recomended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movies_posters.append(fetch_poster(movie_id))
    return recomended_movies,  recomended_movies_posters

with bz2.BZ2File('compress_similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

#similarity=pickle.load(open('compress_similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie=st.selectbox('Select movies', movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
    