import pandas as pd

data = [["aaa", "bbb", 29],["aaa", "bbb", 29],["aaa", "bbb", 29],["aaa", "bbb", 29]]

df = pd.DataFrame(data, columns=["first_name", "last_name", "age"])
print(df)

df["address"] = ["xyz",
                 "abc", "def", "pqr"]

print(df)

print(df.loc[0:3, "first_name": "age"])
print(df.iloc[:, :])
print(df.transpose().transpose())
df.rename(columns={"age": "age_new", "first_name": "first_name_new"}, inplace=True)
print(df)

df.replace("aaa", "new_aaa", inplace=True)
print(df)

print(df.info())
print(df.describe())
#
# df.index = [i for i in range(100, 104) ]
# df.columns = [i for i in range(100, 104) ]

min_age = df.groupby().min()
print(min_age)

