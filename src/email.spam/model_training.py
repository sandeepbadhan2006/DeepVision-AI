import os
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score, classification_report


# ==============================
# Load Dataset
# ==============================

train_df = pd.read_csv("artifacts/email/processed_train.csv")
test_df = pd.read_csv("artifacts/email/processed_test.csv")

train_df["processed_text"] = train_df["processed_text"].fillna("").astype(str)
test_df["processed_text"] = test_df["processed_text"].fillna("").astype(str)

X_train = train_df["processed_text"]
y_train = train_df["label"]

X_test = test_df["processed_text"]
y_test = test_df["label"]


# ==============================
# TF-IDF
# ==============================

vectorizer = TfidfVectorizer(max_features=5000)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# Save Vectorizer
os.makedirs("artifacts/email", exist_ok=True)

with open("artifacts/email/vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


# ==============================
# Models
# ==============================

models = {

    "Naive Bayes": MultinomialNB(),

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        eval_metric="logloss",
        random_state=42
    )

}


best_accuracy = 0
best_model = None
best_model_name = ""


print("=" * 60)

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name} Accuracy : {accuracy:.4f}")

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_model = model
        best_model_name = name

print("=" * 60)


# ==============================
# Save Best Model
# ==============================

with open("artifacts/email/model.pkl", "wb") as file:

    pickle.dump(best_model, file)


print(f"\nBest Model : {best_model_name}")

print(f"Accuracy : {best_accuracy:.4f}")


# ==============================
# Classification Report
# ==============================

prediction = best_model.predict(X_test)

print("\nClassification Report\n")

print(classification_report(y_test, prediction))