import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/products.csv")

engine = create_engine(
    "postgresql://postgres:naufalfamzz8721@localhost:5432/postgres"
)

df.to_sql(
    name="products",
    con=engine,
    if_exists="replace",
    index=False
)

print('data loaded to PostgreSQL')