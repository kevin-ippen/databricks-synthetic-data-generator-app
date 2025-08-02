import streamlit as st
import json
from datetime import datetime, timedelta
import random
from faker import Faker
import pandas as pd

# Initialize Spark session and Faker
try:
    spark = SparkSession.builder.getOrCreate()
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

def generate_synthetic_data(spark, catalog, schema, table_name, columns, row_count=1000, mode="overwrite"):
    """Generate synthetic data and write to Unity Catalog"""
    
    # Build Spark schema
    fields = []
    for col in columns:
        col_type = col["type"]
        
        if col_type in ["string", "first_name", "last_name", "email", "phone", "address", "city", "state", "zipcode", "sentence", "text", "choice"]:
            fields.append(StructField(col["name"], StringType(), True))
        elif col_type == "integer":
            fields.append(StructField(col["name"], IntegerType(), True))
        elif col_type == "float":
            fields.append(StructField(col["name"], DoubleType(), True))
        elif col_type == "boolean":
            fields.append(StructField(col["name"], BooleanType(), True))
        elif col_type == "date":
            fields.append(StructField(col["name"], DateType(), True))
        elif col_type == "timestamp":
            fields.append(StructField(col["name"], TimestampType(), True))
        else:
            fields.append(StructField(col["name"], StringType(), True))

    schema_def = StructType(fields)

    # Generate data
    def row_gen(_):
        row = []
        for col in columns:
            row.append(generate_realistic_data(col, fake))
        return tuple(row)

    rdd = spark.sparkContext.parallelize([row_gen(i) for i in range(row_count)])
    df = spark.createDataFrame(rdd, schema_def)

    # Ensure catalog and schema exist
    spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")

    # Write to table
    full_name = f"{catalog}.{schema}.{table_name}"
    df.write.format("delta").mode(mode).saveAsTable(full_name)
    
    return full_name

def generate_synthetic_dataframe(columns, row_count):
    """Generate pandas DataFrame instead of Spark DataFrame"""
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
    """Write DataFrame to Unity Catalog using SQL"""
    with conn.cursor() as cursor:
        rows = list(df.itertuples(index=False))
        values = ",".join([f"({','.join(map(repr, row))})" for row in rows])
        cursor.execute(f"INSERT OVERWRITE {table_name} VALUES {values}")


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
        if st.button("🎲 Generate Synthetic Data", type="primary"):
            try:
                with st.spinner("Generating synthetic data..."):
                    result = generate_synthetic_data(
                        spark=spark,
                        catalog=catalog,
                        schema=schema,
                        table_name=table_name,
                        columns=st.session_state.columns,
                        row_count=int(row_count),
                        mode=write_mode
                    )
                st.success(f"✅ Synthetic data written to: **{result}**")
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