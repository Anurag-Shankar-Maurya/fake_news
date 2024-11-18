from flask import Flask, request, jsonify, render_template
from preprocess import load_data, preprocess_data, vectorize_data
from model import build_and_train_model
from predict import predict_news

app = Flask(__name__)

# Step 1: Load and preprocess data
data = load_data()
X_train, X_test, y_train, y_test = preprocess_data(data)
X_train_vec, X_test_vec, vectorizer = vectorize_data(X_train, X_test)

# Step 2: Train the ML model
model = build_and_train_model(X_train_vec, y_train)

@app.route('/')
def home():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle predictions from the frontend."""
    content = request.json
    text = content.get('text', '')
    if not text.strip():
        return jsonify({'error': 'Input text is empty.'}), 400

    prediction = predict_news(text, vectorizer, model)
    label, confidence = prediction.split('(')
    return jsonify({
        'prediction': label.strip(),
        'confidence': confidence.strip(')')
    })

if __name__ == '__main__':
    app.run(debug=True)
