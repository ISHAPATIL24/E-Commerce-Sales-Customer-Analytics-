# Analytical Questions & Visualization Design Plan

**Course:** Data Visualization Techniques (DVT) Lab  
**Project:** Data Detective Challenge  
**Team:** Group 4 (E-Commerce Sales & Customer Analytics)  

---

## Analytical Matrix Overview

| # | Analytical Question | Required Variables | Proposed Visualization | Justification & Visual Encoding |
| :---: | :--- | :--- | :--- | :--- |
| **Q1** | **Category & Sub-Category Profit Disparity:** Which product lines generate volume but erode profit margins? | Independent: `Category`, `Sub-Category`<br>Dependent: `Sales`, `Profit`, `Profit Margin %` | **Dual-Metric Grouped Bar Chart / Diverging Horizontal Bar Chart** | Grouped or diverging bars position positive and negative profits clearly relative to a zero baseline, preventing the misinterpretation that high sales imply profitability. |
| **Q2** | **Regional Performance & Margin Asymmetry:** How do regional sales volumes compare to regional net profitability? | Independent: `Region`, `State`<br>Dependent: `Sales`, `Profit`, `Margin %` | **Grouped Regional Bar Chart + State Choropleth Map** | Encodes geographical distribution directly; enables immediate visual isolation of underperforming regions (e.g., Central Region's low margin vs. high turnover). |
| **Q3** | **Discount Cliff & Elasticity:** At what discount threshold does transaction profitability turn negative? | Independent: `Discount` (0%–80%)<br>Dependent: `Profit`, `Sales`, `Quantity` | **Bubble Scatter Plot with Zero-Reference Threshold & OLS Trend** | Scatter plotting encodes continuous variables on Cartesian coordinates ($X=\text{Discount}$, $Y=\text{Profit}$, Size=$\text{Sales}$), revealing the non-linear inflection point where profits collapse. |
| **Q4** | **Temporal Dynamics & Seasonality:** What are the cyclical seasonal demand surges across quarters and years? | Independent: `Order Date` (Monthly/Quarterly aggregations)<br>Dependent: `Sales`, `Profit` | **Multi-Series Time-Series Line Chart with Rolling 3-Month Moving Average** | Line marks provide continuous perceptual continuity along the temporal X-axis, supporting trend detection, Q4 holiday peaks, and YoY performance tracking. |
| **Q5** | **Customer Concentration (Pareto Principle):** What proportion of total revenue is driven by the top customer tier? | Independent: `Customer ID`, `Customer Name`<br>Dependent: `Cumulative Sales %`, `Cumulative Customer %` | **Pareto Curve (Lorenz Curve) with 80/20 Reference Lines** | Combines sorted customer percentiles with cumulative revenue contribution, testing the classical 80/20 rule and isolating key-account reliance. |

---

## Detailed Methodological Justifications

### Question 1: Product Hierarchy Profitability
- **Business Rationale:** E-commerce operations often fall prey to the "gross turnover fallacy," prioritizing high-volume SKUs without recognizing that fulfillment, returns, and wholesale pricing make them loss-leaders.
- **Visual Encoding:** Sub-categories plotted along the Y-axis, sorted by Net Profit. Green bars depict positive margin contributions (e.g., Copiers, Phones), while sharp red bars alert executives to loss leaders (e.g., Tables at -$17,725 and Bookcases at -$3,472).

### Question 2: Regional Performance & Profit Erosion
- **Business Rationale:** Identifying which operational territories require pricing recalibration or logistics restructuring.
- **Visual Encoding:** Macro-regions (`West`, `East`, `Central`, `South`) rendered side-by-side with grouped Sales and Profit metrics, augmented by state-level drill-down tables to show state-specific anomalies (e.g., Texas and Illinois dragging down Central).

### Question 3: The Discount Destruction Curve
- **Business Rationale:** Sales teams frequently apply promotional discounts to close deals, assuming volume compensates for margin loss.
- **Visual Encoding:** Plotting each transaction as a mark with `Discount` on the horizontal axis and `Profit` on the vertical axis. A distinct red shaded region highlights transactions past the 20% discount mark where the trend line plunges into negative territory.

### Question 4: Temporal Seasonality & Growth Trajectory
- **Business Rationale:** Inventory management and cash-flow forecasting require understanding seasonal spikes (such as Q4 Black Friday / Cyber Monday surges).
- **Visual Encoding:** Monthly chronological lines tracking Sales (solid blue) and Profit (emerald green) from 2014 through 2017, illustrating consistent Q4 revenue surges with broadly stable margins (Q4 12.6% vs Q2 12.4%); a Month x Year heatmap reinforces the seasonal pattern.

### Question 5: Customer Concentration & Lifetime Value
- **Business Rationale:** Assessing enterprise vulnerability to customer churn.
- **Visual Encoding:** Sorting 793 customers by sales volume in descending order and computing cumulative percentage curves against a theoretical 1:1 parity line. Shows that the top 20% of customers account for ~48% of total revenue.
