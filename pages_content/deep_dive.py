"""
Analytical Deep-Dive Page: 5 Analytical Questions for Group 4 DVT Lab Assignment.
"""

import streamlit as st
from components.charts import (
    subcategory_profitability_chart,
    discount_cliff_scatter,
    pareto_customer_curve,
    region_chart,
    trend_chart,
    state_choropleth,
    month_year_heatmap,
)
from utils.helpers import empty_state


def render(df, col_map):
    st.header("🔍 Analytical Deep-Dive: 5 Core Questions")
    st.caption("Detailed visual investigation into profitability drivers, margins, discounts, and customer tiers.")

    if df.empty:
        empty_state("No rows match current filter selections.")
        return

    # Tabs for the 5 analytical questions
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Q1: Sub-Category Profitability",
        "Q2: Regional Margin Asymmetry",
        "Q3: The Discount Cliff",
        "Q4: Seasonality Dynamics",
        "Q5: Customer Pareto Concentration",
    ])

    with tab1:
        st.subheader("Question 1: Which product lines generate volume but erode profit margins?")
        st.markdown(
            """
            - **Variables:** Independent: `Category`, `Sub-Category` | Dependent: `Sales`, `Profit`, `Margin %`
            - **Proposed Visualization:** Diverging Horizontal Bar Chart with Zero Reference Line.
            - **Justification:** Bars encode linear quantity differences accurately without radial or perspective distortion. Sorting by profit immediately isolates loss leaders (e.g., Tables and Bookcases) in red versus profitable anchors in green.
            """
        )
        subcategory_profitability_chart(df, col_map)
        st.info("💡 **Key Insight:** Tables (-$17.7k loss) and Bookcases (-$3.5k loss) consistently destroy bottom-line value despite generating over $320,000 in combined gross revenue.")

    with tab2:
        st.subheader("Question 2: How do regional sales volumes compare to regional net profitability?")
        st.markdown(
            """
            - **Variables:** Independent: `Region`, `State` | Dependent: `Sales`, `Profit`, `Margin %`
            - **Proposed Visualization:** Grouped Dual-Metric Bar Chart + State-level Choropleth Map.
            - **Justification:** Allows executives to compare gross revenue bars directly against net profit bars within each territory on a unified baseline.
            """
        )
        region_chart(df, col_map)
        state_choropleth(df, col_map)
        st.warning("⚠️ **Key Insight:** The Central Region generates $501k in sales but achieves only a 7.9% profit margin, compared to ~15% in the West, driven by loss-making discounting in Texas and Illinois (average discount ~37–39% there).")

    with tab3:
        st.subheader("Question 3: At what discount threshold does transaction profitability turn negative?")
        st.markdown(
            """
            - **Variables:** Independent: `Discount` (0%–80%) | Dependent: `Profit`, `Sales` (Bubble size)
            - **Proposed Visualization:** Bubble Scatter Plot with Zero-Profit Horizontal Baseline and 20% Discount Ceiling.
            - **Justification:** Scatter plots effectively display the bivariate distribution of continuous financial variables, pinpointing the exact non-linear threshold where profitability collapses.
            """
        )
        discount_cliff_scatter(df, col_map)
        st.error("🚨 **Key Insight:** Transactions with discounts above 20% sharply plunge into negative profits. Clearance markdowns exceeding 50% suffer a catastrophic -119% margin loss.")

    with tab4:
        st.subheader("Question 4: What are the cyclical seasonal demand surges across quarters and years?")
        st.markdown(
            """
            - **Variables:** Independent: `Order Date` (Monthly intervals) | Dependent: `Sales`, `Profit`
            - **Proposed Visualization:** Multi-Line Time-Series Trend Chart + Month x Year Heatmap.
            - **Justification:** Continuous line marks along an ordered temporal axis leverage human visual continuity to detect seasonality, momentum, and YoY growth.
            """
        )
        trend_chart(df, col_map)
        month_year_heatmap(df, col_map)
        st.info("📅 **Key Insight:** E-commerce sales peak dramatically in Q4 (September through December): September, November and December together bring ~43% of annual sales. Profit margin does not collapse in Q4 (12.6% vs 12.4% in Q2), so the seasonal surge is growth, not a margin squeeze.")

    with tab5:
        st.subheader("Question 5: What proportion of total revenue is driven by the top customer tier?")
        st.markdown(
            """
            - **Variables:** Independent: `Customer ID` | Dependent: `Cumulative Sales %`, `Cumulative Customer %`
            - **Proposed Visualization:** Pareto (Lorenz) Distribution Curve against 1:1 Parity Benchmark.
            - **Justification:** Compares actual buyer inequality against theoretical parity, confirming the degree of enterprise reliance on high-value corporate accounts.
            """
        )
        pareto_customer_curve(df, col_map)
        st.success("🎯 **Key Insight:** The top 20% of customer accounts account for 48% of total gross sales, demonstrating moderate concentration without extreme single-account vulnerability.")
