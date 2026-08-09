import os
import pandas as pd 
from sklearn.model_selection import train_test_split

df = pd.read_csv("archive/phishing_email.csv")

# Create artifacts folder if not exists
os.makedirs("artifacts/email", exist_ok=True)

train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

train_df.to_csv("artifacts/email/train.csv", index=False)
test_df.to_csv("artifacts/email/test.csv", index=False)

print("Data Ingestion Completed Successfully!")