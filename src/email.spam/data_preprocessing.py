import os

import string

import pandas as pd 

import nltk

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


train_df = pd.read_csv("artifacts/email/train.csv")
test_df = pd.read_csv("artifacts/email/test.csv")


train_df = train_df.drop_duplicates()
test_df = test_df.drop_duplicates()

train_df.reset_index(drop=True, inplace=True)
test_df.reset_index(drop=True, inplace=True)

def transform_text(text):
    text = text.lower()

    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [ps.stem(word) for word in tokens]
    text = " ".join(tokens)

    return text

train_df["processed_text"] = train_df["text_combined"].apply(transform_text)

test_df["processed_text"] = test_df["text_combined"].apply(transform_text)

os.makedirs("artifacts/email", exist_ok=True)

train_df.to_csv(
    "artifacts/email/processed_train.csv",
    index=False
)

test_df.to_csv(
    "artifacts/email/processed_test.csv",
    index=False
)

print("Data Preprocessing Completed Successfully!")

