"""
Project Name: Logistics & Discrepancy Tracking Automation Tool
Description: A utility script to automate inventory discrepancy checks 
             and invoice reconciliation for warehouse operations.
Author: Ali Ikhsan
"""

import pandas as pd

def check_inventory_discrepancies(system_stock_file, physical_stock_file):
    print("=== STARTING INVENTORY DISCREPANCY RECONCILIATION ===")
    
    # Simulasi data frame untuk data sistem dan fisik gudang
    # Dalam implementasi nyata, ini bisa membaca file CSV/Excel dari sistem ERP
    system_data = {
        'Part_ID': ['P001', 'P002', 'P003', 'P004'],
        'Part_Name': ['Brake Pad', 'Oil Filter', 'Hydraulic Hose', 'Air Filter'],
        'System_Qty': [150, 80, 45, 200]
    }
    
    physical_data = {
        'Part_ID': ['P001', 'P002', 'P003', 'P004'],
        'Part_Name': ['Brake Pad', 'Oil Filter', 'Hydraulic Hose', 'Air Filter'],
        'Physical_Qty': [148, 80, 42, 200]
    }
    
    df_sys = pd.DataFrame(system_data)
    df_phys = pd.DataFrame(physical_data)
    
    # Menggabungkan data untuk perbandingan
    merged_df = pd.merge(df_sys, df_phys, on=['Part_ID', 'Part_Name'])
    
    # Menghitung selisih (discrepancy)
    merged_df['Discrepancy'] = merged_df['System_Qty'] - merged_df['Physical_Qty']
    
    # Filter item yang memiliki selisih (tidak 0)
    discrepancies = merged_df[merged_df['Discrepancy'] != 0]
    
    print(f"\nTotal Parts Checked: {len(merged_df)}")
    print(f"Discrepancies Found: {len(discrepancies)}")
    
    if not discrepancies.empty:
        print("\n--- DISCREPANCY REPORT ---")
        print(discrepancies.to_string(index=False))
    else:
        print("\nInventory Integrity is 100% Aligned. No discrepancies found.")
        
    print("\n=== RECONCILIATION PROCESS COMPLETED ===")
    return discrepancies

if __name__ == "__main__":
    # Menjalankan fungsi simulasi
    check_inventory_discrepancies("system_stock.csv", "physical_stock.csv")