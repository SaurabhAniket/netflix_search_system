from elasticsearch import Elasticsearch

def search_series(es, query):
    index_name = 'netflix_series'
    result = es.search(index=index_name, body={
        "query": {
            "match": {
                "title": query
            }
        }
    })
    return [res['_source'] for res in result['hits']['hits']]
