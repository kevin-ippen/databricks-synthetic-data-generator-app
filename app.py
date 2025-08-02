import streamlit as st
import json
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config
from data_generator import generate_synthetic_dataframe, write_to_unity_catalog

# Initialize Databricks config
cfg = Config()

@st.cache_resource
def get_connection(http_path):
    return sql.connect(
        server_hostname=cfg.host,
        http_path=http_path,
        credentials_provider=lambda: cfg.authenticate,
    )

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