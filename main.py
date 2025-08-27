import pandas as pd
import json

with open('data/data.json', 'r') as f:
    data = json.load(f)

columns = [
    "extra", "civility", "lastname", "firstname", "middle", 
    "address", "zip", "city", "canton", "email"
]

df = pd.DataFrame(data["data"], columns=columns)

print(df)
