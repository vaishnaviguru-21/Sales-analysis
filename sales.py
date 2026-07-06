import pandas as pd
df = pd.read_csv(r"C:\Users\user\Downloads\sales_data.csv")

df.head()

df.info()

df.describe(include='all')

df.isnull().sum()

df.columns = df.columns.str.lower()
df.columns

labels = ['Low', 'Medium', 'High', 'Very High']
df['sales_group'] = pd.qcut(df['sales_amount'], q=4, labels = labels)
df[['sales_amount', 'sales_group']].head(10)

daily=df.groupby('sale_date')['sales_amount'].sum()
daily

df.groupby('region')['sales_amount'].sum()

df.groupby('product_category')['sales_amount'].sum()

df.groupby('customer_type').agg({
'sales_amount':'sum',
'quantity_sold':'sum',
'discount':'mean'
})

df['profit']=(df['unit_price']-df['unit_cost'])*df['quantity_sold']
df['profit']

df['profit_margin']=df['profit']/df['sales_amount']
df['profit_margin']

#convert to datetime
print(df['sale_date'].dtype)

import pandas as pd
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')
print(df['sale_date'].dtype)

df['weekday']=df['sale_date'].dt.day_name()
df['weekday']

#installation
pip install psycopg2-binary

import psycopg2
import pandas as pd

!pip install psycopg2-binary sqlalchemy

from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL Connection Details
username = "postgres"
password = "1234"
host = "localhost"
port = "5433"          
database = "sales_analysis"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Upload DataFrame to PostgreSQL
df.to_sql(
    name="sales",
    con=engine,
    if_exists="replace",   
    index=False
)
print("✅ Data uploaded successfully!")
