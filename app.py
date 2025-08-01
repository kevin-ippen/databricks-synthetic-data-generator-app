import streamlit as st
import yaml
import pandas as pd
from utils.data_generator import generate_synthetic_data
from utils.uc_writer import write_to_uc

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

st.title("Synthetic Data Generator for Unity Catalog")

st.sidebar.header("Configuration")
catalog = st.sidebar.text_input("Unity Catalog", config["unity_catalog"]["catalog"])
schema = st.sidebar.text_input("Schema", config["unity_catalog"]["schema"])
table_prefix = st.sidebar.text_input("Table Prefix", config["unity_catalog"]["default_table_prefix"])
row_count = st.sidebar.number_input("Row Count", value=config["data_defaults"]["row_count"])

st.header("Define Columns")
columns = []
num_columns = st.number_input("Number of columns", min_value=1, value=3)

for i in range(num_columns):
    col_name = st.text_input(f"Column {i+1} Name", f"col_{i+1}")
    col_type = st.selectbox(f"Column {i+1} Type", config["supported_types"], key=f"type_{i}")
    columns.append({"name": col_name, "type": col_type})

if st.button("Generate Preview"):
    df = generate_synthetic_data(columns, row_count=row_count)
    st.dataframe(df.head())

    if st.button("Write to Unity Catalog"):
        table_name = table_prefix + "table"
        full_table = write_to_uc(df, catalog, schema, table_name)
        st.success(f"Data written to {full_table}")
