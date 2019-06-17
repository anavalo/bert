import pandas as pd
from pandas.io.json import json_normalize
import json



with open('bioasq_data/allMeSH_limitjournals.json') as f:
    for line in f:
        data = json.load(line)

df = pd.Dataframe(data)

print(df.info)



#
# data_lsit = []
# for chunks in pd.read_json('bioasq_data/allMeSH_limitjournals.json', lines=True, chunksize=1000):
#     data_lsit.append(chunks)
# df = pd.concat(data_lsit, axis = 0)


