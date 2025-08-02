import streamlit as st
import json
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config
from faker import Faker
from collections import OrderedDict
from datetime import datetime, timedelta
import random
from templates import TEMPLATES

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

def generate_realistic_data(col_config, fake):
    """Generate realistic data using Faker's advanced capabilities"""
    col_type = col_config["type"]
    null_rate = col_config.get("null_rate", 0)
    locale = col_config.get("locale", "en_US")
    
    # Handle null values
    if random.random() < null_rate:
        return None
    
    # Initialize localized faker if needed
    if locale != "en_US":
        fake_local = Faker(locale)
    else:
        fake_local = fake
    
    # === ENHANCED FAKER TYPES ===
    
    # Business & Professional
    if col_type == "company_email":
        first = fake_local.first_name().lower()
        last = fake_local.last_name().lower()
        company = fake_local.company().split()[0].lower()
        return f"{first}.{last}@{company}.com"
    
    elif col_type == "business_phone":
        return fake_local.phone_number()
    
    elif col_type == "job_title":
        return fake_local.job()
    
    elif col_type == "company_name":
        return fake_local.company()
    
    elif col_type == "website_url":
        return fake_local.url()
    
    # Financial
    elif col_type == "credit_card":
        card_type = col_config.get("card_type", None)
        return fake_local.credit_card_number(card_type=card_type)
    
    elif col_type == "iban":
        return fake_local.iban()
    
    elif col_type == "currency_amount":
        min_val = col_config.get("min_val", 10.00)
        max_val = col_config.get("max_val", 10000.00)
        decimals = col_config.get("decimals", 2)
        return round(fake_local.pyfloat(min_value=min_val, max_value=max_val), decimals)
    
    # Geographic (with proper correlations)
    elif col_type == "localized_address":
        return fake_local.address().replace('\n', ', ')
    
    elif col_type == "coordinates":
        return f"{fake_local.latitude()}, {fake_local.longitude()}"
    
    elif col_type == "country":
        return fake_local.country()
    
    # Enhanced Text
    elif col_type == "product_name":
        adjectives = ['Premium', 'Deluxe', 'Professional', 'Smart', 'Ultra', 'Pro']
        nouns = ['Widget', 'Device', 'Tool', 'System', 'Solution', 'Platform']
        return f"{fake_local.random_element(adjectives)} {fake_local.random_element(nouns)}"
    
    elif col_type == "review_text":
        min_sentences = col_config.get("min_sentences", 2)
        max_sentences = col_config.get("max_sentences", 5)
        sentences = []
        for _ in range(fake_local.random_int(min_sentences, max_sentences)):
            sentences.append(fake_local.sentence())
        return " ".join(sentences)
    
    elif col_type == "hashtag":
        words = fake_local.words(nb=fake_local.random_int(1, 3))
        return "#" + "".join(word.capitalize() for word in words)
    
    # Enhanced Dates with Business Logic
    elif col_type == "business_date":
        # Only weekdays
        start_date = col_config.get("start_date", "2024-01-01")
        end_date = col_config.get("end_date", "2024-12-31")
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        while True:
            random_date = fake_local.date_between(start_date=start, end_date=end)
            if random_date.weekday() < 5:  # Monday = 0, Friday = 4
                return random_date
    
    elif col_type == "business_hours_timestamp":
        # Business hours only (9 AM - 5 PM)
        start_date = col_config.get("start_date", "2024-01-01")
        end_date = col_config.get("end_date", "2024-12-31")
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        random_date = fake_local.date_between(start_date=start, end_date=end)
        business_hour = fake_local.random_int(9, 17)  # 9 AM to 5 PM
        business_minute = fake_local.random_int(0, 59)
        
        return datetime.combine(random_date, datetime.min.time().replace(hour=business_hour, minute=business_minute))
    
    # Enhanced Choices with Realistic Weights
    elif col_type == "weighted_choice":
        choices = col_config.get("choices", ["A", "B", "C"])
        weights = col_config.get("weights", None)
        if weights:
            return fake_local.random_element(elements=OrderedDict(zip(choices, weights)))
        else:
            return fake_local.random_element(choices)
    
    # ID Generators with Realistic Formats
    elif col_type == "realistic_id":
        prefix = col_config.get("prefix", "ID")
        length = col_config.get("length", 8)
        format_type = col_config.get("format", "alphanumeric")  # numeric, alpha, alphanumeric
        
        if format_type == "numeric":
            suffix = ''.join([str(fake_local.random_digit()) for _ in range(length)])
        elif format_type == "alpha":
            suffix = ''.join([fake_local.random_letter().upper() for _ in range(length)])
        else:  # alphanumeric
            suffix = fake_local.bothify('?' * length).upper()
        
        return f"{prefix}-{suffix}"
    
    # === EXISTING TYPES (keep these) ===
    elif col_type == "string":
        if "pattern" in col_config:
            pattern = col_config["pattern"]
            if "{random_int:" in pattern:
                start = pattern.find("{random_int:") + 12
                end = pattern.find("}", start)
                min_val, max_val = map(int, pattern[start:end].split(":"))
                return pattern.replace(f"{{random_int:{min_val}:{max_val}}}", str(random.randint(min_val, max_val)))
        return fake_local.word()
    
    elif col_type == "first_name":
        return fake_local.first_name()
    elif col_type == "last_name":
        return fake_local.last_name()
    elif col_type == "email":
        return fake_local.email()
    elif col_type == "phone":
        return fake_local.phone_number()
    elif col_type == "address":
        return fake_local.address().replace('\n', ', ')
    elif col_type == "city":
        return fake_local.city()
    elif col_type == "state":
        return fake_local.state()
    elif col_type == "zipcode":
        return fake_local.zipcode()
    elif col_type == "sentence":
        min_words = col_config.get("min_words", 5)
        max_words = col_config.get("max_words", 15)
        return fake_local.sentence(nb_words=fake_local.random_int(min_words, max_words))
    elif col_type == "text":
        min_sentences = col_config.get("min_sentences", 1)
        max_sentences = col_config.get("max_sentences", 3)
        sentences = []
        for _ in range(fake_local.random_int(min_sentences, max_sentences)):
            sentences.append(fake_local.sentence())
        return " ".join(sentences)
    elif col_type == "integer":
        min_val = col_config.get("min_val", 0)
        max_val = col_config.get("max_val", 10000)
        return fake_local.random_int(min_val, max_val)
    elif col_type == "float":
        min_val = col_config.get("min_val", 0.0)
        max_val = col_config.get("max_val", 10000.0)
        decimals = col_config.get("decimals", 2)
        return round(fake_local.pyfloat(min_value=min_val, max_value=max_val), decimals)
    elif col_type == "boolean":
        true_rate = col_config.get("true_rate", 0.5)
        return fake_local.random.random() < true_rate
    elif col_type == "choice":
        choices = col_config.get("choices", ["A", "B", "C"])
        weights = col_config.get("weights", None)
        if weights and len(weights) == len(choices):
            return fake_local.random_element(elements=OrderedDict(zip(choices, weights)))
        else:
            return fake_local.random_element(choices)
    elif col_type == "date":
        start_date_str = col_config.get("start_date", "2020-01-01")
        end_date_str = col_config.get("end_date", "2024-12-31")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        return fake_local.date_between(start_date=start_date, end_date=end_date)
    elif col_type == "timestamp":
        start_date_str = col_config.get("start_date", "2024-01-01")
        end_date_str = col_config.get("end_date", "2024-12-31")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        return fake_local.date_time_between(start_date=start_date, end_date=end_date)
    else:
        return fake_local.word()

def generate_advanced_dataframe(columns, row_count):
    """Generate DataFrame using advanced template configurations"""
    data = []
    for i in range(row_count):
        row = {}
        for col in columns:
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
            
            # Step 1: Create table with proper schema
            column_definitions = []
            for col_name, dtype in df.dtypes.items():
                sql_type = get_sql_type(dtype)
                column_definitions.append(f"`{col_name}` {sql_type}")
            
            columns_sql = ", ".join(column_definitions)
            
            create_table_sql = f"""
            CREATE OR REPLACE TABLE {table_name} (
                {columns_sql}
            ) USING DELTA
            """
            
            cursor.execute(create_table_sql)
            
            # Step 2: Insert data
            if len(df) > 0:
                # Get column names for INSERT
                column_names = ", ".join([f"`{col}`" for col in df.columns])
                
                # Process rows
                clean_rows = []
                for _, row in df.iterrows():
                    clean_values = [clean_value(val) for val in row]
                    clean_rows.append(f"({','.join(clean_values)})")
                
                values = ",".join(clean_rows)
                
                insert_sql = f"""
                INSERT INTO {table_name} ({column_names})
                VALUES {values}
                """
                
                cursor.execute(insert_sql)
            
            st.write(f"✅ Created table with columns: {list(df.columns)}")

# Streamlit UI
st.set_page_config(page_title="Advanced Synthetic Data Generator", layout="wide")
st.title("🎯 Advanced Synthetic Data Generator")
st.markdown("Generate realistic synthetic data with 20+ B2C templates or custom configurations")

# Sidebar configuration
with st.sidebar:
    st.header("📋 Configuration")
    
    # SQL Warehouse configuration
    http_path = st.text_input(
        "SQL Warehouse HTTP Path:", 
        placeholder="/sql/1.0/warehouses/862f1d757f0424f7",
        help="Get this from your SQL Warehouse details page"
    )
    
    catalog = st.text_input("Unity Catalog", "users")
    schema = st.text_input("Schema", "kevin_ippen")
    table_name = st.text_input("Table Name", "synthetic_table")
    row_count = st.number_input("Row Count", min_value=100, max_value=100000, value=1000)

# Main content - Template Selection
col1, col2 = st.columns([1, 2])

with col1:
    st.header("🎨 Template Selection")
    template_names = list(TEMPLATES.keys())
    selected_template = st.selectbox(
        "Choose a Template",
        template_names,
        help="Select a pre-built B2C template or 'Custom' to build your own"
    )
    
    if selected_template != "Custom":
        template_info = TEMPLATES[selected_template]
        st.info(f"**{selected_template}**\n\n{template_info['description']}")
        
        # Show template details
        with st.expander("📋 Template Details"):
            st.write(f"**Columns:** {len(template_info['columns'])}")
            for col in template_info['columns'][:5]:  # Show first 5 columns
                st.write(f"• **{col['name']}** ({col['type']})")
            if len(template_info['columns']) > 5:
                st.write(f"... and {len(template_info['columns']) - 5} more columns")
        
        if st.button("📥 Load Template", type="primary"):
            st.session_state.columns = template_info["columns"].copy()
            st.success(f"✅ Loaded {selected_template} template!")
            st.rerun()

with col2:
    st.header("⚙️ Column Configuration")
    
    # Initialize session state
    if "columns" not in st.session_state:
        st.session_state.columns = []
    
    if st.session_state.columns:
        st.write(f"**Current Schema:** {len(st.session_state.columns)} columns")
        
        # Show column summary
        col_summary = pd.DataFrame([
            {
                "Column": col["name"], 
                "Type": col["type"],
                "Null Rate": f"{col.get('null_rate', 0)*100:.1f}%"
            } 
            for col in st.session_state.columns
        ])
        st.dataframe(col_summary, hide_index=True)
        
        # Preview data
        if st.button("👀 Preview Data"):
            sample_df = generate_advanced_dataframe(st.session_state.columns, 5)
            st.write("**Sample Data Preview:**")
            st.dataframe(sample_df)
    else:
        st.info("👆 Select a template above or add custom columns below")

# Custom column builder
st.header("🔧 Custom Column Builder")
if st.button("➕ Add Custom Column"):
    st.session_state.columns.append({
        "name": f"custom_col_{len(st.session_state.columns) + 1}",
        "type": "string",
        "null_rate": 0.0
    })
    st.rerun()

# Generate Data Section
st.header("🚀 Generate Synthetic Data")

if st.session_state.columns:
    col1_gen, col2_gen, col3_gen = st.columns(3)
    
    with col1_gen:
        if st.button("🎲 Generate Data", type="primary"):
            if not http_path:
                st.error("Please provide SQL Warehouse HTTP Path")
            else:
                try:
                    with st.spinner("Generating synthetic data..."):
                        conn = get_connection(http_path)
                        df = generate_advanced_dataframe(st.session_state.columns, int(row_count))
                        full_table_name = f"{catalog}.{schema}.{table_name}"
                        write_to_unity_catalog(full_table_name, df, conn)
                    st.success(f"✅ {row_count:,} rows written to: **{full_table_name}**")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2_gen:
        if st.button("📊 Preview Schema"):
            st.json({
                "table_name": f"{catalog}.{schema}.{table_name}",
                "row_count": row_count,
                "columns": len(st.session_state.columns),
                "schema": st.session_state.columns
            })
    
    with col3_gen:
        if st.button("🗑️ Clear Schema"):
            st.session_state.columns = []
            st.rerun()

else:
    st.warning("⚠️ Please select a template or add custom columns to generate data")

# Footer
st.markdown("---")
st.markdown("💡 **Pro Tips:** Use templates for realistic B2C data, preview before generating large datasets, and check null rates for data quality simulation.")