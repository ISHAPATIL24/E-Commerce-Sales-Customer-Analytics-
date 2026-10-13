"""
E-Commerce Analytics Dashboard — Group 4 DVT Lab Assignment
Data Detective Challenge: E-Commerce Sales & Customer Analytics

Run with:
    streamlit run app.py
"""

import os
import sys
import streamlit as st

# Flush cached submodules so Streamlit hot-reloading always loads latest code from disk
for mod_name in list(sys.modules.keys()):
    if any(mod_name.startswith(pkg) for pkg in ("utils", "components", "pages_content")):
        del sys.modules[mod_name]

from utils.data_loader import load_file, clean_dataframe, load_default_dataset
from utils.sample_data import generate_sample_data
from utils.column_detector import detect_columns, has_minimum_viable_data
from components.filters import render_sidebar_filters, render_column_mapping_editor
from pages_content import overview, deep_dive, misleading_vs_correct, ai_critique, data_story, reports



# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Group 4 | E-Commerce Sales Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom metric styling
st.markdown(
    """
    <style>
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #e2e8f0;
        padding: 14px 18px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }
    .sub-caption {
        font-size: 1.0rem;
        color: #64748b;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-header">🛒 E-Commerce Sales & Customer Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-caption">DVT Lab Challenge | Group 4 — Data Detective Investigation</div>', unsafe_allow_html=True)

# ---------------- DATA SOURCE SELECTION ----------------
st.sidebar.title("📁 Data Source")
data_mode = st.sidebar.radio(
    "Choose Dataset Mode",
    [
        "🟢 Real Dataset (Superstore 9,994 rows)",
        "📁 Upload Custom File (CSV/Excel)",
        "🧪 Synthetic Sample (Original 300 rows)"
    ],
    index=0
)

df = None
load_error = None
data_source_label = ""

if data_mode == "🟢 Real Dataset (Superstore 9,994 rows)":
    # Automatically locate sample_superstore.csv in relative data/ directory
    candidate_paths = [
        "data/sample_superstore.csv",
        os.path.join(os.path.dirname(__file__), "data", "sample_superstore.csv")
    ]
    found_path = next((p for p in candidate_paths if os.path.exists(p)), None)
    if found_path:
        df, load_error = load_default_dataset(found_path)
        data_source_label = "Verified Real-World Benchmark: Sample Superstore (9,994 records)"
    else:
        load_error = "Verified dataset data/sample_superstore.csv not found on disk. Please upload via sidebar."
elif data_mode == "📁 Upload Custom File (CSV/Excel)":
    uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx", "xls"])
    if uploaded_file is not None:
        with st.spinner("Parsing uploaded file..."):
            df, load_error = load_file(uploaded_file)
            data_source_label = f"Uploaded Custom File: {uploaded_file.name}"
    else:
        st.info("👆 Please select and upload a `.csv` or `.xlsx` file from your device.")
        st.stop()
elif data_mode == "🧪 Synthetic Sample (Original 300 rows)":
    df = generate_sample_data()
    data_source_label = "Synthetic Demo Dataset (300 mock records generated in-memory)"

# ---------------- ERROR / EMPTY STATES ----------------
if df is None:
    if load_error:
        st.error(f"⚠️ {load_error}")
    else:
        st.info("No data available to display.")
    st.stop()

# Clean and auto-detect columns
df = clean_dataframe(df)
col_map = detect_columns(df)

# Sidebar data badge
st.sidebar.caption(f"**Loaded Data:** {data_source_label}")

# ---------------- DATA PREVIEW EXPANDER ----------------
with st.expander("📄 Data Preview & Metadata", expanded=False):
    st.dataframe(df.head(10), use_container_width=True)
    st.caption(f"Active Dataset: {len(df):,} rows × {len(df.columns)} columns.")

# ---------------- ADVANCED COLUMN MAPPING ----------------
col_map = render_column_mapping_editor(df, col_map)

if not has_minimum_viable_data(col_map):
    st.warning(
        "⚠️ We couldn't automatically detect enough usable columns "
        "(need at least one numeric metric like Sales/Profit and one "
        "category-like column such as Category or Product). "
        "Use **Column Mapping (Advanced)** in the sidebar to map them manually."
    )
    st.stop()

# ---------------- NAVIGATION ROUTING ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Assignment Sections",
    [
        "📊 Executive Overview",
        "🔍 Analytical Deep-Dive (5 Questions)",
        "⚖️ Misleading vs. Correct Visualizations",
        "🤖 AI Visualization Critique",
        "🕵️ Data Story & Findings",
        "📋 Dataset Discovery & Reports"
    ],
    index=0
)

# ---------------- DYNAMIC FILTERS ----------------
filtered_df = render_sidebar_filters(df, col_map)

# ---------------- ROUTE TO COMPONENT ----------------
if page == "📊 Executive Overview":
    overview.render(filtered_df, col_map)
elif page == "🔍 Analytical Deep-Dive (5 Questions)":
    deep_dive.render(filtered_df, col_map)
elif page == "⚖️ Misleading vs. Correct Visualizations":
    misleading_vs_correct.render(filtered_df, col_map)
elif page == "🤖 AI Visualization Critique":
    ai_critique.render()
elif page == "🕵️ Data Story & Findings":
    data_story.render(filtered_df, col_map)
elif page == "📋 Dataset Discovery & Reports":
    reports.render(filtered_df, col_map)

st.markdown("---")
st.caption("Group 4 DVT Lab Submission | Built with Streamlit, Pandas, and Plotly | Academic License CC0")
