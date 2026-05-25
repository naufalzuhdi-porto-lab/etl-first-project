import pandas as pd
import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)

data = response.json()
df = pd.DataFrame(data)
print(df.head(5))

df.to_csv('data/products.csv', index=False)

print('Data saved successfully')