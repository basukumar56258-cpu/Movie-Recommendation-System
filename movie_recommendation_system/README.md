# 🎬 Movie Recommendation System

A simple Machine Learning based Movie Recommendation System built with:

- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS
- JavaScript

## How it works

The system uses **TF-IDF Vectorization** to convert movie genres and descriptions into numerical vectors. Then it uses **Cosine Similarity** to find movies with similar features.

## Project Structure

```text
movie_recommendation_system/
│
├── app.py
├── movies.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Run in VS Code

### 1. Open the project folder

Open this folder in VS Code.

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install libraries

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

## Recommendation Algorithm

1. Movie genres + descriptions are combined.
2. TF-IDF converts the text into vectors.
3. Cosine similarity calculates similarity between movies.
4. The top 6 similar movies are shown.

## Important

The included `movies.csv` is a small demo dataset. You can replace it with a larger dataset as long as it has these columns:

```text
title,genres,description
```
