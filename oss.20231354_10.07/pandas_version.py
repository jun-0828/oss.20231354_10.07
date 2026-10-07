import pandas as pd

data = pd.read_csv("scores.csv")
data["score"] = pd.to_numeric(data["score"], errors = "coerce")
result = data.groupby("category")["score"].mean().round(2)
print(result)
