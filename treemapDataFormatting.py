import pandas
import json

#read in dataset
df = pandas.DataFrame.from_csv('Features.csv', header = 0)

index = []
for i in df.index:
    if i not in index:
        index.append(i)

#formatting data
data = {'name': 'Candy Crush Saga', 'children':[]}
for i in index:
    data['children'].append({'name': i, 'children':[]})

rows, cols = df.shape
index = df.index
for i in range(rows):
    if df.iloc[i, 2] == 1:
        for j in data['children']:
            if j['name'] == index[i]:
                j['children'].append({'name': df.iloc[i, 0],'choice': df.iloc[i, 1], 'value': df.iloc[i, 3]})

#file output
with open('treemapNodes.json', 'w') as outfile:
    json.dump(data, outfile)