"""
=============================================================================
E-Commerce Sales Intelligence Dashboard
College Data Analytics Microproject: E-Commerce Sales Data Analysis (EDA)
=============================================================================
Technology Stack:
- Python 3
- Streamlit (Interactive Web Application)
- Pandas & NumPy (Data Processing & Statistical Computations)
- Plotly Express & Plotly Graph Objects (Interactive Data Visualizations)
- Custom CSS (Apple-level Minimalism & Enterprise Design System)
=============================================================================
"""

import os
import io
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & METADATA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Sales Intelligence | EDA Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS STYLING (APPLE-INSPIRED MINIMALISM & ENTERPRISE POLISH)
# -----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
/* Base typography and clean layout */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #0F172A;
}

/* Background refinement */
.stApp {
    background-color: #F8FAFC;
}

/* Header Container */
.header-container {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 24px 32px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px -1px rgba(0, 0, 0, 0.04);
}

.header-title {
    font-size: 2.1rem;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.025em;
    margin: 0;
    line-height: 1.2;
}

.header-subtitle {
    font-size: 0.95rem;
    font-weight: 500;
    color: #2563EB;
    margin-top: 6px;
    margin-bottom: 4px;
    letter-spacing: -0.01em;
}

.header-tagline {
    font-size: 0.85rem;
    color: #64748B;
    margin: 0;
}

/* Section Header Dividers */
.section-header {
    margin-top: 32px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #E2E8F0;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.02em;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.section-desc {
    font-size: 0.85rem;
    color: #64748B;
    margin: 4px 0 0 0;
}

/* KPI Card Cards */
.kpi-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    height: 100%;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.06), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
}

.kpi-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #64748B;
    margin-bottom: 6px;
}

.kpi-value {
    font-size: 1.75rem;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 4px;
}

.kpi-subtext {
    font-size: 0.75rem;
    color: #94A3B8;
    margin: 0;
}

/* Insight Cards */
.insight-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 12px;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.03);
    border-left: 4px solid #2563EB;
}

.insight-card.teal {
    border-left-color: #0D9488;
}

.insight-card.navy {
    border-left-color: #1E3A8A;
}

.insight-card.purple {
    border-left-color: #6366F1;
}

.insight-title {
    font-size: 0.825rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #475569;
    margin-bottom: 4px;
}

.insight-content {
    font-size: 0.95rem;
    color: #0F172A;
    font-weight: 500;
    line-height: 1.45;
    margin: 0;
}

.insight-detail {
    font-size: 0.8rem;
    color: #64748B;
    margin-top: 4px;
    margin-bottom: 0;
}

/* Chart Container Cards */
.chart-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
}

.chart-header {
    margin-bottom: 14px;
}

.chart-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: -0.01em;
    margin: 0;
}

.chart-desc {
    font-size: 0.8rem;
    color: #64748B;
    margin: 2px 0 0 0;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}

/* Tag / Badge Pills */
.pill {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    background-color: #EFF6FF;
    color: #1D4ED8;
    margin-right: 6px;
    margin-bottom: 6px;
}

.pill-teal {
    background-color: #F0FDFA;
    color: #0F766E;
}

.pill-gray {
    background-color: #F1F5F9;
    color: #475569;
}

/* Hide default streamlit decorations */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. DATA LOADING, VALIDATION & PREPROCESSING PIPELINE
# -----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_and_preprocess_dataset():
    """
    Loads dataset safely from project directory using relative paths.
    Checks clean_final_data(1).csv first, then clean_final_data.csv.
    Performs datetime parsing, type safety checks, and cleans 24 non-positive records.
    """
    candidates = [
        "clean_final_data(1).csv",
        "clean_final_data.csv",
        os.path.join(os.path.dirname(__file__), "clean_final_data(1).csv"),
        os.path.join(os.path.dirname(__file__), "clean_final_data.csv"),
    ]

    filepath = None
    for path in candidates:
        if os.path.exists(path):
            filepath = path
            break

    if filepath is None:
        return None, None, "Dataset file clean_final_data(1).csv / clean_final_data.csv not found in project directory."

    try:
        raw_df = pd.read_csv(filepath)
    except Exception as e:
        return None, None, f"Failed to read CSV file: {str(e)}"

    # Required column schema check
    expected_cols = [
        'OrderID', 'CustomerID', 'OrderDate', 'ProductID', 'Quantity',
        'Discount', 'PaymentMethod', 'Status', 'Age', 'City', 'SignupDate',
        'CustomerSegment', 'ProductName', 'Category', 'UnitPrice', 'Sales', 'OrderValue'
    ]
    missing = [c for c in expected_cols if c not in raw_df.columns]
    if missing:
        return None, None, f"Dataset schema error: Missing expected columns: {missing}"

    # Date parsing
    raw_df['OrderDate'] = pd.to_datetime(raw_df['OrderDate'], errors='coerce')
    raw_df['SignupDate'] = pd.to_datetime(raw_df['SignupDate'], errors='coerce')

    # Date temporal helpers
    raw_df['Year'] = raw_df['OrderDate'].dt.year
    raw_df['Month'] = raw_df['OrderDate'].dt.month
    raw_df['MonthName'] = raw_df['OrderDate'].dt.strftime('%B')
    raw_df['YearMonth'] = raw_df['OrderDate'].dt.to_period('M').dt.to_timestamp()

    # Preprocessing: remove 24 non-positive records (Quantity <= 0 or Sales <= 0)
    # This precisely transitions dataset from 49,222 rows to 49,198 rows.
    clean_mask = (raw_df['Quantity'] > 0) & (raw_df['Sales'] > 0)
    clean_df = raw_df[clean_mask].copy()

    return raw_df, clean_df, None


# Load datasets
raw_dataset, cleaned_dataset, load_error = load_and_preprocess_dataset()

if load_error:
    st.error(f"🚨 **Dataset Loading Error**: {load_error}")
    st.info("Please ensure that `clean_final_data(1).csv` or `clean_final_data.csv` is located in the project root directory.")
    st.stop()


# -----------------------------------------------------------------------------
# 4. SIDEBAR CONTROLS & INTERACTIVE FILTERS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Filter Controls")
    st.caption("Apply multidimensional filters to update all KPI cards and charts dynamically.")

    # Reset Filters Button
    if st.button("🔄 Reset All Filters", use_container_width=True, help="Reset all interactive filters to their default state"):
        for key in list(st.session_state.keys()):
            if key.startswith("filter_"):
                del st.session_state[key]
        st.rerun()

    st.markdown("---")

    # Dataset Mode Selector
    st.markdown("**🧹 Data Preprocessing Mode**")
    use_cleaned = st.checkbox(
        "Cleaned Dataset (49,198 rows)",
        value=True,
        key="filter_use_cleaned",
        help="When checked, filters out 24 invalid records with Quantity ≤ 0 or Sales ≤ 0 as documented in the EDA methodology."
    )
    base_df = cleaned_dataset if use_cleaned else raw_dataset

    st.markdown("---")
    st.markdown("**💱 Currency Symbol Display**")
    currency_symbol = st.selectbox(
        "Currency Format",
        options=["$", "₹", "€", "£", "None (Units)"],
        index=0,
        key="filter_currency",
        help="Custom currency formatting. Default is '$'. Can be set to raw units or regional symbols without assuming currency."
    )
    curr_prefix = "" if currency_symbol == "None (Units)" else f"{currency_symbol} "

    st.markdown("---")
    st.markdown("**📅 Temporal Filters**")

    # Date range filter
    min_date = base_df['OrderDate'].min().date()
    max_date = base_df['OrderDate'].max().date()

    selected_date_range = st.date_input(
        "Order Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="filter_date_range"
    )

    # Year filter
    available_years = sorted(base_df['Year'].dropna().unique().astype(int).tolist())
    selected_years = st.multiselect(
        "Year",
        options=available_years,
        default=[],
        placeholder="All Years",
        key="filter_years"
    )

    # Month filter
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    available_months = [m for m in month_order if m in base_df['MonthName'].unique()]
    selected_months = st.multiselect(
        "Month",
        options=available_months,
        default=[],
        placeholder="All Months",
        key="filter_months"
    )

    st.markdown("---")
    st.markdown("**🛍️ Product & Category Filters**")

    # Category filter
    all_categories = sorted(base_df['Category'].dropna().unique().tolist())
    selected_categories = st.multiselect(
        "Product Category",
        options=all_categories,
        default=[],
        placeholder="All Categories",
        key="filter_categories"
    )

    # Product Name filter (cascaded by selected categories if any)
    if selected_categories:
        available_products = sorted(base_df[base_df['Category'].isin(selected_categories)]['ProductName'].dropna().unique().tolist())
    else:
        available_products = sorted(base_df['ProductName'].dropna().unique().tolist())

    selected_products = st.multiselect(
        "Product Name",
        options=available_products,
        default=[],
        placeholder="All Products",
        key="filter_products"
    )

    st.markdown("---")
    st.markdown("**👥 Customer & Operational Filters**")

    # Customer Segment filter
    all_segments = sorted(base_df['CustomerSegment'].dropna().unique().tolist())
    selected_segments = st.multiselect(
        "Customer Segment",
        options=all_segments,
        default=[],
        placeholder="All Segments",
        key="filter_segments"
    )

    # Payment Method filter
    all_payments = sorted(base_df['PaymentMethod'].dropna().unique().tolist())
    selected_payments = st.multiselect(
        "Payment Method",
        options=all_payments,
        default=[],
        placeholder="All Payment Methods",
        key="filter_payments"
    )

    # Order Status filter
    all_statuses = sorted(base_df['Status'].dropna().unique().tolist())
    selected_statuses = st.multiselect(
        "Order Status",
        options=all_statuses,
        default=[],
        placeholder="All Statuses",
        key="filter_statuses"
    )

    # City filter
    all_cities = sorted(base_df['City'].dropna().unique().tolist())
    selected_cities = st.multiselect(
        "Customer City",
        options=all_cities,
        default=[],
        placeholder="All Cities",
        key="filter_cities"
    )


# -----------------------------------------------------------------------------
# 5. DATA FILTERING EXECUTION
# -----------------------------------------------------------------------------
filtered_df = base_df.copy()

# Apply Date Range filter safely
if isinstance(selected_date_range, tuple) and len(selected_date_range) == 2:
    start_dt, end_dt = selected_date_range
    filtered_df = filtered_df[
        (filtered_df['OrderDate'].dt.date >= start_dt) &
        (filtered_df['OrderDate'].dt.date <= end_dt)
    ]
elif isinstance(selected_date_range, tuple) and len(selected_date_range) == 1:
    start_dt = selected_date_range[0]
    filtered_df = filtered_df[filtered_df['OrderDate'].dt.date >= start_dt]

# Apply Year filter
if selected_years:
    filtered_df = filtered_df[filtered_df['Year'].isin(selected_years)]

# Apply Month filter
if selected_months:
    filtered_df = filtered_df[filtered_df['MonthName'].isin(selected_months)]

# Apply Category filter
if selected_categories:
    filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]

# Apply Product Name filter
if selected_products:
    filtered_df = filtered_df[filtered_df['ProductName'].isin(selected_products)]

# Apply Segment filter
if selected_segments:
    filtered_df = filtered_df[filtered_df['CustomerSegment'].isin(selected_segments)]

# Apply Payment filter
if selected_payments:
    filtered_df = filtered_df[filtered_df['PaymentMethod'].isin(selected_payments)]

# Apply Status filter
if selected_statuses:
    filtered_df = filtered_df[filtered_df['Status'].isin(selected_statuses)]

# Apply City filter
if selected_cities:
    filtered_df = filtered_df[filtered_df['City'].isin(selected_cities)]


# -----------------------------------------------------------------------------
# 6. HEADER & EXECUTIVE HERO SECTION
# -----------------------------------------------------------------------------
st.markdown("""
<div class="header-container">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
        <div>
            <h1 class="header-title">E-Commerce Sales Intelligence</h1>
            <div class="header-subtitle">Sales Performance | Customer Insights | Product Analytics</div>
            <p class="header-tagline">Academic EDA Microproject & Business Performance Analysis Dashboard</p>
        </div>
        <div style="text-align: right;">
            <span class="pill">Streamlit 1.45</span>
            <span class="pill pill-teal">Plotly Interactive</span>
            <span class="pill pill-gray">49k+ Records</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 7. FILTER STATUS PILLS & SUMMARY BANNER
# -----------------------------------------------------------------------------
total_raw_rows = len(base_df)
current_rows = len(filtered_df)
pct_active = (current_rows / total_raw_rows * 100) if total_raw_rows > 0 else 0

active_filter_tags = []
if selected_categories:
    active_filter_tags.append(f"Categories: {', '.join(selected_categories)}")
if selected_products:
    active_filter_tags.append(f"Products: {len(selected_products)} selected")
if selected_segments:
    active_filter_tags.append(f"Segments: {', '.join(selected_segments)}")
if selected_payments:
    active_filter_tags.append(f"Payments: {', '.join(selected_payments)}")
if selected_statuses:
    active_filter_tags.append(f"Status: {', '.join(selected_statuses)}")
if selected_cities:
    active_filter_tags.append(f"Cities: {len(selected_cities)} selected")

col_banner_1, col_banner_2 = st.columns([3, 1])
with col_banner_1:
    tag_html = " ".join([f'<span class="pill">{tag}</span>' for tag in active_filter_tags])
    if active_filter_tags:
        st.markdown(f"**Active Filters:** {tag_html}", unsafe_allow_html=True)
    else:
        st.markdown("**Active Filters:** <span class='pill pill-gray'>Showing All Unfiltered Records</span>", unsafe_allow_html=True)
with col_banner_2:
    st.markdown(f"<div style='text-align: right; color: #64748B; font-size: 0.85rem; padding-top: 4px;'><b>{current_rows:,}</b> of <b>{total_raw_rows:,}</b> orders ({pct_active:.1f}%)</div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 8. DYNAMIC KPI CARDS (SECTION 1)
# -----------------------------------------------------------------------------
# 1. Total Sales — sum of Sales
total_sales = float(filtered_df['Sales'].sum()) if not filtered_df.empty else 0.0

# 2. Total Orders — distinct count of OrderID
total_orders = int(filtered_df['OrderID'].nunique()) if not filtered_df.empty else 0

# 3. Total Quantity Sold — sum of Quantity
total_quantity = float(filtered_df['Quantity'].sum()) if not filtered_df.empty else 0.0

# 4. Average Sales — average Sales per record
avg_sales_record = float(filtered_df['Sales'].mean()) if not filtered_df.empty else 0.0

# 5. Total Customers — distinct count of CustomerID
total_customers = int(filtered_df['CustomerID'].nunique()) if not filtered_df.empty else 0

# 6. Average Order Value (AOV) — total sales / distinct orders
# Clearly distinguished from existing OrderValue column
aov = (total_sales / total_orders) if total_orders > 0 else 0.0

kpi_cols = st.columns(6)

with kpi_cols[0]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Sales</div>
        <div class="kpi-value">{curr_prefix}{total_sales:,.0f}</div>
        <div class="kpi-subtext">Sum of revenue across orders</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Orders</div>
        <div class="kpi-value">{total_orders:,}</div>
        <div class="kpi-subtext">Distinct OrderID count</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Quantity Sold</div>
        <div class="kpi-value">{total_quantity:,.0f}</div>
        <div class="kpi-subtext">Sum of product units sold</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Average Sales</div>
        <div class="kpi-value">{curr_prefix}{avg_sales_record:,.2f}</div>
        <div class="kpi-subtext">Mean sales per line item</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[4]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Customers</div>
        <div class="kpi-value">{total_customers:,}</div>
        <div class="kpi-subtext">Distinct CustomerID count</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[5]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Order Value (AOV)</div>
        <div class="kpi-value">{curr_prefix}{aov:,.2f}</div>
        <div class="kpi-subtext">Total Sales ÷ Distinct Orders</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 9. DYNAMIC SECTION: KEY BUSINESS INSIGHTS
# -----------------------------------------------------------------------------
st.markdown("### 💡 Key Business Insights")
st.caption("Dynamically generated statistical takeaways synthesized from current filter selections.")

if filtered_df.empty:
    st.warning("⚠️ **No Data Available**: The selected combination of filters returned 0 records. Please widen your filter criteria or click 'Reset All Filters'.")
else:
    # 1. Top Category
    cat_grp = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    top_cat = cat_grp.sort_values(by='Sales', ascending=False).iloc[0]
    top_cat_name = top_cat['Category']
    top_cat_sales = top_cat['Sales']
    top_cat_pct = (top_cat_sales / total_sales * 100) if total_sales > 0 else 0

    # 2. Top Product
    prod_grp = filtered_df.groupby('ProductName').agg({'Sales': 'sum', 'Quantity': 'sum'}).reset_index()
    top_prod = prod_grp.sort_values(by='Sales', ascending=False).iloc[0]
    top_prod_name = top_prod['ProductName']
    top_prod_sales = top_prod['Sales']
    top_prod_qty = top_prod['Quantity']

    # 3. Top Payment Method
    pm_counts = filtered_df['PaymentMethod'].value_counts()
    top_pm_name = pm_counts.index[0]
    top_pm_count = pm_counts.iloc[0]
    top_pm_pct = (top_pm_count / current_rows * 100) if current_rows > 0 else 0

    # 4. Top Customer Segment
    seg_grp = filtered_df.groupby('CustomerSegment')['Sales'].sum().reset_index()
    top_seg = seg_grp.sort_values(by='Sales', ascending=False).iloc[0]
    top_seg_name = top_seg['CustomerSegment']
    top_seg_sales = top_seg['Sales']
    top_seg_pct = (top_seg_sales / total_sales * 100) if total_sales > 0 else 0

    # 5. Monthly Sales Trend (Peak & Valley)
    monthly_trend = filtered_df.groupby('YearMonth')['Sales'].sum().reset_index()
    if len(monthly_trend) > 1:
        peak_month_row = monthly_trend.sort_values(by='Sales', ascending=False).iloc[0]
        peak_month_str = peak_month_row['YearMonth'].strftime('%B %Y')
        peak_month_val = peak_month_row['Sales']
        lowest_month_row = monthly_trend.sort_values(by='Sales', ascending=True).iloc[0]
        lowest_month_str = lowest_month_row['YearMonth'].strftime('%B %Y')
        trend_summary = f"Peak revenue occurred in <b>{peak_month_str}</b> ({curr_prefix}{peak_month_val:,.0f}); lowest in <b>{lowest_month_str}</b>."
    elif len(monthly_trend) == 1:
        m_str = monthly_trend.iloc[0]['YearMonth'].strftime('%B %Y')
        trend_summary = f"Single month view for <b>{m_str}</b> ({curr_prefix}{monthly_trend.iloc[0]['Sales']:,.0f})."
    else:
        trend_summary = "Insufficient monthly time steps in current filter range."

    # 6. Most Common Order Status
    status_counts = filtered_df['Status'].value_counts()
    top_status_name = status_counts.index[0]
    top_status_pct = (status_counts.iloc[0] / current_rows * 100) if current_rows > 0 else 0
    cancelled_pct = (status_counts.get('Cancelled', 0) / current_rows * 100) if current_rows > 0 else 0
    returned_pct = (status_counts.get('Returned', 0) / current_rows * 100) if current_rows > 0 else 0

    # 7. UnitPrice vs Sales Correlation
    if filtered_df['UnitPrice'].nunique() > 1 and filtered_df['Sales'].nunique() > 1:
        corr_val = filtered_df['UnitPrice'].corr(filtered_df['Sales'])
        if np.isnan(corr_val):
            corr_interp = "Indeterminate due to constant variance."
        elif corr_val > 0.7:
            corr_interp = f"Strong positive relationship (r = {corr_val:+.2f}). Higher ticket price items are the primary driver of top-line sales volume."
        elif corr_val > 0.3:
            corr_interp = f"Moderate positive relationship (r = {corr_val:+.2f}). Sales grow moderately with unit price."
        elif corr_val > -0.3:
            corr_interp = f"Weak/negligible linear relationship (r = {corr_val:+.2f}). Unit price alone does not dictate sales volume."
        else:
            corr_interp = f"Inverse relationship (r = {corr_val:+.2f})."
    else:
        corr_interp = "Constant price or single product selected — variance insufficient for correlation computation."

    # Render insights in 4 responsive cards
    ins_col1, ins_col2 = st.columns(2)
    with ins_col1:
        st.markdown(f"""
        <div class="insight-card navy">
            <div class="insight-title">🏆 Category & Product Dominance</div>
            <p class="insight-content"><b>{top_cat_name}</b> leads all categories with <b>{curr_prefix}{top_cat_sales:,.0f}</b> ({top_cat_pct:.1f}% of filtered revenue). Top individual SKU is <b>{top_prod_name}</b> generating <b>{curr_prefix}{top_prod_sales:,.0f}</b> across {top_prod_qty:,.0f} units sold.</p>
            <p class="insight-detail">Reflects high-ticket electronics and productivity accessories driving customer order baskets.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="insight-card teal">
            <div class="insight-title">💳 Payment Channel Preferences</div>
            <p class="insight-content"><b>{top_pm_name}</b> is the dominant payment channel, capturing <b>{top_pm_pct:.1f}%</b> ({top_pm_count:,} transactions) of all checkouts. Digital methods significantly outpace physical cash transactions.</p>
            <p class="insight-detail">High payment gateway and card-to-card adoption indicates mature digital payment familiarity among buyers.</p>
        </div>
        """, unsafe_allow_html=True)

    with ins_col2:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">👥 Customer Segment & Fulfillment</div>
            <p class="insight-content">The <b>{top_seg_name}</b> customer segment drives the highest gross revenue at <b>{curr_prefix}{top_seg_sales:,.0f}</b> ({top_seg_pct:.1f}%). Fulfillment health is resilient with <b>{top_status_pct:.1f}%</b> Completed, {cancelled_pct:.1f}% Cancelled, and {returned_pct:.1f}% Returned.</p>
            <p class="insight-detail">Uniform return and cancellation rates across tiers suggest fulfillment quality is stable regardless of buyer tenure.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="insight-card purple">
            <div class="insight-title">📈 Temporal Velocity & Pricing Correlation</div>
            <p class="insight-content">{trend_summary} Pricing elasticity check: <b>{corr_interp}</b></p>
            <p class="insight-detail">Statistical note: Correlation reflects association, not causal mechanics. Order volume and discounting also modulate realized revenue.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 10. PLOTLY THEME & COLOR PALETTE UTILITY
# -----------------------------------------------------------------------------
PLOT_FONT = dict(family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", size=12, color="#0F172A")
NAVY_PALETTE = ["#1E3A8A", "#2563EB", "#0D9488", "#0284C7", "#6366F1", "#059669", "#D97706", "#475569"]

def apply_sleek_layout(fig, title="", height=400):
    """Applies Apple-level minimalism and enterprise clean aesthetics to Plotly figures."""
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>" if title else "",
            font=dict(size=14, color="#0F172A", family="Inter, sans-serif"),
            x=0.01,
            y=0.96
        ),
        margin=dict(l=40, r=20, t=50 if title else 20, b=40),
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=PLOT_FONT,
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_size=12,
            font_color="#FFFFFF",
            font_family="Inter, sans-serif"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11, color="#475569")
        )
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="#F1F5F9",
        linecolor="#CBD5E1",
        tickfont=dict(color="#475569", size=11),
        title_font=dict(color="#0F172A", size=12, weight=600)
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#F1F5F9",
        linecolor="#CBD5E1",
        tickfont=dict(color="#475569", size=11),
        title_font=dict(color="#0F172A", size=12, weight=600)
    )
    return fig


# -----------------------------------------------------------------------------
# 11. VISUALIZATIONS SECTION (RESPONSIVE CONTINUOUS LAYOUT)
# -----------------------------------------------------------------------------
if filtered_df.empty:
    st.info("No records to display. Please adjust your filters from the sidebar.")
else:
    # =========================================================================
    # ROW 1: EXISTING CHARTS (UNTOUCHED AND PRESERVED EXACTLY)
    # =========================================================================
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">📈 Sales Performance Overview</h2>
        <p class="section-desc">Macro trends across product categories and chronological sales velocity.</p>
    </div>
    """, unsafe_allow_html=True)

    col_r1_1, col_r1_2 = st.columns(2)

    # -------------------------------------------------------------------------
    # CHART 1: Sales by Product Category
    # -------------------------------------------------------------------------
    with col_r1_1:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 1: Sales by Product Category</h3>
            <p class="chart-desc">Gross sales aggregated by product category, sorted in descending order.</p>
        </div>
        """, unsafe_allow_html=True)

        cat_sales = filtered_df.groupby('Category').agg(
            TotalSales=('Sales', 'sum'),
            Orders=('OrderID', 'count'),
            TotalQty=('Quantity', 'sum')
        ).reset_index().sort_values(by='TotalSales', ascending=False)

        fig1 = px.bar(
            cat_sales,
            x='Category',
            y='TotalSales',
            text='TotalSales',
            color='TotalSales',
            color_continuous_scale=[[0, "#93C5FD"], [0.5, "#2563EB"], [1, "#1E3A8A"]],
            labels={'TotalSales': 'Total Sales', 'Category': 'Category'}
        )
        fig1.update_traces(
            texttemplate=f'{curr_prefix}%{{text:,.0f}}',
            textposition='outside',
            hovertemplate=f"<b>Category:</b> %{{x}}<br><b>Sales:</b> {curr_prefix}%{{y:,.2f}}<extra></extra>",
            marker_line_color="#E2E8F0",
            marker_line_width=1
        )
        fig1.update_coloraxes(showscale=False)
        apply_sleek_layout(fig1, height=420)
        fig1.update_yaxes(range=[0, cat_sales['TotalSales'].max() * 1.15])
        st.plotly_chart(fig1, use_container_width=True)

    # -------------------------------------------------------------------------
    # CHART 2: Monthly Sales Trend
    # -------------------------------------------------------------------------
    with col_r1_2:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 2: Monthly Sales Trend</h3>
            <p class="chart-desc">Chronological sales velocity and order volume over time.</p>
        </div>
        """, unsafe_allow_html=True)

        monthly_data = filtered_df.groupby('YearMonth').agg(
            TotalSales=('Sales', 'sum'),
            Orders=('OrderID', 'count'),
            AvgOrderVal=('Sales', 'mean')
        ).reset_index().sort_values(by='YearMonth')

        # Compute Month-over-Month change
        monthly_data['Sales_MoM'] = monthly_data['TotalSales'].pct_change() * 100

        fig2 = go.Figure()
        # Area fill under trend
        fig2.add_trace(go.Scatter(
            x=monthly_data['YearMonth'],
            y=monthly_data['TotalSales'],
            mode='lines+markers',
            name='Total Sales',
            line=dict(color='#2563EB', width=3),
            marker=dict(size=6, color='#1E3A8A', symbol='circle'),
            fill='tozeroy',
            fillcolor='rgba(37, 99, 235, 0.08)',
            customdata=np.stack((monthly_data['Orders'], monthly_data['Sales_MoM'].fillna(0)), axis=-1),
            hovertemplate=(
                "<b>Month:</b> %{x|%B %Y}<br>" +
                f"<b>Sales:</b> {curr_prefix}%{{y:,.2f}}<br>" +
                "<b>Orders:</b> %{customdata[0]:,}<br>" +
                "<b>MoM Growth:</b> %{customdata[1]:+.1f}%<extra></extra>"
            )
        ))

        apply_sleek_layout(fig2, height=420)
        fig2.update_xaxes(title="Order Date (Monthly)", dtick="M2", tickformat="%b %Y")
        fig2.update_yaxes(title="Total Sales")
        st.plotly_chart(fig2, use_container_width=True)


    # =========================================================================
    # ROW 2: TOP PRODUCTS & UNIT PRICE VS SALES
    # =========================================================================
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🛍️ Product & Pricing Analytics</h2>
        <p class="section-desc">SKU level revenue contributions and relationship between catalog price and realized sales.</p>
    </div>
    """, unsafe_allow_html=True)

    col_r2_1, col_r2_2 = st.columns(2)

    # -------------------------------------------------------------------------
    # SECTION 8: Top 10 Products (Horizontal Bar Chart)
    # -------------------------------------------------------------------------
    with col_r2_1:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 8: Top 10 Products by Total Sales</h3>
            <p class="chart-desc">Horizontal bar chart ranking ProductName by total revenue generated.</p>
        </div>
        """, unsafe_allow_html=True)

        top_products = filtered_df.groupby(['ProductName', 'Category']).agg(
            TotalSales=('Sales', 'sum'),
            TotalQty=('Quantity', 'sum'),
            AvgUnitPrice=('UnitPrice', 'mean'),
            OrderCount=('OrderID', 'count')
        ).reset_index().sort_values(by='TotalSales', ascending=False).head(10)

        # Sort ascending for horizontal bar chart display
        top_products_sorted = top_products.sort_values(by='TotalSales', ascending=True)

        fig_top = px.bar(
            top_products_sorted,
            x='TotalSales',
            y='ProductName',
            orientation='h',
            color='TotalSales',
            color_continuous_scale=[[0, "#0D9488"], [1, "#1E3A8A"]],
            labels={'TotalSales': 'Total Sales', 'ProductName': 'Product'}
        )
        fig_top.update_traces(
            texttemplate=f'{curr_prefix}%{{x:,.0f}}',
            textposition='outside',
            hovertemplate=(
                "<b>%{y}</b><br>" +
                f"<b>Total Sales:</b> {curr_prefix}%{{x:,.2f}}<br>" +
                "<b>Units Sold:</b> %{customdata[0]:,.0f}<br>" +
                f"<b>Unit Price:</b> {curr_prefix}%{{customdata[1]:.2f}}<br>" +
                "<b>Category:</b> %{customdata[2]}<extra></extra>"
            ),
            customdata=np.stack((
                top_products_sorted['TotalQty'],
                top_products_sorted['AvgUnitPrice'],
                top_products_sorted['Category']
            ), axis=-1),
            marker_line_color="#E2E8F0",
            marker_line_width=1
        )
        fig_top.update_coloraxes(showscale=False)
        apply_sleek_layout(fig_top, height=450)
        fig_top.update_xaxes(title="Total Sales", range=[0, top_products_sorted['TotalSales'].max() * 1.25])
        fig_top.update_yaxes(title="")
        st.plotly_chart(fig_top, use_container_width=True)

    # -------------------------------------------------------------------------
    # SECTION 3: Unit Price vs Sales (Interactive Scatter Plot)
    # -------------------------------------------------------------------------
    with col_r2_2:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 3: Unit Price vs Sales</h3>
            <p class="chart-desc">Interactive scatter plot showing transaction sales as a function of catalog unit price.</p>
        </div>
        """, unsafe_allow_html=True)

        # Sample for smooth browser rendering if points > 3,500
        if len(filtered_df) > 3500:
            scatter_df = filtered_df.sample(3500, random_state=42)
            scatter_note = f"<i>Displaying representative sample of 3,500 points from {len(filtered_df):,} active records.</i>"
        else:
            scatter_df = filtered_df
            scatter_note = f"<i>Displaying all {len(filtered_df):,} records in active filter.</i>"

        fig_scatter = px.scatter(
            scatter_df,
            x='UnitPrice',
            y='Sales',
            color='Category',
            color_discrete_sequence=NAVY_PALETTE,
            hover_data={
                'UnitPrice': f':.2f',
                'Sales': f':.2f',
                'Quantity': True,
                'Discount': ':.1f',
                'ProductName': True,
                'Category': True
            },
            labels={'UnitPrice': 'Unit Price', 'Sales': 'Sales'}
        )
        fig_scatter.update_traces(
            marker=dict(size=7, opacity=0.7, line=dict(width=0.5, color='#FFFFFF')),
            hovertemplate=(
                "<b>%{customdata[4]}</b> (%{customdata[5]})<br>" +
                f"<b>Unit Price:</b> {curr_prefix}%{{x:.2f}}<br>" +
                f"<b>Sales:</b> {curr_prefix}%{{y:.2f}}<br>" +
                "<b>Quantity:</b> %{customdata[2]}<br>" +
                "<b>Discount:</b> %{customdata[3]}%<extra></extra>"
            )
        )
        apply_sleek_layout(fig_scatter, height=450)
        fig_scatter.update_xaxes(title="Unit Price")
        fig_scatter.update_yaxes(title="Sales")
        st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown(f"<div style='font-size: 0.75rem; color: #64748B;'>{scatter_note}</div>", unsafe_allow_html=True)


    # =========================================================================
    # ROW 3: SALES DISTRIBUTION & PAYMENT METHOD DISTRIBUTION
    # =========================================================================
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">📊 Sales Distribution & Payment Preferences</h2>
        <p class="section-desc">Statistical transaction value spread and checkout payment channel adoption.</p>
    </div>
    """, unsafe_allow_html=True)

    col_r3_1, col_r3_2 = st.columns(2)

    # -------------------------------------------------------------------------
    # SECTION 2: Sales Distribution (Histogram)
    # -------------------------------------------------------------------------
    with col_r3_1:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 2: Sales Distribution (Histogram)</h3>
            <p class="chart-desc">Interactive frequency distribution of line-item sales with mean and median markers.</p>
        </div>
        """, unsafe_allow_html=True)

        mean_sales_val = filtered_df['Sales'].mean()
        median_sales_val = filtered_df['Sales'].median()

        fig_hist = px.histogram(
            filtered_df,
            x='Sales',
            nbins=40,
            color_discrete_sequence=['#2563EB'],
            labels={'Sales': 'Sales Value', 'count': 'Frequency (Orders)'}
        )
        fig_hist.update_traces(
            marker_line_color="#1E3A8A",
            marker_line_width=0.8,
            hovertemplate=f"<b>Sales Range:</b> {curr_prefix}%{{x}}<br><b>Count:</b> %{{y:,}}<extra></extra>"
        )

        # Add vertical reference lines for Mean and Median
        fig_hist.add_vline(
            x=mean_sales_val,
            line_dash="dash",
            line_color="#DC2626",
            line_width=2,
            annotation_text=f"Mean: {curr_prefix}{mean_sales_val:.1f}",
            annotation_position="top right"
        )
        fig_hist.add_vline(
            x=median_sales_val,
            line_dash="dot",
            line_color="#0D9488",
            line_width=2,
            annotation_text=f"Median: {curr_prefix}{median_sales_val:.1f}",
            annotation_position="top left"
        )

        apply_sleek_layout(fig_hist, height=420)
        fig_hist.update_xaxes(title="Sales Amount")
        fig_hist.update_yaxes(title="Frequency (Orders)")
        st.plotly_chart(fig_hist, use_container_width=True)

    # -------------------------------------------------------------------------
    # SECTION 4: Payment Method Distribution (Donut Chart)
    # -------------------------------------------------------------------------
    with col_r3_2:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 4: Payment Method Distribution</h3>
            <p class="chart-desc">Donut chart showing transaction counts and percentages by checkout method (Not Sales Volume).</p>
        </div>
        """, unsafe_allow_html=True)

        pm_dist = filtered_df.groupby('PaymentMethod').agg(
            Transactions=('OrderID', 'count'),
            TotalSales=('Sales', 'sum')
        ).reset_index().sort_values(by='Transactions', ascending=False)

        fig_donut = px.pie(
            pm_dist,
            values='Transactions',
            names='PaymentMethod',
            hole=0.58,
            color='PaymentMethod',
            color_discrete_sequence=["#1E3A8A", "#2563EB", "#0D9488", "#F59E0B"]
        )
        fig_donut.update_traces(
            textposition='outside',
            textinfo='percent+label',
            hovertemplate=(
                "<b>Method:</b> %{label}<br>" +
                "<b>Transactions:</b> %{value:,} (%{percent:.1%})<br>" +
                f"<b>Associated Sales:</b> {curr_prefix}%{{customdata[0]:,.2f}}<extra></extra>"
            ),
            customdata=np.stack((pm_dist['TotalSales'],), axis=-1),
            marker=dict(line=dict(color='#FFFFFF', width=2))
        )
        apply_sleek_layout(fig_donut, height=420)
        fig_donut.add_annotation(
            text=f"<b>{current_rows:,}</b><br><span style='font-size:10px; color:#64748B;'>Transactions</span>",
            x=0.5, y=0.5,
            font=dict(size=14, color="#0F172A", family="Inter, sans-serif"),
            showarrow=False
        )
        st.plotly_chart(fig_donut, use_container_width=True)


    # =========================================================================
    # ROW 4: CUSTOMER SEGMENT ANALYSIS & ORDER STATUS ANALYSIS
    # =========================================================================
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">👥 Customer Segmentation & Fulfillment Dynamics</h2>
        <p class="section-desc">Comparing purchasing performance across customer tiers and operational order fulfillment states.</p>
    </div>
    """, unsafe_allow_html=True)

    col_r4_1, col_r4_2 = st.columns(2)

    # -------------------------------------------------------------------------
    # SECTION 5: Customer Segment Analysis (Total Sales & Average Sales Comparison)
    # -------------------------------------------------------------------------
    with col_r4_1:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 5: Customer Segment Analysis</h3>
            <p class="chart-desc">Comparison of Total Sales (revenue) and Average Sales per order for New, Regular, and VIP customers.</p>
        </div>
        """, unsafe_allow_html=True)

        seg_analysis = filtered_df.groupby('CustomerSegment').agg(
            TotalSales=('Sales', 'sum'),
            AvgSales=('Sales', 'mean'),
            DistinctCustomers=('CustomerID', 'nunique'),
            TotalOrders=('OrderID', 'nunique')
        ).reset_index()

        # Dual-axis comparative chart: Total Sales on primary Y, Average Sales on secondary Y
        fig_seg = go.Figure()
        fig_seg.add_trace(go.Bar(
            x=seg_analysis['CustomerSegment'],
            y=seg_analysis['TotalSales'],
            name='Total Sales',
            marker_color='#2563EB',
            text=seg_analysis['TotalSales'].apply(lambda v: f"{curr_prefix}{v:,.0f}"),
            textposition='outside',
            hovertemplate=f"<b>Segment:</b> %{{x}}<br><b>Total Sales:</b> {curr_prefix}%{{y:,.2f}}<extra></extra>"
        ))
        fig_seg.add_trace(go.Scatter(
            x=seg_analysis['CustomerSegment'],
            y=seg_analysis['AvgSales'],
            name='Average Sales per Order',
            yaxis='y2',
            mode='lines+markers',
            marker=dict(size=9, color='#0D9488', symbol='diamond'),
            line=dict(color='#0D9488', width=3),
            hovertemplate=f"<b>Segment:</b> %{{x}}<br><b>Average Sales:</b> {curr_prefix}%{{y:,.2f}}<extra></extra>"
        ))

        apply_sleek_layout(fig_seg, height=420)
        fig_seg.update_layout(
            yaxis=dict(title="Total Sales", showgrid=True, gridcolor="#F1F5F9"),
            yaxis2=dict(
                title=f"Average Sales ({curr_prefix.strip()})",
                overlaying='y',
                side='right',
                showgrid=False,
                title_font=dict(color="#0D9488", size=12, weight=600),
                tickfont=dict(color="#0D9488", size=11)
            ),
            legend=dict(x=0.5, y=1.12, orientation='h', xanchor='center')
        )
        st.plotly_chart(fig_seg, use_container_width=True)

    # -------------------------------------------------------------------------
    # SECTION 6: Order Status Analysis
    # -------------------------------------------------------------------------
    with col_r4_2:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 6: Order Status Analysis</h3>
            <p class="chart-desc">Counts and percentages of Completed, Cancelled, and Returned orders, with CustomerSegment comparison.</p>
        </div>
        """, unsafe_allow_html=True)

        # Cross-tab Segment vs Status
        status_seg = pd.crosstab(
            filtered_df['CustomerSegment'],
            filtered_df['Status'],
            normalize='index'
        ) * 100
        status_seg = status_seg.reset_index()

        # Ensure all statuses exist even in filtered slices
        for st_col in ['Completed', 'Cancelled', 'Returned']:
            if st_col not in status_seg.columns:
                status_seg[st_col] = 0.0

        fig_status = go.Figure()
        fig_status.add_trace(go.Bar(
            x=status_seg['CustomerSegment'],
            y=status_seg['Completed'],
            name='Completed',
            marker_color='#059669',
            text=status_seg['Completed'].apply(lambda v: f"{v:.1f}%"),
            textposition='inside',
            hovertemplate="<b>Segment:</b> %{x}<br><b>Completed:</b> %{y:.1f}%<extra></extra>"
        ))
        fig_status.add_trace(go.Bar(
            x=status_seg['CustomerSegment'],
            y=status_seg['Cancelled'],
            name='Cancelled',
            marker_color='#DC2626',
            text=status_seg['Cancelled'].apply(lambda v: f"{v:.1f}%"),
            textposition='inside',
            hovertemplate="<b>Segment:</b> %{x}<br><b>Cancelled:</b> %{y:.1f}%<extra></extra>"
        ))
        fig_status.add_trace(go.Bar(
            x=status_seg['CustomerSegment'],
            y=status_seg['Returned'],
            name='Returned',
            marker_color='#D97706',
            text=status_seg['Returned'].apply(lambda v: f"{v:.1f}%"),
            textposition='inside',
            hovertemplate="<b>Segment:</b> %{x}<br><b>Returned:</b> %{y:.1f}%<extra></extra>"
        ))

        fig_status.update_layout(barmode='stack')
        apply_sleek_layout(fig_status, height=420)
        fig_status.update_yaxes(title="Percentage of Segment Orders (%)", range=[0, 100])
        fig_status.update_layout(legend=dict(x=0.5, y=1.12, orientation='h', xanchor='center'))
        st.plotly_chart(fig_status, use_container_width=True)


    # =========================================================================
    # ROW 5: CORRELATION HEATMAP & STATISTICAL SUMMARY
    # =========================================================================
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🔬 Statistical EDA & Correlation Matrix</h2>
        <p class="section-desc">Multivariate Pearson correlation coefficients and parametric summary statistics across numeric dimensions.</p>
    </div>
    """, unsafe_allow_html=True)

    col_r5_1, col_r5_2 = st.columns(2)

    # -------------------------------------------------------------------------
    # SECTION 7: Correlation Heatmap
    # -------------------------------------------------------------------------
    with col_r5_1:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Chart 7: Pearson Correlation Heatmap</h3>
            <p class="chart-desc">Matrix analyzing Quantity, Discount, Age, UnitPrice, Sales, and OrderValue.</p>
        </div>
        """, unsafe_allow_html=True)

        corr_cols = ['Quantity', 'Discount', 'Age', 'UnitPrice', 'Sales', 'OrderValue']
        corr_df = filtered_df[corr_cols].corr()

        fig_corr = go.Figure(data=go.Heatmap(
            z=corr_df.values,
            x=corr_cols,
            y=corr_cols,
            colorscale='RdBu_r',
            zmin=-1.0,
            zmax=1.0,
            text=np.round(corr_df.values, 2),
            texttemplate="%{text:.2f}",
            textfont=dict(size=12, color="#0F172A", family="Inter, sans-serif"),
            hoverongaps=False,
            hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: <b>%{z:.3f}</b><extra></extra>",
            colorbar=dict(
                title="Correlation (r)",
                tickvals=[-1, -0.5, 0, 0.5, 1],
                len=0.9
            )
        ))

        apply_sleek_layout(fig_corr, height=430)
        st.plotly_chart(fig_corr, use_container_width=True)
        st.caption("<i>Note: High correlation reflects numerical co-movement (e.g. UnitPrice & Sales), not causal mechanism.</i>")

    with col_r5_2:
        st.markdown("""
        <div class="chart-header">
            <h3 class="chart-title">Parametric Statistical Summary (Active Subset)</h3>
            <p class="chart-desc">Central tendency, dispersion, and percentile distribution for numerical attributes.</p>
        </div>
        """, unsafe_allow_html=True)

        stat_summary = filtered_df[corr_cols].describe().T[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
        stat_summary.columns = ['Count', 'Mean', 'Std Dev', 'Min', '25th Pct', 'Median', '75th Pct', 'Max']
        st.dataframe(
            stat_summary.style.format({
                'Count': '{:,.0f}',
                'Mean': '{:,.2f}',
                'Std Dev': '{:,.2f}',
                'Min': '{:,.2f}',
                '25th Pct': '{:,.2f}',
                'Median': '{:,.2f}',
                '75th Pct': '{:,.2f}',
                'Max': '{:,.2f}'
            }),
            use_container_width=True,
            height=370
        )


# =============================================================================
# 12. AUXILIARY DATA EXPLORER & PROJECT DOCUMENTATION EXPANDERS
# =============================================================================
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

with st.expander("📋 Filtered Dataset Explorer & CSV Audit Export", expanded=False):
    st.markdown("""
    <div class="chart-header">
        <h3 class="chart-title">Tabular Data Explorer</h3>
        <p class="chart-desc">Search, inspect individual rows, and export the active slice of tabular e-commerce data.</p>
    </div>
    """, unsafe_allow_html=True)

    col_exp_1, col_exp_2 = st.columns([3, 1])
    with col_exp_1:
        search_term = st.text_input("🔍 Quick Search by Customer, City, or Product Name", "")
    with col_exp_2:
        max_rows_display = st.selectbox("Display Limit", [50, 100, 250, 500, 1000], index=1)

    table_display_df = filtered_df.copy()
    if search_term:
        search_mask = (
            table_display_df['ProductName'].astype(str).str.contains(search_term, case=False, na=False) |
            table_display_df['City'].astype(str).str.contains(search_term, case=False, na=False) |
            table_display_df['Category'].astype(str).str.contains(search_term, case=False, na=False) |
            table_display_df['CustomerID'].astype(str).str.contains(search_term, case=False, na=False)
        )
        table_display_df = table_display_df[search_mask]

    display_cols = [
        'OrderID', 'CustomerID', 'OrderDate', 'ProductName', 'Category',
        'Quantity', 'UnitPrice', 'Discount', 'Sales', 'PaymentMethod',
        'Status', 'CustomerSegment', 'City', 'Age'
    ]
    formatted_table = table_display_df[display_cols].head(max_rows_display).copy()
    formatted_table['OrderDate'] = formatted_table['OrderDate'].dt.strftime('%Y-%m-%d')

    st.dataframe(formatted_table, use_container_width=True, height=350)
    st.caption(f"Showing up to {max_rows_display} of {len(table_display_df):,} matching rows.")

    # CSV Download Button
    csv_buffer = io.StringIO()
    table_display_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_buffer.getvalue(),
        file_name="filtered_ecommerce_sales_data.csv",
        mime="text/csv",
        help="Download the filtered records for external review or submission."
    )

with st.expander("ℹ️ Academic Project Documentation & Methodology (About)", expanded=False):
    doc_col1, doc_col2 = st.columns(2)

    with doc_col1:
        st.markdown("""
        #### 1. Project Background & Objectives
        - **Project Title:** E-Commerce Sales Data Analysis (EDA)
        - **Course:** College Data Analytics Microproject
        - **Primary Objectives:**
          1. **Sales Performance:** Evaluate revenue velocity across categories, individual products, and chronological months.
          2. **Customer Segmentation:** Contrast purchasing patterns between New, Regular, and VIP customer cohorts.
          3. **Fulfillment Tracking:** Monitor distribution of Completed, Cancelled, and Returned transactions.
          4. **Payment Preferences:** Map transaction frequency across Gateways, Card-to-Card, Wallets, and Cash.
          5. **Statistical Relationships:** Investigate Pearson correlation and price-demand sensitivity.

        #### 2. Dataset Dimensions & Preprocessing Pipeline
        - **Original Dataset:** 49,222 records across 17 attributes.
        - **Cleaning Criterion:** In the raw dataset, 24 records exhibited invalid business parameters:
          - 19 records with negative Quantity (< 0) and negative Sales (< 0).
          - 5 records with zero Quantity (= 0) and zero Sales (= 0).
        - **Cleaned Dataset:** 49,198 valid records (49,222 − 24).
        - **Sales vs OrderValue Verification:** An exhaustive numerical comparison reveals that the `Sales` column and `OrderValue` column contain identical values across all rows.
        - **Average Order Value (AOV) Formulation:** Calculated as dynamic aggregate revenue divided by distinct order count ($\\text{Total Sales} \\div \\text{Distinct Orders}$).
        """)

    with doc_col2:
        st.markdown("""
        #### 3. Statistical Analysis Methods
        - **Univariate Analysis:** Evaluated frequency distributions and parametric metrics (mean, standard deviation) vs non-parametric metrics (median, interquartile range) to assess skewness.
        - **Bivariate Analysis:** Cross-tabulated categorical dimensions (Customer Segment vs Order Status) and plotted continuous relationships (Unit Price vs Realized Sales).
        - **Multivariate Analysis:** Constructed a full 6x6 Pearson correlation matrix spanning `Quantity`, `Discount`, `Age`, `UnitPrice`, `Sales`, and `OrderValue`.
        - **Time-Series Aggregation:** Resampled order timestamps to monthly buckets to analyze month-over-month sales velocity.

        #### 4. Technology Stack & Limitations
        - **Core Language:** Python 3.13, Streamlit 1.45, Pandas 2.2, NumPy 2.1, Plotly 5.24.
        - **Descriptive EDA Scope:** Purely exploratory and descriptive data analytics. No predictive modeling or machine learning claimed.
        - **Correlation ≠ Causation:** Strong correlation between `UnitPrice` and `Sales` ($r \\approx +0.78$) demonstrates revenue weighting, not causal consumer behavior.
        """)

st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.85rem; padding: 24px 0 12px 0;">
    College Data Analytics Microproject | E-Commerce Sales Data Analysis (EDA) | Local Environment Deployment
</div>
""", unsafe_allow_html=True)
