# Evidence-Based Findings & Actionable Recommendations

**Course:** Data Visualization Techniques (DVT) Lab  
**Project:** Data Detective Challenge  
**Team:** Group 4 (E-Commerce Sales & Customer Analytics)  
**Dataset:** Sample Superstore Dataset (9,994 verified transaction records)  

---

## Part 1: Five Evidence-Based Analytical Findings

### Finding 1: The Severe Discount Cliff Past 20%
- **Empirical Evidence:**
  - When discount is **0%**, average profit margin is **+29.51%** ($320,987.60 profit across 4,798 orders).
  - When discount is between **0.1% and 20%**, profit margin drops to **+11.91%** ($100,785.47 profit across 3,803 orders).
  - When discount reaches **21% to 50%**, profit margin collapses to **-19.70%** (a net loss of -$58,817.00 across 537 orders).
  - When discount exceeds **50%**, profit margin reaches **-119.20%** (destroying -$76,559.05 on only $64,228.74 of sales across 856 orders).
- **Analytical Takeaway:** Discounts above 20% consistently destroy enterprise profitability without yielding proportional volume compensation.

### Finding 2: Furniture Sub-Category Value Destruction (Tables & Bookcases)
- **Empirical Evidence:**
  - While Technology yields an aggregate profit margin of **17.40%** ($145,454.95 profit on $836,154.03 sales) and Office Supplies yields **17.04%** ($122,490.80 profit), Furniture yields a margin of only **2.49%** ($18,451.27 profit on $741,999.80 sales).
  - Inside Furniture, **Tables** generated $206,965.53 in sales but incurred **-$17,725.48 in net losses** (-8.56% margin).
  - **Bookcases** generated $114,880.00 in sales but incurred **-$3,472.56 in net losses** (-3.02% margin).
  - Combined losses in Tables and Bookcases totaled **-$21,198.04**, dragging down overall company profitability.

### Finding 3: The Central Region Margin Deficit
- **Empirical Evidence:**
  - West Region generated $725,457.82 in sales with **$108,418.45 profit** (**14.94% margin**).
  - East Region generated $678,781.24 in sales with **$91,522.78 profit** (**13.48% margin**).
  - Central Region generated $501,239.89 in sales but produced only **$39,706.36 profit** (**7.92% margin**).
  - The Central region’s margin is roughly half that of the West and East regions. This divergence is driven by high discount rates in states like Texas (-$25,729.39 profit) and Illinois (-$12,607.89 profit).

### Finding 4: Strong Q4 Seasonality (Volume Surge, Stable Margin)
- **Empirical Evidence:**
  - Monthly sales peak in **September, November and December** in every year (2014–2017).
  - November and December together contribute **29.5%** of annual revenue (about 43% with September).
  - Margin is not squeezed in Q4: Q4 **12.6%**, Q2 **12.4%**, Q3 **11.8%**, Q1 **13.4%**. The seasonal surge is volume growth, so inventory and staffing should be planned for it.

### Finding 5: Customer Concentration & Key-Account Exposure
- **Empirical Evidence:**
  - Out of 793 unique customer accounts, the top **20% (158 accounts)** generate **47.96% ($1,101,757.53)** of gross sales.
  - The top 5 individual buyers (e.g., Sean Miller, Tamara Chand, Raymond Buch) each generated over $14,000 in gross purchases.
  - Corporate and Home Office orders are larger on average (AOV $466.41 and $472.67) than Consumer orders ($449.11).

---

## Part 2: Three Actionable Business Recommendations

### Recommendation 1: Implement a Hard Ceiling on Promotional Discounts
- **Strategic Action:** Establish an enterprise-wide discount authorization policy:
  - Disallow sales representatives from applying discounts above **20%** without formal regional vice-president sign-off.
  - Immediately terminate the >50% discount clearance tier, which generated -$76,559.05 in losses on minor turnover.
- **Estimated Business Impact (Modeled Projection):** Eliminating negative-margin transactions ($>20\%$ discounts) is modeled to recover up to **$135,376.05** in lost net profit, lifting the margin on the remaining sales from **12.47% to about 21.8%** (a counterfactual that assumes the removed sales are lost, not re-priced).

### Recommendation 2: Restructure the Furniture Catalog & Pricing Strategy
- **Strategic Action:**
  - **Reprice or Drop Tables:** Increase base prices on Tables by 10–12% and renegotiate supplier wholesale agreements. If margin improvement is unachievable, transition Tables to a dropship-on-demand fulfillment model to eliminate warehousing overhead.
  - Bundle loss-making sub-categories (Tables, Bookcases) with high-margin items (Technology accessories, Copiers, Office Labels) to ensure positive basket margin.
- **Estimated Business Impact (Modeled Projection):** Bringing Tables and Bookcases to breakeven (+0% margin) saves **$21,198.04** in direct bottom-line drag ($17,725.48 from Tables and $3,472.56 from Bookcases).

### Recommendation 3: Standardize Regional Discount Governance in Central Markets
- **Strategic Action:**
  - Recalibrate commercial terms in the Central Region, with priority focus on **Texas and Illinois**, where average discounts are ~37–39% (versus ~0% in other Central states).
  - Realign regional sales incentives: tie representative bonuses and commission structures to **Net Contribution Profit** rather than gross sales turnover.
- **Estimated Business Impact (Modeled Projection):** Raising Central Region margins from 7.92% to match East Region's 13.48% yields an estimated incremental **+$27,869.00** in annual bottom-line operating earnings.

