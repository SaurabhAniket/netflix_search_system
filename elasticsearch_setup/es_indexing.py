import pandas as pd
from elasticsearch import Elasticsearch, helpers

# Create an instance of the Elasticsearch client
es = Elasticsearch(
    hosts=[{"host": "localhost", "port": 9200, "scheme": "http"}]  # Use "https" if using SSL
)

# Load your data from the correct CSV path
df = pd.read_csv(r'C:\Users\KIIT\Desktop\Assignment\netflix_search_system\data\netflix_series.csv')  # Ensure this path is correct

# Create a list to hold the indexing actions
actions = []

# Iterate over the DataFrame and prepare actions for indexing
for index, row in df.iterrows():
    action = {
        "_index": "netflix_series",
        "_id": row['show_id'],
        "_source": {
            "type": row['type'],
            "title": row['title'],
            "director": row['director'],
            "cast": row['cast'],
            "country": row['country'],
            "date_added": row['date_added'],
            "release_year": row['release_year'],
            "rating": row['rating'],
            "duration": row['duration'],
            "listed_in": row['listed_in'],
            "description": row['description']
        }
    }
    actions.append(action)

# Use the helpers.bulk function to perform the indexing in bulk
if actions:
    helpers.bulk(es, actions)
    print("Indexing completed.")
else:
    print("No actions to index.")
