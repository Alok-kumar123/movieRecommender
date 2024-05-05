**Movie Recommender System**
This project implements a movie recommender system using content-based filtering with the TMDB dataset. It leverages natural language processing techniques to analyze movie metadata and provide recommendations based on similarities between movies.

**Prerequisites**
Python 3.x
Required libraries: pandas, numpy, scikit-learn, nltk, streamlit, requests

**Description**
The preprocess.py script preprocesses the raw TMDB dataset by cleaning, transforming, and extracting relevant features.
The app.py script hosts the Streamlit web application for the movie recommender system.
The recommender system is built using content-based filtering, which recommends movies based on similarities between their features such as genres, keywords, cast, and crew.
Users can select a movie from the dropdown menu, and the system recommends similar movies along with their posters.
Movie recommendations are generated using cosine similarity between movie features.
The project utilizes the TMDB API to fetch movie posters.

**Acknowledgements**
TMDB for providing the dataset and API.
Streamlit for enabling easy and interactive web application development.
