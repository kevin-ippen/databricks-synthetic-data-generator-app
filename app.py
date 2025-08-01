import streamlit as st
import json

st.title("Synthetic Data Generator (Notebook-based)")

catalog = st.text_input("Unity Catalog", "sandbox_catalog")
schema = st.text_input("Schema", "synthetic_data")
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
    params = {
        "catalog": catalog,
        "schema": schema,
        "table_name": table_name,
        "columns": json.dumps(columns),
        "row_count": row_count
    }

    result = dbutils.notebook.run("/Workspace/Users/kevin.ippen@databricks.com/synthetic-data-generator/notebooks/1_data_generator_notebook", 600, params)
    st.success(f"Synthetic data written to {result}")