# Movie Recommender System

A content-based movie recommendation system built using Python.  
The system recommends movies similar to a given movie based on metadata such as genres, cast, crew, and overview.

# How It Works

1. Movie metadata is preprocessed and combined into a single feature set
2. Text data is vectorized
3. Cosine similarity is used to measure similarity between movies
4. The top 5 most similar movies are recommended
5. A Streamlit web app is used for interaction (runs locally)


# Features

- Content-based filtering (no user data required)
- Cosine similarity for recommendations
- Interactive Streamlit interface
- Displays movie posters and ratings (TMDB API)
- Runs locally using Jupyter Notebook / Streamlit


# Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Jupyter Notebook


# How to Run (Locally)

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Install the pkl files
   Run the last code in the notebook to generate the required files
5. Run the streamlit app
   streamlit run app.py
