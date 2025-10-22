from main import summarize_csv
import pandas as pd

def test_summarize_csv():
    df = pd.DataFrame({"x": [1, 2, 3]})
    df.to_csv("test.csv", index=False)
    result = summarize_csv("test.csv")
    assert "x" in result.columns
