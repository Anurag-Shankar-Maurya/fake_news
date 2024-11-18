from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def build_and_train_model(X_train_vec, y_train):
    """Train a Logistic Regression model."""
    model = LogisticRegression(max_iter=500, random_state=42)
    model.fit(X_train_vec, y_train)
    return model

def evaluate_model(model, X_test_vec, y_test):
    """Evaluate the model and print classification report."""
    y_pred = model.predict(X_test_vec)
    print(classification_report(y_test, y_pred, target_names=['Fake', 'Real']))
