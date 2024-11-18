import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def load_data():
    """Load and preprocess data from CSV files."""
    fake_data = pd.read_csv('data/Fake.csv')
    real_data = pd.read_csv('data/True.csv')

    fake_data['label'] = 0  # Fake news
    real_data['label'] = 1  # Real news

    data = pd.concat([fake_data[['title', 'text', 'label']],
                      real_data[['title', 'text', 'label']]])
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)

    data['combined'] = data['title'].fillna('') + " " + data['text'].fillna('')
    return data

def preprocess_data(data):
    """Split data into training and testing sets."""
    X = data['combined'].values
    y = data['label'].values
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def vectorize_data(X_train, X_test):
    """Vectorize text data using TF-IDF."""
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    return X_train_vec, X_test_vec, vectorizer
