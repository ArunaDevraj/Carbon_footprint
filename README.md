<<<<<<< HEAD
# Carbon_footprint
=======
## Carbon Footprint

To automatically calculate carbon emissions

# 🌱 Carbon Footprint Tracker for ERPNext

A custom ERPNext module to track and log your organisation’s carbon emissions from various sources like travel, electricity, manufacturing, and more.

---

## 🛠️ Step-by-Step Implementation

### ✅ Step 1: Create Custom App

```bash
bench new-app carbon_footprint
bench --site your-site-name install-app carbon_footprint


✅ Step 2: Create Emission Factor Doctype

cd carbon_footprint
frappe new-doctype "Emission Factor" --create-desk

Fields:

    activity_type (Data)

    source_type (Data)

    emission_factor (Float, kg CO₂/unit)

    unit (Data)


✅ Step 3: Create Carbon Footprint Log Doctype

frappe new-doctype "Carbon Footprint Log" --create-desk
✅ Step 4: Add Python Logic to Calculate Emissions

📄 carbon_footprint/api/carbon.py
✅ Step 5: Hook Into Expense Claim
✅ Step 6: Create Dashboards & Reports

    Go to Dashboard > New

    Create a chart:

        Doctype: Carbon Footprint Log

        Chart Type: Line / Bar

        Y-axis: carbon_emission

        Filter by month or date
