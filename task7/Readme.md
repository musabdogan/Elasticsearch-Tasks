# Vector Search

# .elser_model_2
I used the .elser_model_2 pre-trained ML model to index the text data with sparse_vector field type.
I used text_expansion search with content_embedding with model_id and model_text parameters.
https://www.elastic.co/guide/en/elasticsearch/reference/8.12/semantic-search-elser.html
```
GET /sparse/_search?pretty
{
  "query": {
    "text_expansion": {
      "content_embedding": {
        "model_id": ".elser_model_2",
        "model_text": "How to avoid muscle soreness after running?"
      }
    }
  }
}
```
# sentence-transformers__msmarco-minilm-l-12-v3
I used the sentence-transformers__msmarco-minilm-l-12-v3 pre-trained ML model to index the text data with dense_vector field type.
I used KNN search with query_vector. Each time I need to convert the query into vectors with _infer API call.
https://www.elastic.co/guide/en/machine-learning/current/ml-nlp-text-emb-vector-search-example.html
```
POST /collection-with-embeddings/_search?pretty
{
  "knn": {
    "field": "text_embedding.predicted_value",
    "query_vector": [0.3246288001537323, -0.1966380625963211, ...],  <-- number of dims (dimensional dense vector space)
    "k": 10,
    "num_candidates": 100
  }
}
```
# sematic_text field type.
Not introduced yet but it will.
There is a discussion about once the semantic_text field type is introduced the sparse_vector field type will be redundant. https://github.com/elastic/elasticsearch/issues/98094

