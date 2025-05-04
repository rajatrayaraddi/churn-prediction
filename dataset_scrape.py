import pandas as pd

base_url = "https://huggingface.co/datasets/aai510-group1/telco-customer-churn/resolve/main/"

files = ["train.csv", "test.csv", "validation.csv"]

for file in files:
    url = base_url + file
    df = pd.read_csv(url)
    df.to_csv(file, index=False)
    print(f"Saved {file} locally.")

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
validation_df = pd.read_csv("validation.csv")

combined_df = pd.concat([train_df, test_df, validation_df], ignore_index=True)

combined_df.to_csv("combined_data.csv", index=False)