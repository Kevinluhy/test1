import pandas as pd

data=pd.read_csv("test.csv")
print (type(data["mark"][1]))


data.to_csv("test_new.csv", index = None)