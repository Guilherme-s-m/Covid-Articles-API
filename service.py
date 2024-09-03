import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_papers_from_csv(user_interest):
    """
    Recommends papers based on user interest using TF-IDF and cosine similarity.

    :param user_interest: A string representing the user's interests.
    :param csv_path: Path to the CSV file containing the papers.
    :return: A list of dictionaries containing 'title', 'abstract' (first 500 words), and 'relevance' for the top 10 papers.
    """
    csv_path = "data/metadata.csv"  # Caminho para o CSV

    # Load documents from CSV
    df = pd.read_csv(csv_path)

    # Convert DataFrame to a list of dictionaries
    documents = df.to_dict(orient='records')

    # Combine user interest with document contents for TF-IDF vectorization
    corpus = [user_interest] + [doc['abstract'] for doc in documents]
    
    # Apply TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Compute cosine similarity between the user interest and each document
    user_vector = tfidf_matrix[0]
    doc_vectors = tfidf_matrix[1:]
    similarities = cosine_similarity(user_vector, doc_vectors).flatten()
    
    # Prepare the results in the required format
    results = []
    for i, doc in enumerate(documents):
        result = {
            'title': doc['title'],
            'content': ' '.join(doc['abstract'].split()[:500]),  # Truncate to first 500 words
            'relevance': similarities[i]
        }
        if similarities[i] > 0.1:
            results.append(result)

    # Sort results by relevance score in descending order
    sorted_results = sorted(results, key=lambda x: x['relevance'], reverse=True)
    
    # Return top 10 results
    return sorted_results[:10]

