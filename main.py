import pandas as pd

def summarize_csv(file_path):
    data = pd.read_csv(file_path)
    return data.describe()

if __name__ == "__main__":
    print(summarize_csv("data.csv"))
EOF
