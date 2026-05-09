# Automated Inventory Analytics & Alert Monitoring System

## Project Overview

This project is a real-time inventory analytics and monitoring system built using Python, Pandas, SQLite, and Streamlit.

The system reads inventory data from Excel files, stores operational records in a SQLite database, calculates inventory KPIs, visualizes stock metrics through interactive dashboards, and sends automated low-stock email alerts.

---

## Features

- Excel inventory data ingestion
- SQLite database integration
- Inventory KPI calculations
- Real-time Streamlit dashboard
- Inventory value monitoring
- Low-stock and reorder alerts
- Automated Gmail email notifications
- Inventory analytics visualizations
- Scheduled monitoring automation

---

## Technologies Used

- Python
- Pandas
- SQLite
- Streamlit
- Plotly
- OpenPyXL
- SMTP (Email Automation)
- Schedule Library

---

## KPIs Tracked

- Inventory Value
- Quantity Available
- Low Stock Detection
- Reorder Monitoring
- Stock Status Classification

---

## Dashboard Modules

### Overview Dashboard
- KPI summary cards
- Inventory analytics charts
- Stock monitoring metrics

### Alerts Monitoring
- Low-stock detection
- Operational alert tracking
- Automated email notifications

---

## Project Structure

```bash
inventory_tracker_project/
│
├── data/
├── modules/
├── dashboard.py
├── daily_tracker.py
├── load_data.py
├── init_db.py
└── requirements.txt
