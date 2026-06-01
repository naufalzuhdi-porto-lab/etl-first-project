import pandas as pd
from sqlalchemy import create_engine
import requests

def extract():
    url = "https://fakestoreapi.com/products"
    
    response = requests.get(url)
    
    data = response.json()
    df = pd.DataFrame(data)
    print('Extract Data Successful!!')
    return df

def transform(df):
    df.columns = df.columns.str.lower()
    
    df['price'] = df['price'].astype(float)
    df['title'] = df['title'].str.strip()
    df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
    df['rating_count'] = df['rating'].apply(lambda x: x['count'])
    df.drop(columns=["rating"], inplace=True)
    
    print("Transformation Data Successful")
    
    return df

def load(df):
    engine = create_engine(
        "postgresql://postgres:naufalfamzz8721@localhost:5432/postgres"
    )
    
    df.to_sql(
        name="products_etl",
        con=engine,
        if_exists="replace",
        index=False
    )
    print('Load Data Successful')
    
def main():
    df = extract()
    df = transform(df)
    load(df)
    
if __name__ == "__main__":
    main()