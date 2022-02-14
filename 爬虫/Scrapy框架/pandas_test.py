import pandas as pd
import jsonlines



# with open('github.jl','r+', encoding='utf-8') as f:
#     for item in jsonlines.Reader(f):
#         print(item)
# print()

df = pd.read_json('github.jl', lines=True)
print(df.head)

print(df.shape)

print(df.columns)

print(df.branches[0:10])

print(df.Readme[:10])

print(df.Contributors)

print(df.about[:30])
