import streamlit as st

st.title("🔍 Minimal Test App")
st.write("If you see this, Streamlit is working!")

# Test basic imports one by one
try:
    import json
    st.write("✅ json imported")
except Exception as e:
    st.error(f"❌ json failed: {e}")

try:
    from datetime import datetime, timedelta
    st.write("✅ datetime imported")
except Exception as e:
    st.error(f"❌ datetime failed: {e}")

try:
    import random
    st.write("✅ random imported")
except Exception as e:
    st.error(f"❌ random failed: {e}")

try:
    from faker import Faker
    st.write("✅ faker imported")
except Exception as e:
    st.error(f"❌ faker failed: {e}")

# DON'T test Spark or PySpark yet - that's likely the issue

st.write("✅ Basic app is working!")