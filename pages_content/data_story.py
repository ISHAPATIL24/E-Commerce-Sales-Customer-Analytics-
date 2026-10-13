"""
Data Story, Findings & Recommendations Module for Group 4 DVT Lab Assignment.
"""

import streamlit as st


def render(df, col_map):
    st.header("🕵️ Data Detective Story: Findings & Recommendations")
    st.caption("Synthesizing empirical evidence from 9,994 retail sales records into actionable business strategy.")

    tab_story, tab_findings, tab_recs = st.tabs([
        "🎙️ Two-Minute Data Story Script",
        "📊 5 Evidence-Based Findings",
        "🎯 3 Actionable Recommendations",
    ])

    with tab_story:
        st.subheader("Oral Presentation Delivery Script (Timed 120 Seconds)")
        st.caption("Structured narrative: Hook [0–20s] → Tension [20–50s] → Evidence [50–90s] → Resolution [90–120s].")

        st.markdown(
            """
            > **[00:00 – 00:20] The Hook: An Illusion of Prosperity**  
            > *"Good morning, evaluators and colleagues. Welcome to Group 4's Data Detective investigation.  
            > At first glance, our e-commerce enterprise looks like a thriving success story: **$2.3 million in gross revenue**, 
            > over **5,000 completed orders**, and an apparently healthy **12.5% overall profit margin**. Executive leadership was celebrating growth.  
            > But as data detectives, we looked beneath these headline averages — and uncovered an invisible profit leak draining hundreds of thousands of dollars from the business."*
            > 
            > ---
            > **[00:20 – 00:50] The Tension: The Furniture Black Hole & Regional Anomaly**  
            > *"When we decompose performance by merchandise hierarchy, the illusion shatters.  
            > While **Technology** and **Office Supplies** deliver robust **17% profit margins**, our **Furniture category** 
            > generated nearly three-quarters of a million dollars in sales, but yielded a meager **2.5% margin**.  
            > Investigating further, two specific sub-categories — **Tables and Bookcases** — actually operated at catastrophic net losses, destroying **over $21,000 in bottom-line profits**.  
            > Simultaneously, our **Central Region** produced half a million dollars in turnover, yet delivered only half the profit margin of the West and East. Why was high sales volume destroying value?"*
            > 
            > ---
            > **[00:50 – 01:30] The Evidence: The Discount Cliff Exposed**  
            > *"Here is our smoking gun: the **Discount Cliff**.  
            > When our commercial team offers zero discount, transactions generate a stellar **29.5% profit margin**. When discounts are kept under 20%, margins remain healthy at **12%**.  
            > But the moment discounts cross **20%**, profit collapses off a cliff into deep negative territory — averaging **-20% margin**, and plunging to **-119% margin** on clearance markdowns over 50%.  
            > Over 1,300 order lines were transacted at these destructive discount levels, predominantly in Central states like Texas and Illinois. Sales reps were using extreme discounts to inflate top-line volume, completely blind to the fact that every sale was losing money."*
            > 
            > ---
            > **[01:30 – 02:00] The Resolution: Actionable Strategy & Value Recovery**  
            > *"Our data detective diagnosis points to three immediate, high-impact interventions:  
            > 1. **Establish a hard 20% discount ceiling:** Prohibit unapproved discounts above 20%, instantly stopping $135,000 in operational losses and lifting margin on remaining sales to roughly 22%.  
            > 2. **Restructure Tables & Bookcases:** Reprice the line by 10% and transition to drop-shipping to eliminate warehousing overhead.  
            > 3. **Shift Sales Incentives:** Align regional commissions with Net Contribution Margin instead of raw top-line volume.  
            > In conclusion, true visualization doesn't just display data — it unmasks hidden truths and protects enterprise value. Thank you!"*
            """
        )

    with tab_findings:
        st.subheader("Five Empirical Findings from Verified Dataset")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                #### 1. The Severe Discount Cliff Past 20%
                - At **0% discount**, margin is **+29.5%** ($320k profit across 4,798 orders).
                - At **0.1–20% discount**, margin is **+11.9%** ($100k profit across 3,803 orders).
                - At **21–50% discount**, margin collapses to **-19.7%** (loss of -$58.8k across 537 orders).
                - At **>50% discount**, margin plummets to **-119.2%** (loss of -$76.5k across 856 orders).
                - *Conclusion:* Discounts over 20% destroy enterprise value without driving net gains.

                #### 2. Chronic Loss Leaders in Furniture
                - While Technology yields **17.4% margin** and Office Supplies yields **17.0% margin**, Furniture generates only **2.5% margin**.
                - **Tables** lost **-$17,725.48** (-8.56% margin on $206k sales).
                - **Bookcases** lost **-$3,472.56** (-3.02% margin on $114k sales).
                - Tables & Bookcases destroyed **$21,198.04** in net capital.
                """
            )
        with col2:
            st.markdown(
                """
                #### 3. Central Region Margin Compression
                - West Region: $725k sales with **$108.4k profit (14.9% margin)**.
                - East Region: $678k sales with **$91.5k profit (13.5% margin)**.
                - Central Region: $501k sales with only **$39.7k profit (7.9% margin)**.
                - Dragged down by Texas (-$25.7k profit) and Illinois (-$12.6k profit), where the average discount is ~37–39% (other Central states: ~0%).

                #### 4. Q4 Seasonality Surge (Stable Margin)
                - November and December alone bring 29.5% of annual revenue; with September, ~43%.
                - Q4 margin (12.6%) is about level with Q2 (12.4%) and above Q3 (11.8%), so the seasonal surge is not a margin squeeze.

                #### 5. Pareto Concentration of Accounts
                - Top 20% of customers (158 accounts) account for **48.0% of gross revenue**.
                - Corporate and Home Office orders are larger (AOV $466 and $473) than Consumer orders ($449).
                """
            )

    with tab_recs:
        st.subheader("Three Actionable Managerial Recommendations")

        st.success(
            """
            ### 🎯 Recommendation 1: Implement a Hard 20% Ceiling on Promotional Discounts
            - **Action:** Enforce strict system-level governance requiring VP approval for discounts exceeding 20%. Immediately eliminate the >50% clearance tier.
            - **Estimated Business Impact (Projection):** Recovers up to **$135,376.05** in operational losses (modeled by eliminating historical >20% discount transactions), lifting margin on the remaining sales from **12.5% to ~21.8%**.
            """
        )

        st.warning(
            """
            ### 🎯 Recommendation 2: Restructure the Tables & Bookcases Product Lines
            - **Action:** Increase base prices on Tables by 10–12%, bundle them with high-margin Technology peripherals, and shift fulfillment to on-demand drop-shipping to eliminate warehousing holding costs.
            - **Estimated Business Impact (Projection):** Eliminates **$21,198.04** in chronic merchandise drag (modeled by bringing Tables and Bookcases to breakeven).
            """
        )

        st.info(
            """
            ### 🎯 Recommendation 3: Realign Central Regional Sales Incentives
            - **Action:** Restructure commercial compensation in Texas and Illinois, tying sales commissions strictly to **Net Contribution Profit** rather than gross revenue turnover.
            - **Estimated Business Impact (Projection):** Closing Central Region's margin gap to match East Region delivers an estimated **+$27,869.00** in incremental annual operating profit.
            """
        )

