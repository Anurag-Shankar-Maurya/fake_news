def predict_news(news_text, vectorizer, model):
    """Predict if news is Fake or Real."""
    news_vec = vectorizer.transform([news_text])
    prediction_prob = model.predict_proba(news_vec)[0]
    prediction = model.predict(news_vec)[0]

    fake_percentage = prediction_prob[0] * 100
    real_percentage = prediction_prob[1] * 100

    if prediction == 1:
        return f"Real ({real_percentage:.2f}% confidence)"
    else:
        return f"Fake ({fake_percentage:.2f}% confidence)"
