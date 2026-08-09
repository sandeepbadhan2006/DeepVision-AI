import pickle

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


# Load Model
with open("artifacts/email/model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Vectorizer
with open("artifacts/email/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


stop_words = set(stopwords.words("english"))
ps = PorterStemmer()


def transform_text(text):

    text = str(text)
    text = text.lower()

    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [ps.stem(word) for word in tokens]

    return " ".join(tokens)


def predict_email(email):

    processed_email = transform_text(email)

    vector = vectorizer.transform([processed_email])

    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = round(max(probabilities) * 100, 2)

    if prediction == 1:
        result = "Spam Email"

        if confidence >= 85:
            risk = "High"
        elif confidence >= 65:
            risk = "Medium"
        else:
            risk = "Low"

    else:
        result = "Legitimate Email"

        if confidence >= 85:
            risk = "Low"
        elif confidence >= 65:
            risk = "Medium"
        else:
            risk = "High"

    return result, confidence, risk


if __name__ == "__main__":

    email = input("Enter Email:\n\n")

    result = predict_email(email)

    print("\nPrediction :", result)