"""
Misleading vs. Correct Visualization Module for Group 4 DVT Lab Assignment.
Demonstrates Edward Tufte's Lie Factor and ethical visualization design.
"""

import streamlit as st
from components.charts import render_misleading_comparison


def render(df, col_map):
    st.header("⚖️ Visualization Ethics: Misleading vs. Correct Visualizations")
    st.caption("Demonstrating Graphical Integrity, Truncated Axis Distortion, and Tufte's Lie Factor.")

    st.markdown(
        """
        In data visualization, **graphical integrity** requires that visual representations of data 
        do not distort the underlying numbers. When an axis is artificially manipulated, readers perceive 
        exaggerated differences that lead to flawed management decisions.
        """
    )

    # Interactive side-by-side rendering
    render_misleading_comparison(df, col_map)

    st.divider()

    # Analytical Deep-Dive on Visualization Ethics
    st.subheader("📐 The Mathematics of Distortion: Tufte's Lie Factor")
    
    st.latex(r"\text{Lie Factor} = \frac{\text{Size of effect shown in graphic}}{\text{Size of effect in data}}")

    st.markdown(
        r"""
        - **In the Honest Graphic (Zero-Baseline):** 
          - Actual data: West is $\$725,458$ and South is $\$391,722$.
          - Actual data percentage increase: $\frac{725,458 - 391,722}{391,722} = \mathbf{85.2\%}$ (Ratio $= 1.85$).
          - Graphical bar length ratio on a zero baseline: $\frac{725,458}{391,722} = \mathbf{1.85}$.
          - **Result:** $\text{Lie Factor} = \frac{85.2\%}{85.2\%} = \mathbf{1.00}$ (Perfect Fidelity).

        - **In the Deliberately Misleading Graphic (Baseline truncated at $\$350,000$):**
          - Visible bar height for South: $391,722 - 350,000 = 41,722\text{ units}$.
          - Visible bar height for West: $725,458 - 350,000 = 375,458\text{ units}$.
          - Graphical percentage increase shown: $\frac{375,458 - 41,722}{41,722} = \mathbf{800.5\%}$ (Visual ratio $= 9.00$).
          - **Lie Factor Calculation:**
            $$\text{Lie Factor} = \frac{800.5\%}{85.2\%} \approx \mathbf{9.40} \quad \left(\text{or ratio comparison: } \frac{9.00}{1.85} \approx \mathbf{4.86}\right)$$
          - In either formulation, the Lie Factor dramatically exceeds Edward Tufte's acceptable fidelity corridor of $[0.95, 1.05]$.

        ### 🚨 Potential Real-World Business Impact:
        1. **Misallocated Capital:** Executives viewing the truncated chart would falsely conclude that South territory sales are negligible and terminate regional sales channels, even though South generated nearly $\$400,000$ in healthy revenue.
        2. **False Panic & Volatility:** Creates artificial distress during executive reporting reviews.
        3. **Loss of Stakeholder Trust:** Violates visual ethics guidelines established by Edward Tufte and Alberto Cairo.
        """
    )
