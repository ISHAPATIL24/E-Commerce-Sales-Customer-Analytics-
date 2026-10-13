"""
Executive Dashboard Overview page for Group 4 DVT Lab Assignment.
"""

import streamlit as st
from components.kpi import render_kpis
from components.charts import category_charts, trend_chart, region_chart
from utils.helpers import empty_state


def render(df, col_map):
    st.header("📊 Executive Overview Dashboard")
    st.caption("Group 4: E-Commerce Sales & Customer Analytics | Data Detective Investigation")

    if df.empty:
        empty_state("No data matches current filter criteria. Please adjust your sidebar filters.")
        return

    # Render 5-card KPI Header
    render_kpis(df, col_map)
    st.divider()

    # Strategic Performance Callouts
    category_col = col_map.get("category")
    product_col = col_map.get("product")
    sales_col = col_map.get("sales")
    profit_col = col_map.get("profit")

    col_a, col_b = st.columns(2)
    if category_col and sales_col:
        top_cat = df.groupby(category_col)[sales_col].sum().idxmax()
        col_a.info(f"🏆 **Top Sales Category:** {top_cat}")
    if profit_col and category_col:
        top_profit_cat = df.groupby(category_col)[profit_col].sum().idxmax()
        col_b.success(f"💎 **Top Profit Contributor:** {top_profit_cat}")

    # Section 1: Category Market Share & Performance
    st.subheader("1. Category Breakdown & Market Distribution")
    category_charts(df, col_map)

    # Section 2: Temporal Revenue & Profit Dynamics
    st.subheader("2. Revenue & Net Profit Trend Over Time")
    trend_chart(df, col_map)

    # Section 3: Macro-Regional Performance
    st.subheader("3. Regional Sales & Profit Comparison")
    region_chart(df, col_map)
