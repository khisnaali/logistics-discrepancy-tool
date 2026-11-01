# 📦 Enterprise Logistics & Inventory Discrepancy Reconciliation Tool

An automated web-based inventory reconciliation dashboard built with **Python (Pandas)** and **Streamlit**, designed to eliminate manual spreadsheet errors, accelerate stock auditing, and provide deep financial insights into inventory discrepancies.

🌐 **Live Web App Demo:** [Access Streamlit App Here](https://logistics-discrepancy-tool.streamlit.app/)

---

## 🚀 Business Value & Key Features (Why This Tool Matters)

In large-scale warehouse operations (such as automotive parts distribution and heavy machinery logistics), traditional manual spreadsheet reconciliations are slow, error-prone, and lack real-time financial tracking. This application solves those enterprise challenges through:

1. **Automated System vs. Physical Stock Matching**
   * Instantly merges and reconciles ERP system records (`System_Qty`) with physical warehouse audit counts (`Physical_Qty`) via unique part identifiers (`Part_ID`).
2. **Financial Impact & Valuation Analysis**
   * Goes beyond simple quantity differences by calculating financial loss (`Discrepancy_Value = Discrepancy × Unit_Cost`), allowing management to prioritize high-value asset auditing.
3. **Automated Status Classification**
   * Automatically flags and categorizes items into operational states (`Match`, `Shortage / Missing`, or `Surplus / Overstock`) to streamline warehouse investigations.
4. **Interactive Enterprise Reporting & Exporting**
   * Features dynamic KPI metrics, zone-based filtering, and instant clean CSV/Excel report generation for management reviews.

---

## 🛠️ Technology Stack
* **Core Logic & Data Processing:** Python, Pandas
* **User Interface & Web Framework:** Streamlit
* **Deployment & Cloud Hosting:** Streamlit Community Cloud
* **Version Control:** Git & GitHub

---

## 📁 Dataset Template Structure

If you wish to test the application with your own data, ensure your files follow this schema:

### 1. System Stock File (`system_stock.csv`)
| Part_ID | Part_Name | Zone | System_Qty | Unit_Cost (IDR) |
| :--- | :--- | :---: | :---: | :---: |
| P001 | Brake Pad | Zone-A | 150 | 500,000 |
| P002 | Oil Filter | Zone-B | 80 | 150,000 |

### 2. Physical Stock File (`physical_stock.csv`)
| Part_ID | Physical_Qty |
| :--- | :---: |
| P001 | 148 |
| P002 | 80 |

---

## ⚙️ Local Installation & Running Guide

If you want to run this application locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/khisnaali/logistics-discrepancy-tool.git](https://github.com/khisnaali/logistics-discrepancy-tool.git)
   cd logistics-discrepancy-tool