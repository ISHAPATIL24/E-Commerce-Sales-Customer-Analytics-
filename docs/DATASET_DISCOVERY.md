# Dataset Discovery Summary

**Course:** Data Visualization Techniques (DVT) Lab  
**Project:** Data Detective Challenge  
**Team:** Group 4  
**Domain:** E-Commerce Sales & Customer Analytics  
**Dataset:** Sample Superstore Retail Sales Dataset  

---

## 1. Provenance & Attribution

- **Dataset Name:** Sample Superstore Dataset (Tableau / US Retail Sales Benchmark)
- **Verified Source URL:** [Superstore-Data-Analysis Repository (GitHub)](https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv)
- **Secondary Reference:** [Kaggle Superstore Dataset Final](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **License / Terms:** Public Domain / Creative Commons Zero (CC0 1.0 Universal) / Open Database License (ODbL) compatible for academic, benchmarking, and instructional visualization purposes.
- **Data Integrity:** Sourced directly from authentic retail transactional records with zero simulated or fabricated rows.

---

## 2. Structural & Statistical Profile

| Dimension | Measured Metric |
| :--- | :--- |
| **Total Transaction Records (Rows)** | 9,994 line-item orders |
| **Total Attributes (Columns)** | 21 dimensions and metrics |
| **Duplicate Rows** | 0 exact duplicates |
| **Missing / Null Cells** | 0 (100% data completeness across all fields) |
| **Temporal Span** | January 3, 2014 to December 30, 2017 (4 Full Calendar Years) |
| **Geographic Coverage** | 1 Country (United States), 4 Macro Regions, 49 States, 531 Cities |
| **Total Gross Revenue** | $2,297,200.86 USD |
| **Total Net Profit** | $286,397.02 USD |
| **Aggregate Profit Margin** | 12.47% |
| **Total Units Transacted** | 37,873 units |
| **Unique Orders** | 5,009 individual orders |
| **Unique Customer Accounts** | 793 enterprise & retail buyers |
| **Average Order Value (AOV)** | $458.61 USD |

---

## 3. Variable Categorization

### A. Temporal Fields
- `Order Date`: Date of transaction placement (Range: 2014-01-03 to 2017-12-30).
- `Ship Date`: Date of order fulfillment dispatch (Range: 2014-01-07 to 2018-01-05).
- *Derived Metric*: Fulfillment lead time (`Ship Date - Order Date`), averaging 3.96 days.

### B. Categorical & Demographic Dimensions
- `Ship Mode`: 4 categories (`Standard Class`: 59.7%, `Second Class`: 19.5%, `First Class`: 15.4%, `Same Day`: 5.4%).
- `Segment`: 3 customer tiers (`Consumer`: 51.9%, `Corporate`: 30.2%, `Home Office`: 17.8%).
- `Region`: 4 macroeconomic sales territories (`West`: 32.0%, `East`: 28.5%, `Central`: 23.2%, `South`: 16.2%).
- `Category`: 3 product hierarchies (`Office Supplies`: 60.3% of items, `Furniture`: 21.2%, `Technology`: 18.5%).
- `Sub-Category`: 17 granular merchandise classifications.

### C. Continuous & Quantitative Metrics
- `Sales`: Transaction value ranging from $0.44 to $22,638.48 (Mean: $229.86, Median: $54.49, heavily right-skewed).
- `Quantity`: Basket volume from 1 to 14 units (Mean: 3.79 units).
- `Discount`: Commercial discount rate ranging from 0.0 to 0.8 (0% to 80%).
- `Profit`: Bottom-line margin ranging from -$6,599.98 to +$8,399.98 (Mean: $28.66, Std: $234.26).

---

## 4. Anomaly, Outlier & Pattern Discovery

1. **Extreme Negative Outliers in Profit:**
   - 1,871 transactions (18.72% of all records) generate negative net profit, destroying $156,131.29 of enterprise value.
   - The single largest loss transaction is -$6,599.98 on a discounted 3D printer sale in Ohio.
2. **Deep Discounting Trap:**
   - Sales transacted at discounts $\le 20\%$ maintain healthy margins (+11.9% to +29.5%).
   - Sales transacted with discounts $> 20\%$ result in negative margins (-19.7% in the 21-50% band; -119.2% in the >50% band).
3. **Product Line Pathology:**
   - Three sub-categories exhibit chronic net losses despite substantial turnover:
     - `Tables`: $206,965.53 revenue with **-$17,725.48 net loss** (-8.56% margin).
     - `Bookcases`: $114,880.00 revenue with **-$3,472.56 net loss** (-3.02% margin).
     - `Supplies`: $46,673.54 revenue with **-$1,189.10 net loss** (-2.55% margin).
4. **Regional Margin Compression:**
   - The Central region produces $501,239.89 in gross revenue but yields only a 7.92% margin, compared to West (14.94%) and East (13.48%). This stems from excessive discounting policies in Illinois and Texas.
