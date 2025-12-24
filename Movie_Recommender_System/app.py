import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.set_page_config(
    page_title="Movie Recommender System",
    layout="centered"
)

API_KEY = "3fa7b2b1a265408017b8e83069c9bc6a"  

def fetch_movie_details(movie_title):
    
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    response = requests.get(url)
    data = response.json()

    if data.get("results"):
        movie = data["results"][0]

        poster = None
        if movie.get("poster_path"):
            poster = "https://image.tmdb.org/t/p/w500" + movie["poster_path"]

        rating = movie.get("vote_average", 0)

        return poster, rating

    return None, None


def recommend(movie):

    idx = movies[movies["title"] == movie].index[0]
    distances = similarity[idx]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []
    ratings = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster, rating = fetch_movie_details(title)

        names.append(title)
        posters.append(poster)
        ratings.append(rating)

    return names, posters, ratings


st.title(" Movie Recommender System")

movie_name = st.selectbox(
    "Please select or type a movie",
    movies["title"].values
)

if st.button("Recommend"):
    with st.spinner("Finding best movies for you..."):
        names, posters, ratings = recommend(movie_name)

    cols = st.columns(5)

    for col, name, poster, rating in zip(cols, names, posters, ratings):
        with col:
            if poster:
                st.image(poster, width=180)
            st.caption(name)
            if rating:
                st.markdown(f" **⭐{rating:.1f}/10**")
