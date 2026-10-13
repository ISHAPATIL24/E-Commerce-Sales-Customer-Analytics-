"""
Dataset Discovery, Quality Audit & Data Export page for Group 4 DVT Lab Assignment.
"""

import streamlit as st
import pandas as pd
from utils.helpers import empty_state


def render(df, col_map):
    st.header("📋 Dataset Discovery & Quality Audit")
    st.caption("Comprehensive data health check, column profiling, and filtered data export.")

    if df.empty:
        empty_state("No rows match current filter selections.")
        return

    # Section 1: Summary Statistics Cards
    st.subheader("1. Structural Dataset Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Active Filtered Rows", f"{len(df):,}")
    c2.metric("Total Attributes", len(df.columns))
    c3.metric("Missing Cells", int(df.isnull().sum().sum()))
    c4.metric("Exact Duplicates", int(df.duplicated().sum()))

    # Section 2: Data Quality & Missing Value Audit
    with st.expander("🔍 Column-by-Column Null Value Audit", expanded=False):
        null_counts = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": [str(t) for t in df.dtypes],
            "Missing Count": df.isnull().sum().values,
            "Missing Pct (%)": (df.isnull().sum().values / len(df) * 100).round(2),
            "Unique Values": [df[c].nunique() for c in df.columns]
        })
        st.dataframe(null_counts, use_container_width=True)

    # Section 3: Data Dictionary Reference
    with st.expander("📖 Data Dictionary & Field Descriptions", expanded=False):
        st.markdown(
            """
            | Column | Type | Business Definition |
            | :--- | :--- | :--- |
            | `Order ID` | Categorical | Unique transaction code (e.g., CA-2016-152156) |
            | `Order Date` | Temporal | Date customer placed order |
            | `Ship Date` | Temporal | Date order was dispatched |
            | `Ship Mode` | Categorical | Fulfillment shipping class (Standard, Second, First, Same Day) |
            | `Customer ID` | Categorical | Unique buyer identifier |
            | `Segment` | Categorical | Consumer, Corporate, or Home Office |
            | `Region` | Categorical | Macro geographic division (West, East, Central, South) |
            | `Category` | Categorical | Furniture, Office Supplies, or Technology |
            | `Sub-Category` | Categorical | 17 granular merchandise classifications |
            | `Sales` | Continuous | Gross transaction revenue ($ USD) |
            | `Quantity` | Discrete | Units purchased in order |
            | `Discount` | Continuous | Commercial discount percentage applied (0.0 to 0.8) |
            | `Profit` | Continuous | Net earnings/loss generated ($ USD) |
            """
        )

    # Section 4: Live Data View & Export
    st.subheader("2. Filtered Dataset Inspection & Export")
    st.dataframe(df.head(100), use_container_width=True)
    st.caption(f"Showing first {min(100, len(df))} of {len(df):,} records matching filters.")

    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="group4_filtered_superstore_data.csv",
        mime="text/csv",
    )
