import pandas as pd
import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Logistics & Inventory Discrepancy Tool",
    page_icon="📦",
    layout="wide"
)

# Header Utama
st.title("📦 Logistics & Inventory Discrepancy Tracker")
st.markdown("Automated reconciliation tool for warehouse inventory checks and discrepancy analysis.")

st.sidebar.header("Data Control Center")
st.sidebar.info("Upload system & physical stock files to run reconciliation.")

# Contoh Data Input (Demo Mode)
use_demo = st.sidebar.checkbox("Use Demo Data", value=True)

if use_demo:
    system_data = pd.DataFrame({
        'Part_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
        'Part_Name': ['Brake Pad', 'Oil Filter', 'Hydraulic Hose', 'Air Filter', 'Spark Plug'],
        'System_Qty': [150, 80, 45, 200, 90]
    })
    
    physical_data = pd.DataFrame({
        'Part_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
        'Part_Name': ['Brake Pad', 'Oil Filter', 'Hydraulic Hose', 'Air Filter', 'Spark Plug'],
        'Physical_Qty': [148, 80, 42, 200, 85]
    })
else:
    sys_file = st.sidebar.file_uploader("Upload System Stock (CSV/Excel)", type=['csv', 'xlsx'])
    phys_file = st.sidebar.file_uploader("Upload Physical Stock (CSV/Excel)", type=['csv', 'xlsx'])
    
    if sys_file and phys_file:
        system_data = pd.read_csv(sys_file) if sys_file.name.endswith('.csv') else pd.read_excel(sys_file)
        physical_data = pd.read_csv(phys_file) if phys_file.name.endswith('.csv') else pd.read_excel(phys_file)
    else:
        st.warning("Please upload both System and Physical stock files or select 'Use Demo Data'.")
        st.stop()

# Proses Rekonsiliasi Data
merged_df = pd.merge(system_data, physical_data[['Part_ID', 'Physical_Qty']], on='Part_ID', how='inner')
merged_df['Discrepancy'] = merged_df['System_Qty'] - merged_df['Physical_Qty']

# Ringkasan KPI Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("Total Items Checked", len(merged_df))
col2.metric("Total Discrepancies", len(merged_df[merged_df['Discrepancy'] != 0]))
col3.metric("Total Variance (Units)", int(merged_df['Discrepancy'].abs().sum()))

st.markdown("---")

# Tabel Detail Discrepancy
st.subheader("🔍 Discrepancy Detail Report")
discrepancies = merged_df[merged_df['Discrepancy'] != 0]

if not discrepancies.empty:
    st.dataframe(discrepancies.style.highlight_max(axis=0, color='#ffcccc'), use_container_width=True)
    
    # Download Report Button
    csv_data = discrepancies.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Discrepancy Report (CSV)",
        data=csv_data,
        file_name="discrepancy_report.csv",
        mime="text/csv"
    )
else:
    st.success("🎉 No inventory discrepancies found! System and Physical stocks are perfectly aligned.")