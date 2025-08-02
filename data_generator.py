import streamlit as st
import json
from datetime import datetime, timedelta
import random
from faker import Faker
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config

# Initialize Spark session and Faker
try:
    fake = Faker()
except Exception as e:
    st.error(f"Error initializing Spark: {e}")
    st.stop()

# Import templates from separate file
from templates import TEMPLATES

def generate_realistic_data(col_config, fake):
    """Generate realistic data based on column configuration"""
    col_type = col_config["type"]
    null_rate = col_config.get("null_rate", 0)
    
    # Handle null values
    if random.random() < null_rate:
        return None
    
    if col_type == "string":
        if "pattern" in col_config:
            pattern = col_config["pattern"]
            if "{random_int:" in pattern:
                # Extract min and max from pattern like "CUST-{random_int:10000:99999}"
                start = pattern.find("{random_int:") + 12
                end = pattern.find("}", start)
                min_val, max_val = map(int, pattern[start:end].split(":"))
                return pattern.replace(f"{{random_int:{min_val}:{max_val}}}", str(random.randint(min_val, max_val)))
        return fake.word()
    
    elif col_type == "first_name":
        return fake.first_name()
    
    elif col_type == "last_name":
        return fake.last_name()
    
    elif col_type == "email":
        return fake.email()
    
    elif col_type == "phone":
        return fake.phone_number()
    
    elif col_type == "address":
        return fake.address().replace('\n', ', ')
    
    elif col_type == "city":
        return fake.city()
    
    elif col_type == "state":
        return fake.state()
    
    elif col_type == "zipcode":
        return fake.zipcode()
    
    elif col_type == "sentence":
        min_words = col_config.get("min_words", 5)
        max_words = col_config.get("max_words", 15)
        return fake.sentence(nb_words=random.randint(min_words, max_words))
    
    elif col_type == "text":
        min_sentences = col_config.get("min_sentences", 1)
        max_sentences = col_config.get("max_sentences", 3)
        return fake.text(max_nb_chars=random.randint(min_sentences * 50, max_sentences * 100))
    
    elif col_type == "integer":
        min_val = col_config.get("min_val", 0)
        max_val = col_config.get("max_val", 10000)
        return random.randint(min_val, max_val)
    
    elif col_type == "float":
        min_val = col_config.get("min_val", 0.0)
        max_val = col_config.get("max_val", 10000.0)
        decimals = col_config.get("decimals", 2)
        return round(random.uniform(min_val, max_val), decimals)
    
    elif col_type == "boolean":
        true_rate = col_config.get("true_rate", 0.5)
        return random.random() < true_rate
    
    elif col_type == "choice":
        choices = col_config.get("choices", ["A", "B", "C"])
        weights = col_config.get("weights", None)
        return random.choices(choices, weights=weights)[0]
    
    elif col_type == "date":
        start_date = col_config.get("start_date", "2020-01-01")
        end_date = col_config.get("end_date", "2024-12-31")
        return fake.date_between(start_date=start_date, end_date=end_date)
    
    elif col_type == "timestamp":
        start_date = col_config.get("start_date", "2024-01-01")
        end_date = col_config.get("end_date", "2024-12-31")
        return fake.date_time_between(start_date=start_date, end_date=end_date)
    
    else:
        return fake.word()

def generate_synthetic_dataframe_advanced(columns, row_count):
    """Generate pandas DataFrame using advanced template configurations"""
    data = []
    for i in range(row_count):
        row = {}
        for col in columns:
            # Use the advanced generate_realistic_data function
            row[col["name"]] = generate_realistic_data(col, fake)
        data.append(row)
    return pd.DataFrame(data)

def write_to_unity_catalog(table_name: str, df: pd.DataFrame, conn):
    """Write DataFrame to Unity Catalog with proper column names and types"""
    import math
    
    with conn.cursor() as cursor:
        if not df.empty:
            def clean_value(val):
                """Convert any problematic value to a clean SQL value"""
                if val is None or pd.isna(val):
                    return "NULL"
                elif isinstance(val, float) and math.isnan(val):
                    return "NULL"
                elif str(val).lower() in ['nan', 'nat', 'none', '']:
                    return "NULL"
                elif isinstance(val, str):
                    if val.strip() == '':
                        return "NULL"
                    escaped = val.replace("'", "''")
                    return f"'{escaped}'"
                elif isinstance(val, (int, float)):
                    return str(val)
                elif isinstance(val, (datetime, pd.Timestamp)):
                    return f"'{val}'"
                else:
                    return f"'{str(val)}'"
            
            def get_sql_type(dtype):
                """Convert pandas dtype to SQL type"""
                if pd.api.types.is_integer_dtype(dtype):
                    return "BIGINT"
                elif pd.api.types.is_float_dtype(dtype):
                    return "DOUBLE"
                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    return "TIMESTAMP"
                elif pd.api.types.is_bool_dtype(dtype):
                    return "BOOLEAN"
                else:
                    return "STRING"
            
            # Build column definitions with types
            column_definitions = []
            for col_name, dtype in df.dtypes.items():
                sql_type = get_sql_type(dtype)
                column_definitions.append(f"`{col_name}` {sql_type}")
            
            columns_sql = ", ".join(column_definitions)
            
            # Process rows
            clean_rows = []
            for _, row in df.iterrows():
                clean_values = [clean_value(val) for val in row]
                clean_rows.append(f"({','.join(clean_values)})")
            
            values = ",".join(clean_rows)
            
            # Create table with proper schema
            sql_statement = f"""
            CREATE OR REPLACE TABLE {table_name} (
                {columns_sql}
            ) AS VALUES {values}
            """
            
            st.write(f"**Creating table with columns:** {list(df.columns)}")
            cursor.execute(sql_statement)


# Streamlit UI
st.set_page_config(page_title="Enhanced Synthetic Data Generator", layout="wide")
st.title("🎯 Enhanced Synthetic Data Generator")
st.markdown("Generate realistic synthetic data with pre-built templates or custom configurations")

# Sidebar for basic configuration
with st.sidebar:
    st.header("📋 Basic Configuration")
    catalog = st.text_input("Unity Catalog", "sandbox_catalog")
    schema = st.text_input("Schema", "synthetic_data")
    table_name = st.text_input("Table Name", "synthetic_table")
    row_count = st.number_input("Row Count", min_value=100, max_value=1000000, value=1000)
    write_mode = st.selectbox("Write Mode", ["overwrite", "append"], index=0)

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🎨 Template Selection")
    template_name = st.selectbox(
        "Choose a Template",
        list(TEMPLATES.keys()),
        help="Select a pre-built template or choose 'Custom' to build your own"
    )
    
    if template_name != "Custom":
        st.info(f"**{template_name}**\n\n{TEMPLATES[template_name]['description']}")
        if st.button("📥 Load Template"):
            st.session_state.columns = TEMPLATES[template_name]["columns"].copy()
            st.rerun()

with col2:
    st.header("⚙️ Column Configuration")
    
    # Initialize session state
    if "columns" not in st.session_state:
        st.session_state.columns = []
    
    # Add new column button
    if st.button("➕ Add Column"):
        st.session_state.columns.append({
            "name": f"col_{len(st.session_state.columns) + 1}",
            "type": "string",
            "null_rate": 0.0
        })
        st.rerun()
    
    # Configure existing columns
    if st.session_state.columns:
        for i, col in enumerate(st.session_state.columns):
            with st.expander(f"Column {i+1}: {col['name']}", expanded=False):
                col1_inner, col2_inner = st.columns(2)
                
                with col1_inner:
                    col["name"] = st.text_input(f"Name", col["name"], key=f"name_{i}")
                    col["type"] = st.selectbox(
                        f"Type",
                        ["string", "integer", "float", "boolean", "date", "timestamp", 
                         "first_name", "last_name", "email", "phone", "address", "city", 
                         "state", "zipcode", "sentence", "text", "choice"],
                        index=["string", "integer", "float", "boolean", "date", "timestamp", 
                               "first_name", "last_name", "email", "phone", "address", "city", 
                               "state", "zipcode", "sentence", "text", "choice"].index(col["type"]),
                        key=f"type_{i}"
                    )
                
                with col2_inner:
                    col["null_rate"] = st.slider(f"Null Rate", 0.0, 0.5, col.get("null_rate", 0.0), key=f"null_{i}")
                    
                    # Type-specific configuration
                    if col["type"] in ["integer", "float"]:
                        col["min_val"] = st.number_input(f"Min Value", value=col.get("min_val", 0), key=f"min_{i}")
                        col["max_val"] = st.number_input(f"Max Value", value=col.get("max_val", 10000), key=f"max_{i}")
                        if col["type"] == "float":
                            col["decimals"] = st.number_input(f"Decimal Places", min_value=0, max_value=10, value=col.get("decimals", 2), key=f"dec_{i}")
                    
                    elif col["type"] == "choice":
                        choices_str = st.text_area(f"Choices (one per line)", 
                                                 value="\n".join(col.get("choices", ["Option1", "Option2", "Option3"])), 
                                                 key=f"choices_{i}")
                        col["choices"] = [choice.strip() for choice in choices_str.split("\n") if choice.strip()]
                    
                    elif col["type"] in ["date", "timestamp"]:
                        col["start_date"] = st.date_input(f"Start Date", 
                                                        value=datetime.strptime(col.get("start_date", "2020-01-01"), "%Y-%m-%d").date(),
                                                        key=f"start_{i}").strftime("%Y-%m-%d")
                        col["end_date"] = st.date_input(f"End Date", 
                                                      value=datetime.strptime(col.get("end_date", "2024-12-31"), "%Y-%m-%d").date(),
                                                      key=f"end_{i}").strftime("%Y-%m-%d")
                    
                    elif col["type"] == "boolean":
                        col["true_rate"] = st.slider(f"True Rate", 0.0, 1.0, col.get("true_rate", 0.5), key=f"true_{i}")
                
                if st.button(f"🗑️ Remove Column {i+1}", key=f"remove_{i}"):
                    st.session_state.columns.pop(i)
                    st.rerun()

# Generate data section
st.header("🚀 Generate Data")

if st.session_state.columns:
    col1_gen, col2_gen = st.columns(2)
    
    with col1_gen:
        # Add SQL warehouse input BEFORE the button
        http_path = st.text_input(
            "SQL Warehouse HTTP Path:", 
            placeholder="/sql/1.0/warehouses/862f1d757f0424f7",
            help="Get this from your SQL Warehouse details page"
        )

        if st.button("🎲 Generate Synthetic Data", type="primary"):
            if not http_path:
                st.error("Please provide SQL Warehouse HTTP Path")
            else:
                try:
                    from databricks import sql
                    from databricks.sdk.core import Config
                    
                    cfg = Config()
                    
                    with st.spinner("Generating synthetic data..."):
                        # Connect to SQL warehouse
                        conn = sql.connect(
                            server_hostname=cfg.host,
                            http_path=http_path,
                            credentials_provider=lambda: cfg.authenticate,
                        )
                        
                        # Generate data using the advanced function
                        df = generate_synthetic_dataframe_advanced(st.session_state.columns, int(row_count))
                        
                        # Write to Unity Catalog
                        full_table_name = f"{catalog}.{schema}.{table_name}"
                        write_to_unity_catalog(full_table_name, df, conn)
                        
                    st.success(f"✅ Synthetic data written to: **{full_table_name}**")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error generating data: {str(e)}")
    with col2_gen:
        if st.button("👀 Preview Schema"):
            st.json({
                "table_info": {
                    "catalog": catalog,
                    "schema": schema,
                    "table_name": table_name,
                    "row_count": row_count,
                    "write_mode": write_mode
                },
                "columns": st.session_state.columns
            })

else:
    st.warning("⚠️ Please add at least one column or load a template to generate data.")

# Footer
st.markdown("---")
st.markdown("💡 **Tips:** Use templates for quick setup, customize null rates for realistic data gaps, and use choice types for categorical data with specific distributions.")