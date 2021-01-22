import pandas as pd

data = pd.read_csv("BLEURT_score_test.csv")
# print(data["BLEURT Score"])
print(sum(i < -0.26 for i in data["BLEURT Score"]))

data = pd.read_csv("BLEURT_output.csv")
# print(data["BLEURT Score"])
print(sum(i < -0.26 for i in data["BLEURT Score"]))
