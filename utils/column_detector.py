"""
Intelligent column detection.

Given ANY dataframe, this module identifies which column plays which
semantic role (date, sales, profit, quantity, discount, category, sub_category,
product, customer, region, etc.) using two-pass exact & word-boundary matching,
with numeric/categorical dtype fallback when name-matching fails.

The result is a "column map" dict, e.g.:
    {"date": "Order Date", "sales": "Sales", "profit": "Profit", ...}
"""

import re
import pandas as pd

# Ordered keyword lists for prioritized matching
KEYWORDS = {
    "order_id": ["order id", "order_id", "orderid", "invoice", "transaction id", "order no"],
    "date": ["order date", "order_date", "date", "timestamp", "time"],
    "sales": ["sales", "revenue", "amount", "total sales", "total amount", "turnover"],
    "profit": ["profit", "net profit", "margin", "earning", "net income"],
    "quantity": ["quantity", "qty", "units", "unit count", "item count"],
    "discount": ["discount", "disc", "rebate", "markdown"],
    "category": ["category", "product category", "type", "department"],
    "sub_category": ["sub-category", "subcategory", "sub category", "sub_category"],
    "segment": ["segment", "customer segment", "market segment"],
    "product": ["product name", "product_name", "item name", "product", "item"],
    "customer": ["customer name", "customer_name", "client name", "customer", "client"],
    "region": ["region", "sales region", "territory", "zone", "state", "city", "country"],
}

# Roles that must be numeric if matched by name
NUMERIC_ROLES = {"sales", "profit", "quantity", "discount"}


def _match_by_name(columns, keywords, used_columns=None):
    """
    Two-pass matcher:
    1. Check for exact match (case-insensitive).
    2. Check for word-boundary match.
    """
    if used_columns is None:
        used_columns = set()

    # Pass 1: Exact match
    for kw in keywords:
        for col in columns:
            if col in used_columns:
                continue
            if str(col).lower().strip() == kw:
                return col

    # Pass 2: Word-boundary match
    for kw in keywords:
        pattern = r"\b" + re.escape(kw) + r"\b"
        for col in columns:
            if col in used_columns:
                continue
            col_lower = str(col).lower().strip()
            if re.search(pattern, col_lower):
                return col

    # Pass 3: Substring fallback (for compound words like "order_id")
    for kw in keywords:
        for col in columns:
            if col in used_columns:
                continue
            col_lower = str(col).lower().strip()
            if kw in col_lower:
                return col

    return None


def detect_columns(df: pd.DataFrame) -> dict:
    """
    Detect semantic column roles for an arbitrary dataframe.
    Returns a dict mapping role -> column name (or None if not found).
    """
    if df is None or df.empty:
        return {role: None for role in KEYWORDS}

    columns = list(df.columns)
    col_map = {}
    used_columns = set()

    for role, keywords in KEYWORDS.items():
        match = _match_by_name(columns, keywords, used_columns)

        # Validate numeric roles actually look numeric; otherwise reject
        if match is not None and role in NUMERIC_ROLES:
            if not pd.api.types.is_numeric_dtype(df[match]):
                coerced = pd.to_numeric(df[match], errors="coerce")
                if coerced.notna().sum() == 0:
                    match = None

        if match is not None and match not in used_columns:
            col_map[role] = match
            used_columns.add(match)
        else:
            col_map[role] = None

    # Fallback: if "sales" wasn't found by name, pick largest unused numeric column
    if col_map.get("sales") is None:
        numeric_cols = [c for c in get_numeric_columns(df) if c not in used_columns]
        if numeric_cols:
            col_map["sales"] = max(numeric_cols, key=lambda c: df[c].fillna(0).sum())
            used_columns.add(col_map["sales"])

    # Fallback: if "category" wasn't found, pick first sensible categorical column
    if col_map.get("category") is None:
        cat_cols = [c for c in get_categorical_columns(df) if c not in used_columns]
        for c in cat_cols:
            if 1 < df[c].nunique() <= 50:
                col_map["category"] = c
                used_columns.add(c)
                break

    return col_map


def get_numeric_columns(df: pd.DataFrame) -> list:
    """Return all numeric columns in the dataframe."""
    if df is None or df.empty:
        return []
    return list(df.select_dtypes(include="number").columns)


def get_categorical_columns(df: pd.DataFrame) -> list:
    """Return all object/category columns in the dataframe."""
    if df is None or df.empty:
        return []
    return list(df.select_dtypes(include=["object", "category"]).columns)


def get_datetime_columns(df: pd.DataFrame) -> list:
    """Return columns that are datetime or can be parsed as such."""
    if df is None or df.empty:
        return []
    candidates = []
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            candidates.append(col)
        elif "date" in str(col).lower() or "time" in str(col).lower():
            candidates.append(col)
    return candidates


def has_minimum_viable_data(col_map: dict) -> bool:
    """
    Check whether the dataset has at least one numeric metric and one
    categorical dimension - the bare minimum needed to build a dashboard.
    """
    has_metric = col_map.get("sales") is not None or col_map.get("profit") is not None
    has_dimension = col_map.get("category") is not None or col_map.get("product") is not None
    return has_metric and has_dimension
