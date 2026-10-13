# Group 4: E-Commerce Sales & Customer Analytics Dashboard
## Data Visualization Techniques (DVT) Lab — "Data Detective Challenge"

An enterprise-grade, interactive Streamlit analytics dashboard for retail sales and customer intelligence. Built with **Python, Pandas, Plotly, and Streamlit**, this project uncovers hidden business drivers, profit anomalies, and customer dynamics while strictly adhering to data visualization ethics and cognitive design principles.

---

## 👥 Group & Course Information
- **Course:** Data Visualization Techniques (DVT) Lab
- **Challenge:** Data Detective Challenge
- **Group:** Group 4
- **Assigned Domain:** E-Commerce Sales & Customer Analytics


---

## 🚀 Key Features

1. **Dual Dataset Architecture:**
   - **Verified Real-World Benchmark:** Automatically loads the authenticated US Superstore retail dataset (9,994 transaction records, 21 attributes, zero null values).
   - **Custom Upload & Synthetic Modes:** Supports dragging and dropping arbitrary CSV/Excel files with intelligent column auto-detection, as well as the original 300-row synthetic demo mode.
2. **Executive KPI Layer:** 5 real-time metrics including Gross Revenue, Net Profit, Profit Margin %, Total Orders, and Average Order Value (AOV).
3. **Analytical Deep-Dive (5 Core Questions):**
   - **Q1 (Sub-Category Profitability):** Isolates loss-making merchandise (Tables & Bookcases) using diverging horizontal bars.
   - **Q2 (Regional Asymmetry):** Grouped bars plus a US state choropleth exposing loss-making Texas, Illinois, Ohio and Pennsylvania.
   - **Q3 (The Discount Cliff):** Visualizes the non-linear collapse of transaction profits past a 20% discount ceiling.
   - **Q4 (Temporal Seasonality):** Dual-line monthly time series revealing Q4 holiday surges (with stable margins), plus a month x year heatmap.
   - **Q5 (Customer Pareto Concentration):** Lorenz curve demonstrating that top 20% of buyers generate 48% of total revenue.
4. **Visualization Ethics Lab (Misleading vs. Correct):**
   - Interactive side-by-side demonstration of truncated Y-axis distortion.
   - Quantitative evaluation of Edward Tufte's Lie Factor ($\text{Lie Factor} = 4.95$ vs. $\text{Lie Factor} = 1.00$).
5. **AI Visualization Critique:**
   - Unedited prompt and AI proposal (3D exploded radial radar chart).
   - Group 4 official evaluation badge: **`PARTIALLY ACCEPTED`** with structured justification grounded in visualization theory (Tufte, Cairo, Shneiderman).
6. **Data Detective Story & Recommendations:**
   - 5 empirical findings calculated from the live dataset.
   - 3 actionable managerial recommendations.
   - Full 2-minute oral presentation script (0:00 to 2:00) with visual cues.
7. **Automated Verification & Packaging:**
   - Pre-flight packaging script (`package_submission.py`) that audits file existence, verifies data integrity, and produces a consolidated submission ZIP without cache artifacts.

---

## 📁 Project Directory Structure

```
ecommerce-dashboard/
├── data/
│   ├── sample_superstore.csv        # Genuine benchmark dataset (9,994 rows, 21 cols)
│   └── dataset_metadata.json        # Data dictionary, source URL, citation, summary stats
├── docs/
│   ├── DATASET_DISCOVERY.md         # Full exploratory data profile & data dictionary
│   ├── ANALYTICAL_QUESTIONS.md      # 5 questions, variables, charts & justifications
│   ├── FINDINGS_AND_RECOMMENDATIONS.md # 5 evidence-based findings & 3 recommendations
│   ├── AI_CRITIQUE.md               # AI prompt, output, decision badge & critique
│   └── TWO_MINUTE_DATA_STORY.md     # Timed oral presentation script (0:00 - 2:00)
├── utils/
│   ├── __init__.py
│   ├── data_loader.py               # Robust CSV/Excel loader with default dataset fallback
│   ├── column_detector.py           # Adaptive semantic column role detector
│   ├── helpers.py                   # Safe mathematical, currency, and metric helpers
│   └── sample_data.py               # Original synthetic sample generator
├── components/
│   ├── __init__.py
│   ├── kpi.py                       # 5-metric executive KPI card headers
│   ├── filters.py                   # Interactive sidebar filters (Date, Category, Region, Segment)
│   └── charts.py                    # Plotly chart builders (Trend, Region, Pareto, Scatter, Ethics)
├── pages_content/
│   ├── __init__.py
│   ├── overview.py                  # Executive Dashboard Overview
│   ├── deep_dive.py                 # 5 Analytical Questions Deep-Dive
│   ├── misleading_vs_correct.py     # Ethics: Misleading vs. Correct Visualizations
│   ├── ai_critique.py               # AI Visualization Critique & Evaluation
│   ├── data_story.py                # 5 Findings, 3 Recommendations & 2-Minute Script
│   └── reports.py                   # Data discovery audit, quality summary & CSV export
├── app.py                           # Main Streamlit application entry point
├── package_submission.py            # Pre-submission verification & ZIP packager
├── requirements.txt                 # Dependencies: streamlit, pandas, plotly, openpyxl
└── README.md                        # Documentation and project manual
```

---

## 🛠️ Installation & Setup (macOS / Linux / Windows)

### 1. Clone or Open Project
```bash
cd "CHERRY_sir project"  # or Desktop/ecommerce-dashboard
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Dashboard
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

### 5. Create Submission ZIP
```bash
python3 package_submission.py
```

---

## 📊 Dataset Provenance & Attribution
- **Dataset:** Sample Superstore Dataset (Tableau US Retail Sales Benchmark)
- **Source:** [Superstore Data Analysis Repository](https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv)
- **Kaggle Reference:** [Superstore Dataset Final by Vivek A](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **License:** Public Domain / CC0 1.0 Universal (Open Database License compatible).
