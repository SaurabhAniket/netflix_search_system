from flask import Flask, jsonify, request
import pandas as pd
from elasticsearch import Elasticsearch
from app.recommendation import get_recommendations
from app.search_engine import search_series

app = Flask(__name__)

# Initialize Elasticsearch
es = Elasticsearch()

# Load the dataset for recommendations
df = pd.read_csv('data/netflix_series.csv')

# Search route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = search_series(es, query)
    return jsonify(results)

# Recommendation route
@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    recommendations = get_recommendations(title, df)
    return jsonify(list(recommendations))

if __name__ == '__main__':
    app.run(debug=True)
