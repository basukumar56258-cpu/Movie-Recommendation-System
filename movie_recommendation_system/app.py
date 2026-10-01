from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load movie dataset
movies = pd.read_csv("movies.csv")
movies["features"] = (
    movies["genres"].fillna("") + " " +
    movies["description"].fillna("")
)

# Convert movie text into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["features"])

# Similarity between every pair of movies
similarity_matrix = cosine_similarity(tfidf_matrix)

def recommend_movies(title, count=6):
    """Return movies similar to the selected movie."""
    matches = movies[movies["title"].str.lower() == title.lower()]
    if matches.empty:
        return []

    index = matches.index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for movie_index, score in scores[1:count + 1]:
        movie = movies.iloc[movie_index]
        recommendations.append({
            "title": movie["title"],
            "genres": movie["genres"].replace("|", " • "),
            "description": movie["description"],
            "score": round(float(score) * 100, 1)
        })
    return recommendations

@app.route("/")
def home():
    return render_template("index.html", movies=movies["title"].tolist())

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Please select a movie."}), 400

    recommendations = recommend_movies(title)
    if not recommendations:
        return jsonify({"error": "Movie not found."}), 404

    return jsonify({
        "selected": title,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True)
