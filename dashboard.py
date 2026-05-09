import pandas as pd
import streamlit as st
import plotly.express as px

from modules.database import InventoryDB
from modules.kpi_calculator import KPICalculator


# PAGE SETTINGS
st.set_page_config(
    page_title="Inventory Dashboard",
    layout="wide"
)

st.title("📦 Inventory Operations Dashboard")


# DATABASE
db = InventoryDB()

records = db.get_inventory_data()


# COLUMN NAMES
columns = [
    "product_id",
    "name",
    "category",
    "unit_cost",
    "reorder_point",
    "min_stock",
    "quantity_on_hand",
    "quantity_reserved",
    "quantity_available"
]


# DATAFRAME
df = pd.DataFrame(records, columns=columns)


# KPI CALCULATOR
kpi = KPICalculator()


# INVENTORY VALUE
df["inventory_value"] = (
    df["quantity_on_hand"]
    * df["unit_cost"]
)


# STOCK STATUS
def stock_status(row):

    if row["quantity_on_hand"] < row["min_stock"]:
        return "CRITICAL"

    elif row["quantity_on_hand"] < row["reorder_point"]:
        return "LOW"

    else:
        return "OK"


df["stock_status"] = df.apply(
    stock_status,
    axis=1
)


# SUMMARY METRICS
total_inventory_value = df["inventory_value"].sum()

total_products = len(df)

critical_products = len(
    df[df["stock_status"] == "CRITICAL"]
)


# KPI CARDS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Inventory Value",
    f"₹{total_inventory_value:,.0f}"
)

col2.metric(
    "Total Products",
    total_products
)

col3.metric(
    "Critical Products",
    critical_products
)


# INVENTORY TABLE
st.subheader("Inventory Table")

st.dataframe(df)


# CHART
st.subheader("Inventory Value by Product")

fig = px.bar(
    df,
    x="name",
    y="inventory_value"
)

st.plotly_chart(fig)


# ALERTS
st.subheader("Low Stock Alerts")

alerts_df = df[
    df["stock_status"] != "OK"
]

if len(alerts_df) > 0:

    st.dataframe(
        alerts_df[
            [
                "product_id",
                "name",
                "quantity_on_hand",
                "stock_status"
            ]
        ]
    )

else:
    st.success("No alerts found!")


db.close()