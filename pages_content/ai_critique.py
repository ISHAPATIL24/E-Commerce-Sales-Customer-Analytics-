"""
AI Visualization Critique Module for Group 4 DVT Lab Assignment.
Documents prompt, AI output, team decision, and visualization theory justification.
"""

import streamlit as st


def render():
    st.header("🤖 AI Visualization Critique & Evaluation")
    st.caption("Critiquing generative AI visualization recommendations using foundational cognitive principles.")

    st.markdown(
        """
        During the exploratory phase of our project, our team prompted an advanced AI assistant 
        to propose an all-in-one executive chart design. Below is the unedited prompt, the AI's response, 
        Group 4's official evaluation decision, and our justification grounded in academic visualization theory.
        """
    )

    # Section 1: The Prompt
    with st.expander("📝 1. The Prompt Submitted to AI", expanded=True):
        st.code(
            'We are designing an executive e-commerce dashboard for the Superstore dataset. '
            'We want to visualize Sales and Profit simultaneously across our 17 sub-categories, '
            '4 geographical regions, and 4 operational years. Recommend the best single visualization '
            'design to show all of this on one screen, including chart type, color scheme, and aesthetic embellishments.',
            language="markdown"
        )

    # Section 2: AI Generated Output
    with st.expander("🤖 2. Actual AI Recommendation & Output", expanded=True):
        st.markdown(
            """
            > **AI Recommendation:**  
            > *"To showcase multi-dimensional hierarchy across sales, profit, sub-categories, regions, and years simultaneously, I recommend building an **Exploded 3D Dual-Axis Clustered Donut-Radar Chart** (or a 3D Multi-Layered Bubble Matrix).  
            > - Use 3D perspective to project regions as concentric depth layers.  
            > - Use 17 exploded donut wedges for each sub-category.  
            > - Apply dual Y-axes with vibrant rainbow gradient coloring to represent Sales (outer ring thickness) and Profit (wedge color spectrum from bright red to neon green).  
            > - Add bevel effects and drop shadows for a modern aesthetic look."*
            """
        )

    # Section 3: Group Decision
    st.subheader("3. Group 4 Official Evaluation Decision")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.error("### ⚠️ DECISION: PARTIALLY ACCEPTED")
        st.caption("Accepted analytical objective; Completely rejected visual implementation.")
    with col2:
        st.markdown(
            """
            The AI correctly diagnosed the core analytical need — examining profitability across product hierarchies 
            and geographical segments. However, the AI's suggested chart type (**3D Exploded Donut-Radar with rainbow colors**) 
            violates core cognitive ergonomics and graphical integrity rules. We **REJECTED** the chart type and **REDESIGNED** 
            it into clean Small Multiples Diverging Bars and Interactive Linked Cross-Filters.
            """
        )

    st.divider()

    # Section 4: Detailed Theoretical Justification
    st.subheader("4. Team Justification (Visualization Theory Grounding)")

    col_j1, col_j2 = st.columns(2)

    with col_j1:
        st.markdown("#### 🚫 Rejected Elements & Theoretical Flaws")
        st.markdown(
            """
            1. **3D Perspective & Occlusion (Edward Tufte):**  
               3D projections create artificial distortion where foreground wedges appear disproportionately larger than background wedges, introducing an uncontrolled Lie Factor.
            2. **Dual-Axis Overlay (Stephen Few):**  
               Overlaying Sales ($0–$800k) and Profit (-$17k to +$145k) on the same concentric ring causes false line/slice intersections that mislead executive readers.
            3. **Rainbow Color Map (Alberto Cairo & Color Theory):**  
               Rainbow palettes lack perceptual linearity, introduce false visual boundaries, and are inaccessible to color-blind individuals (Deuteranopia/Protanopia).
            4. **Cognitive Overload:**  
               Attempting to cram 17 categories $\\times$ 4 regions $\\times$ 4 years $\\times$ 2 metrics ($>500$ data points) into a single radial chart exceeds human working memory capacity.
            """
        )

    with col_j2:
        st.markdown("#### ✅ Group 4 Remediation & Redesign")
        st.markdown(
            """
            1. **Orthogonal Coordinates (Linear Cartesian Bars):**  
               Replaced radial wedges with horizontal bar charts sharing a truthful zero baseline, enabling effortless length comparison.
            2. **Small Multiples & Tabs:**  
               Separated dimensions into distinct, focused analytical views (Tabs Q1 through Q5) to preserve visual clarity.
            3. **Perceptually Uniform Color Palette:**  
               Utilized a semantic diverging color scale (Emerald Green for positive margin, Crimson Red for negative margin).
            4. **Interactive Details-on-Demand (Ben Shneiderman):**  
               Implemented dynamic sidebar multiselects and hover tooltips rather than static visual clutter, fulfilling the Information Seeking Mantra.
            """
        )
