import os
import pickle
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer


# Load processed datasets
train_df = pd.read_csv("artifacts/email/processed_train.csv")
test_df = pd.read_csv("artifacts/email/processed_test.csv")

print(train_df["processed_text"].isnull().sum())
print(test_df["processed_text"].isnull().sum())

train_df["processed_text"] = train_df["processed_text"].fillna("").astype(str)
test_df["processed_text"] = test_df["processed_text"].fillna("").astype(str)

# Input and Target
X_train = train_df["processed_text"]
y_train = train_df["label"]

X_test = test_df["processed_text"]
y_test = test_df["label"]


# TF-IDF Feature Engineering
vectorizer = TfidfVectorizer(
    max_features=5000
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# Save Vectorizer
os.makedirs("artifacts/email", exist_ok=True)

with open("artifacts/email/vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)


print("Feature Engineering Completed Successfully!")

print("X_train Shape :", X_train.shape)
print("X_test Shape  :", X_test.shape)