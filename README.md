# 📊 E-Commerce Sales Intelligence — Exploratory Data Analysis (EDA) Dashboard

A complete, presentation-ready, interactive analytics dashboard built for a college Data Analytics microproject titled **“E-Commerce Sales Data Analysis (EDA)”**.

Built with **Python**, **Streamlit**, **Pandas**, **NumPy**, and **Plotly**, styled with an **Apple-inspired minimalist design system** (clean white/light grey surfaces, deep navy blue and teal accents, soft card elevations, and responsive typography).

---

## 🎯 Project Overview & Objectives

- **Course:** College Data Analytics Microproject
- **Project Title:** E-Commerce Sales Data Analysis (EDA)
- **Primary Objectives:**
  1. **Sales Performance:** Track gross sales across categories, individual products, and monthly chronological trends.
  2. **Customer Insights:** Analyze purchasing behavior across customer segments (`New`, `Regular`, `VIP`) and urban geographic hubs.
  3. **Payment Preferences:** Map transaction share across digital gateways, card-to-card, mobile wallets, and cash checkout methods.
  4. **Fulfillment Tracking:** Analyze order completion, cancellation, and return rates across customer tiers.
  5. **Statistical & Pricing Analysis:** Investigate price-sales sensitivity and multi-attribute Pearson correlations.

---

## 📦 Technology Stack

- **Language:** Python 3.10+ (Tested on Python 3.13 / Anaconda)
- **Web Application Framework:** [Streamlit](https://streamlit.io/) (`>= 1.35.0`)
- **Data Manipulation & Computation:** [Pandas](https://pandas.pydata.org/) (`>= 2.0.0`), [NumPy](https://numpy.org/) (`>= 1.24.0`)
- **Interactive Visualization:** [Plotly Express & Plotly Graph Objects](https://plotly.com/python/) (`>= 5.18.0`)
- **Styling & Design System:** Custom CSS embedding Apple-level minimalism, subtle drop shadows, and responsive grid layouts.

---

## 📂 Project Structure

```text
e commerce project/
├── .streamlit/
│   └── config.toml                  # Streamlit light theme and server configuration
├── clean_final_data.csv             # Primary dataset (49,222 records, 17 attributes)
├── clean_final_data(1).csv          # Compatible alias for seamless loading
├── app.py                           # Complete interactive Streamlit dashboard
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules for Python/Streamlit
└── README.md                        # Documentation and execution instructions
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have Python installed (Python 3.10 or higher, or Anaconda).

### 2. Install Required Packages
In your terminal or PowerShell, run:
```bash
pip install -r requirements.txt
```

*(Note: If you use Anaconda, packages such as `streamlit`, `pandas`, `numpy`, and `plotly` are likely already present.)*

### 3. Launch the Dashboard
Run the following command from the project root folder:
```bash
streamlit run app.py
```

If `streamlit` is not in your system PATH, use:
```bash
python -m streamlit run app.py
```
Or with Anaconda's Python:
```powershell
& "C:\Users\devam_v\anaconda3\Scripts\streamlit.exe" run app.py
```

The dashboard will open automatically in your browser at:
👉 **`http://localhost:8501`**

---

## 🧹 Dataset Specifications & Data Cleaning Methodology

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `OrderID` | Numeric (int64) | Unique identifier for each order transaction |
| `CustomerID` | Numeric (int64) | Identifier for unique customers |
| `OrderDate` | Datetime (parsed) | Transaction order timestamp (2024-01-01 to 2026-06-30) |
| `ProductID` | Numeric (int64) | Unique product SKU identifier |
| `ProductName` | Text (Categorical) | Product title (20 distinct items) |
| `Category` | Text (Categorical) | Product family (Accessories, Electronics, Gaming, etc.) |
| `Quantity` | Numeric (float64) | Units purchased per line item |
| `UnitPrice` | Numeric (float64) | Base unit price per product |
| `Discount` | Numeric (float64) | Percentage discount applied (0% – 30%) |
| `Sales` | Numeric (float64) | Realized transaction revenue: $\text{UnitPrice} \times \text{Quantity} \times (1 - \frac{\text{Discount}}{100})$ |
| `OrderValue` | Numeric (float64) | Order transaction value (mathematically identical to `Sales`) |
| `PaymentMethod` | Text (Categorical) | Checkout method (`Gateway`, `CardToCard`, `Wallet`, `Cash`) |
| `Status` | Text (Categorical) | Fulfillment state (`Completed`, `Cancelled`, `Returned`) |
| `CustomerSegment` | Text (Categorical) | Customer classification (`New`, `Regular`, `VIP`) |
| `City` | Text (Categorical) | Geographic origin of buyer (10 distinct cities) |
| `Age` | Numeric (float64) | Customer age (18 – 65) |
| `SignupDate` | Datetime (parsed) | Customer account registration timestamp |

### Preprocessing & Cleaning Rules:
1. **Invalid Record Filter (24 rows removed):**
   - **Original raw dataset:** 49,222 rows.
   - 19 records had negative `Quantity` (< 0) and negative `Sales` (< 0).
   - 5 records had zero `Quantity` (= 0) and zero `Sales` (= 0).
   - **Cleaned dataset:** Exactly **49,198 rows** after filtering these non-positive anomalous entries.
2. **Sales vs OrderValue Equivalence:**
   - Numerical audit confirms that `Sales` and `OrderValue` contain 100% identical values across all rows.
   - Each record in this dataset represents an individual order (`OrderID` count equals row count).
3. **Average Order Value (AOV):**
   - Calculated dynamically as $\frac{\sum \text{Sales}}{\text{Distinct OrderID Count}}$.
   - Distinctly separated from line-item values for aggregate analytics.

---

## 📈 Dashboard Features & Architecture

### 1. Dynamic KPI Cards
- **Total Sales:** Aggregate gross sales formatted with custom currency selector (`$`, `₹`, `€`, `£`, or Units).
- **Total Orders:** Distinct count of `OrderID`.
- **Quantity Sold:** Total product units sold across transactions.
- **Average Sales:** Mean sales per transaction line item.
- **Total Customers:** Distinct count of unique buyers (`CustomerID`).
- **Average Order Value (AOV):** Dynamic calculation of Total Sales ÷ Distinct Orders.

### 2. Multi-Dimensional Interactive Filters (Sidebar)
- **Data Preprocessing Mode:** Toggle between cleaned data (49,198 rows) and raw data (49,222 rows).
- **Currency Selector:** Formats numbers with selected currency or unit prefix.
- **Date Range Picker:** Filter by custom calendar dates.
- **Year & Month Multiselect:** Target specific fiscal periods (2024, 2025, 2026).
- **Category & Product Multiselect:** Drill down into specific product families or SKUs.
- **Customer Segment Multiselect:** Filter by `New`, `Regular`, or `VIP`.
- **Payment Method Multiselect:** Filter by `Gateway`, `CardToCard`, `Wallet`, or `Cash`.
- **Order Status Multiselect:** Filter by `Completed`, `Cancelled`, or `Returned`.
- **City Multiselect:** Filter by customer regional locations.
- **Reset All Filters:** One-click reset restoring all defaults.

### 3. Visualizations (All 9 Charts)
1. **Chart 1: Sales by Product Category** — Bar chart sorted in descending order with hover tooltips and dynamic color scaling.
2. **Chart 2: Monthly Sales Trend** — Chronological time-series line chart with area fill and Month-over-Month (MoM) growth rates.
3. **Chart 3: Sales Distribution** — Histogram with mean and median reference lines.
4. **Chart 4: Unit Price vs Sales** — Interactive scatter plot with product category coloring and discount details.
5. **Chart 5: Payment Method Distribution** — Clean donut chart showing transaction count percentages across payment gateways.
6. **Chart 6: Customer Segment Analysis** — Grouped bar chart comparing Total Sales and Distinct Customer counts.
7. **Chart 7: Order Status Analysis** — Overall status pie chart and stacked percentage breakdown across customer tiers.
8. **Chart 8: Pearson Correlation Heatmap** — 6x6 diverging matrix centered at 0 covering numerical variables.
9. **Chart 9: Top 10 Products by Total Sales** — Sorted horizontal bar chart with units sold and unit prices.

### 4. Dynamic "Key Business Insights"
- Top category and product SKU.
- Dominant payment method with transaction share.
- Highest-grossing customer segment.
- Temporal peak and valley months.
- Fulfillment health indicators (completion, cancellation, and return percentages).
- UnitPrice vs Sales Pearson correlation interpretation with academic causality disclaimer.

### 5. Tabular Data Explorer & Export
- Search table by Customer, City, or Product.
- Adjustable row limit (50 to 1,000 rows).
- **Download Filtered Data (CSV):** Export active data slice for review and verification.

---

## 🎓 Academic Integrity & Disclaimers

- **Exploratory Data Analysis (EDA) Scope:** All visualizations and metrics represent descriptive and exploratory statistics from real dataset calculations.
- **No Machine Learning Claim:** No artificial predictive models or synthetic data imputation were performed.
- **Causality Disclaimer:** High correlation between `UnitPrice` and `Sales` ($r \approx 0.78$) demonstrates revenue weighting, not causal consumer behavior.
