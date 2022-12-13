import pandas as pd

df = pd.read_csv("test.csv")
df = df.reset_index()  # make sure indexes pair with number of rows

map = {}
for index, row in df.iterrows():
    score = 0
    score += row['Rating'] * 5
    score += row['Reviews'] *.02
    if row['Pricing'] == "$":
        score +=3
    elif row['Pricing'] == "$$":
        score +=2
    elif row['Pricing'] == "$$$":
        score +=1
    else:
        score +=0.5
    score -= row['Distance'] * .0005
    map[index] = score

sortedmap = sorted(map.values())
restindex = max(map, key=map.get)
print(df.iloc[restindex]['Name'])
restid = (df.iloc[restindex]['ID'])

'''
moveNext = input("Next (y/n)?")
while moveNext == "y":
    del map[restindex]
    restindex = max(map, key=map.get)
    restid = (df.iloc[restindex]['ID'])
    print(df.iloc[restindex]['Name'])
    moveNext = input("Next (y/n)?")
'''