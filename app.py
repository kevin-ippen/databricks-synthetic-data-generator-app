import streamlit as st
import json
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker()

# Initialize Databricks config
cfg = Config()

@st.cache_resource
def get_connection(http_path):
    return sql.connect(
        server_hostname=cfg.host,
        http_path=http_path,
        credentials_provider=lambda: cfg.authenticate,
    )

def generate_synthetic_dataframe(columns, row_count):
    """Generate pandas DataFrame with synthetic data"""
    data = []
    for i in range(row_count):
        row = {}
        for col in columns:
            if col["type"] == "string":
                row[col["name"]] = fake.word()
            elif col["type"] == "integer":
                row[col["name"]] = random.randint(0, 10000)
            elif col["type"] == "float":
                row[col["name"]] = round(random.uniform(0, 10000), 2)
            elif col["type"] == "date":
                row[col["name"]] = fake.date_between(start_date="-1y", end_date="today")
            elif col["type"] == "timestamp":
                row[col["name"]] = datetime.now() - timedelta(days=random.randint(0, 365))
            else:
                row[col["name"]] = fake.word()
        data.append(row)
    return pd.DataFrame(data)

def write_to_unity_catalog(table_name: str, df: pd.DataFrame, conn):
    """Write DataFrame to Unity Catalog using SQL - creates table if it doesn't exist"""
    with conn.cursor() as cursor:
        try:
            # First, create the table schema based on the DataFrame
            column_definitions = []
            for col_name, dtype in df.dtypes.items():
                if pd.api.types.is_integer_dtype(dtype):
                    sql_type = "BIGINT"
                elif pd.api.types.is_float_dtype(dtype):
                    sql_type = "DOUBLE"
                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    sql_type = "TIMESTAMP"
                else:
                    sql_type = "STRING"
                column_definitions.append(f"`{col_name}` {sql_type}")
            
            # Create table if it doesn't exist
            create_table_sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join(column_definitions)}
            ) USING DELTA
            """
            cursor.execute(create_table_sql)
            
            # Clear existing data (if any)
            cursor.execute(f"DELETE FROM {table_name}")
            
            # Insert new data
            if not df.empty:
                rows = list(df.itertuples(index=False))
                values = ",".join([f"({','.join(map(repr, row))})" for row in rows])
                cursor.execute(f"INSERT INTO {table_name} VALUES {values}")
                
        except Exception as e:
            # If table creation fails, try a simpler approach
            st.warning(f"Table creation failed, trying alternative approach: {e}")
            
            # Alternative: Create table from the first row, then insert all data
            if not df.empty:
                first_row = df.iloc[0:1]
                first_values = ",".join([f"({','.join(map(repr, row))})" for row in first_row.itertuples(index=False)])
                
                # Create table with first row
                cursor.execute(f"CREATE OR REPLACE TABLE {table_name} AS VALUES {first_values}")
                
                # Insert remaining rows if there are any
                if len(df) > 1:
                    remaining_rows = df.iloc[1:]
                    remaining_values = ",".join([f"({','.join(map(repr, row))})" for row in remaining_rows.itertuples(index=False)])
                    cursor.execute(f"INSERT INTO {table_name} VALUES {remaining_values}")

st.title("Synthetic Data Generator (SQL-based)")

# SQL Warehouse configuration
http_path = st.text_input(
    "SQL Warehouse HTTP Path:", 
    placeholder="/sql/1.0/warehouses/862f1d757f0424f7",
    help="Get this from your SQL Warehouse details page"
)

catalog = st.text_input("Unity Catalog", "users")
schema = st.text_input("Schema", "kevin_ippen")
table_name = st.text_input("Table Name", "synthetic_table")
row_count = st.number_input("Row Count", value=1000)

st.header("Define Columns")
num_columns = st.number_input("Number of Columns", min_value=1, value=3)
columns = []
for i in range(num_columns):
    col_name = st.text_input(f"Column {i+1} Name", f"col_{i+1}")
    col_type = st.selectbox(f"Column {i+1} Type", ["string", "integer", "float", "date", "timestamp"], key=f"type_{i}")
    columns.append({"name": col_name, "type": col_type})

if st.button("Generate Data"):
    if not http_path:
        st.error("Please provide SQL Warehouse HTTP Path")
    else:
        try:
            with st.spinner("Generating synthetic data..."):
                conn = get_connection(http_path)
                df = generate_synthetic_dataframe(columns, int(row_count))
                full_table_name = f"{catalog}.{schema}.{table_name}"
                write_to_unity_catalog(full_table_name, df, conn)
            st.success(f"Synthetic data written to {full_table_name}")
        except Exception as e:
            st.error(f"Error generating data: {str(e)}")