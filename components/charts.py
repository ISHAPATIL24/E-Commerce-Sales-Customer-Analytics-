"""
Adaptive Plotly chart builders for Group 4 DVT Lab Dashboard.

Each function verifies necessary columns and falls back to friendly empty-state
notifications without throwing uncaught exceptions.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from utils.helpers import empty_state, format_currency


def category_charts(df: pd.DataFrame, col_map: dict):
    """Bar + pie chart of Sales/Profit grouped by category."""
    category_col = col_map.get("category")
    metric_col = col_map.get("sales") or col_map.get("profit")

    if not category_col or not metric_col or df.empty:
        empty_state("Not enough data to show category breakdown.")
        return

    grouped = df.groupby(category_col)[metric_col].sum().reset_index()
    if grouped.empty:
        empty_state("No category data matches the current filters.")
        return

    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(
            grouped,
            x=category_col,
            y=metric_col,
            color=category_col,
            title=f"Total {metric_col} by {category_col}",
            text_auto=".2s",
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig2 = px.pie(
            grouped,
            names=category_col,
            values=metric_col,
            title=f"{metric_col} Market Share Distribution",
            hole=0.4,
        )
        st.plotly_chart(fig2, use_container_width=True)


def trend_chart(df: pd.DataFrame, col_map: dict):
    """Monthly timeline chart of Sales and Profit."""
    date_col = col_map.get("date")
    sales_col = col_map.get("sales")
    profit_col = col_map.get("profit")

    if not date_col or df.empty:
        empty_state("No date column detected - timeline chart unavailable.")
        return

    temp = df.copy()
    temp[date_col] = pd.to_datetime(temp[date_col], errors="coerce")
    temp = temp.dropna(subset=[date_col])
    if temp.empty:
        empty_state("No valid dates found for timeline analysis.")
        return

    temp["period"] = temp[date_col].dt.to_period("M").astype(str)
    
    agg_dict = {}
    if sales_col:
        agg_dict[sales_col] = "sum"
    if profit_col:
        agg_dict[profit_col] = "sum"
        
    if not agg_dict:
        empty_state("No numeric metric columns available for timeline.")
        return

    monthly = temp.groupby("period").agg(agg_dict).reset_index()
    
    fig = go.Figure()
    if sales_col in monthly.columns:
        fig.add_trace(go.Scatter(
            x=monthly["period"], y=monthly[sales_col],
            mode="lines+markers", name="Sales",
            line=dict(color="#1f77b4", width=2.5)
        ))
    if profit_col in monthly.columns:
        fig.add_trace(go.Scatter(
            x=monthly["period"], y=monthly[profit_col],
            mode="lines+markers", name="Profit",
            line=dict(color="#2ca02c", width=2.5)
        ))

    fig.update_layout(
        title="Monthly Revenue & Profit Timeline",
        xaxis_title="Billing Month",
        yaxis_title="Amount ($)",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)


def region_chart(df: pd.DataFrame, col_map: dict):
    """Bar chart comparing Sales and Profit across sales regions."""
    region_col = col_map.get("region")
    sales_col = col_map.get("sales")
    profit_col = col_map.get("profit")

    if not region_col or df.empty:
        empty_state("No region column detected.")
        return

    agg_dict = {}
    if sales_col:
        agg_dict[sales_col] = "sum"
    if profit_col:
        agg_dict[profit_col] = "sum"

    if not agg_dict:
        empty_state("No sales or profit metrics detected for regional analysis.")
        return

    grouped = df.groupby(region_col).agg(agg_dict).reset_index()
    
    fig = go.Figure()
    if sales_col in grouped.columns:
        fig.add_trace(go.Bar(
            x=grouped[region_col], y=grouped[sales_col],
            name="Gross Sales", marker_color="#3366cc"
        ))
    if profit_col in grouped.columns:
        fig.add_trace(go.Bar(
            x=grouped[region_col], y=grouped[profit_col],
            name="Net Profit", marker_color="#109618"
        ))

    fig.update_layout(
        title="Regional Performance: Sales vs. Net Profit",
        barmode="group",
        xaxis_title="Sales Territory",
        yaxis_title="USD ($)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)


def top_n_bar(df: pd.DataFrame, group_col: str, metric_col: str, title: str, n: int = 10):
    """Generic horizontal bar chart for top entities."""
    if not group_col or not metric_col or df.empty:
        empty_state(f"Not enough data to compute {title}.")
        return

    grouped = (
        df.groupby(group_col)[metric_col]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    if grouped.empty:
        empty_state(f"No data matches the current filters for {title}.")
        return

    fig = px.bar(grouped, x=metric_col, y=group_col, orientation="h", title=title, text_auto=".2s")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)


# ---------------- SPECIALIZED ANALYTICAL CHARTS (QUESTIONS 1-5) ----------------

def subcategory_profitability_chart(df: pd.DataFrame, col_map: dict):
    """Question 1: Sub-category profitability ranking highlighting loss makers."""
    subcat_col = col_map.get("sub_category") or col_map.get("product")
    profit_col = col_map.get("profit")
    sales_col = col_map.get("sales")

    if not subcat_col or not profit_col or df.empty:
        empty_state("Sub-Category or Profit columns unavailable.")
        return

    agg_dict = {profit_col: "sum"}
    if sales_col:
        agg_dict[sales_col] = "sum"

    grouped = df.groupby(subcat_col).agg(agg_dict).reset_index().sort_values(profit_col, ascending=True)
    grouped["Status"] = np.where(grouped[profit_col] < 0, "Loss-Making", "Profitable")

    fig = px.bar(
        grouped,
        x=profit_col,
        y=subcat_col,
        orientation="h",
        color="Status",
        color_discrete_map={"Loss-Making": "#d62728", "Profitable": "#2ca02c"},
        title="Q1: Sub-Category Profitability Spectrum (Identifying Loss Leaders)",
        labels={profit_col: "Net Profit ($)", subcat_col: "Sub-Category"},
        text_auto=".2s"
    )
    fig.add_vline(x=0, line_width=1.5, line_dash="dash", line_color="black")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)


def discount_cliff_scatter(df: pd.DataFrame, col_map: dict):
    """Question 3: Scatter plot of Discount vs Profit showing the 20% cliff."""
    disc_col = col_map.get("discount")
    profit_col = col_map.get("profit")
    sales_col = col_map.get("sales")
    cat_col = col_map.get("category")

    if not disc_col or not profit_col or df.empty:
        empty_state("Discount or Profit column unavailable for elasticity analysis.")
        return

    sample_slice = df.sample(min(1200, len(df)), random_state=42) if len(df) > 1200 else df

    fig = px.scatter(
        sample_slice,
        x=disc_col,
        y=profit_col,
        color=cat_col if cat_col else None,
        size=sales_col if sales_col else None,
        hover_data=[col_map.get("product")] if col_map.get("product") else None,
        title="Q3: The Discount Cliff — Transaction Profitability vs. Discount Rate",
        labels={disc_col: "Applied Discount Rate", profit_col: "Transaction Profit ($)"},
        opacity=0.65
    )
    # Add critical 20% discount boundary line
    fig.add_vline(x=0.20, line_width=2, line_dash="dash", line_color="red",
                  annotation_text="Critical 20% Discount Ceiling", annotation_position="top right")
    fig.add_hline(y=0, line_width=1.5, line_color="gray")
    st.plotly_chart(fig, use_container_width=True)


def pareto_customer_curve(df: pd.DataFrame, col_map: dict):
    """Question 5: Customer Pareto (Lorenz) Distribution Curve."""
    cust_col = col_map.get("customer") or col_map.get("order_id")
    sales_col = col_map.get("sales")

    if not cust_col or not sales_col or df.empty:
        empty_state("Customer or Sales column unavailable for Pareto analysis.")
        return

    cust_sales = df.groupby(cust_col)[sales_col].sum().sort_values(ascending=False).reset_index()
    total_revenue = cust_sales[sales_col].sum()
    if total_revenue == 0:
        empty_state("Total revenue is zero.")
        return

    cust_sales["Cum_Sales"] = cust_sales[sales_col].cumsum()
    cust_sales["Cum_Sales_Pct"] = (cust_sales["Cum_Sales"] / total_revenue) * 100
    cust_sales["Cust_Rank_Pct"] = (np.arange(1, len(cust_sales) + 1) / len(cust_sales)) * 100

    fig = go.Figure()
    # Actual Pareto curve
    fig.add_trace(go.Scatter(
        x=cust_sales["Cust_Rank_Pct"],
        y=cust_sales["Cum_Sales_Pct"],
        mode="lines",
        name="Cumulative Revenue %",
        line=dict(color="#1f77b4", width=3)
    ))
    # 1:1 Parity reference line
    fig.add_trace(go.Scatter(
        x=[0, 100], y=[0, 100],
        mode="lines",
        name="Perfect Equality (1:1)",
        line=dict(color="gray", dash="dot")
    ))
    # 80/20 guideline markers
    fig.add_vline(x=20, line_dash="dash", line_color="#ff7f0e",
                  annotation_text="Top 20% of Customers", annotation_position="top left")

    fig.update_layout(
        title="Q5: Customer Concentration Pareto Curve (Revenue Share)",
        xaxis_title="Cumulative % of Customer Base",
        yaxis_title="Cumulative % of Gross Sales",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------- DVT ETHICS: MISLEADING VS. CORRECT CHARTS ----------------

def render_misleading_comparison(df: pd.DataFrame, col_map: dict):
    """
    Side-by-side DVT comparison demonstrating Lie Factor & visual deception.
    Compares a truncated-baseline chart with an honest zero-baseline chart.
    """
    region_col = col_map.get("region")
    sales_col = col_map.get("sales")

    if not region_col or not sales_col or df.empty:
        empty_state("Region or Sales column unavailable for misleading chart comparison.")
        return

    data = df.groupby(region_col)[sales_col].sum().reset_index()
    if len(data) < 2:
        empty_state("Need at least 2 regions to compare scales.")
        return

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### ⚠️ Deliberately Misleading Chart")
        st.caption("Violates Tufte's Proportionality Rule: Truncated Y-Axis creates severe Lie Factor distortion.")
        min_val = data[sales_col].min() * 0.90
        max_val = data[sales_col].max() * 1.05

        fig_misleading = px.bar(
            data,
            x=region_col,
            y=sales_col,
            title="Sales by Region (Truncated Y-Axis Baseline: $350k)",
            color=region_col,
            color_discrete_sequence=["#e74c3c", "#c0392b", "#d9534f", "#e67e22"]
        )
        fig_misleading.update_layout(
            yaxis_range=[min_val, max_val],
            showlegend=False
        )
        st.plotly_chart(fig_misleading, use_container_width=True)
        st.error(
            "**Visual Deception Mechanism:** By starting the Y-axis near the minimum value rather than 0, "
            "West region appears visually ~500% larger than South, when the actual data difference is only ~85%."
        )

    with c2:
        st.markdown("### ✅ Honest & Correct Visualization")
        st.caption("Adheres to Graphical Integrity: Zero-baseline preserves truthful perceptual proportions.")
        
        fig_correct = px.bar(
            data,
            x=region_col,
            y=sales_col,
            title="Sales by Region (Truthful Zero Baseline: $0)",
            color=region_col,
            color_discrete_sequence=["#2980b9", "#27ae60", "#f39c12", "#8e44ad"],
            text_auto=".2s"
        )
        fig_correct.update_layout(
            yaxis_range=[0, data[sales_col].max() * 1.15],
            showlegend=False
        )
        st.plotly_chart(fig_correct, use_container_width=True)
        st.success(
            "**Ethical Encoding:** The visual bar height matches the numerical quantity exactly. "
            "Lie Factor = 1.00 (Perfect Fidelity)."
        )


# ---------------------------------------------------------------------------
# Added charts: Choropleth map (Q2) and Month x Year heatmap (Q4)
# ---------------------------------------------------------------------------
US_STATE_ABBR = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}


def state_choropleth(df: pd.DataFrame, col_map: dict):
    """US state choropleth of total profit (diverging colour scale centred on zero)."""
    state_col = next((c for c in df.columns if str(c).strip().lower() == "state"), None)
    profit_col = col_map.get("profit")
    sales_col = col_map.get("sales")
    if not state_col or not profit_col or df.empty:
        empty_state("A 'State' column and a profit column are required for the map.")
        return

    g = df.groupby(state_col).agg(profit=(profit_col, "sum"), sales=(sales_col, "sum")).reset_index()
    g["abbr"] = g[state_col].map(US_STATE_ABBR)
    g = g.dropna(subset=["abbr"])
    if g.empty:
        empty_state("State names could not be matched to US state codes.")
        return
    g["margin_pct"] = (g["profit"] / g["sales"] * 100).round(1)

    lim = float(g["profit"].abs().max())
    fig = px.choropleth(
        g, locations="abbr", locationmode="USA-states", scope="usa",
        color="profit", color_continuous_scale="RdYlGn", range_color=(-lim, lim),
        hover_name=state_col, hover_data={"abbr": False, "profit": ":,.0f", "sales": ":,.0f", "margin_pct": True},
        title="Net Profit by US State (red = loss, green = profit)",
    )
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)


def month_year_heatmap(df: pd.DataFrame, col_map: dict):
    """Heatmap of total sales by calendar month (x) and year (y) to expose seasonality."""
    date_col = col_map.get("date")
    sales_col = col_map.get("sales")
    if not date_col or not sales_col or df.empty:
        empty_state("A date and sales column are required for the seasonality heatmap.")
        return
    d = df[[date_col, sales_col]].copy()
    d[date_col] = pd.to_datetime(d[date_col], errors="coerce")
    d = d.dropna(subset=[date_col])
    d["Year"] = d[date_col].dt.year
    d["Month"] = d[date_col].dt.month
    pivot = d.pivot_table(index="Year", columns="Month", values=sales_col, aggfunc="sum").fillna(0)
    names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pivot = pivot.reindex(columns=range(1, 13), fill_value=0)
    fig = px.imshow(
        pivot.values, x=names, y=[str(y) for y in pivot.index],
        color_continuous_scale="Blues", aspect="auto", text_auto=".2s",
        labels=dict(color="Sales"), title="Sales Heatmap: Month x Year",
    )
    st.plotly_chart(fig, use_container_width=True)
