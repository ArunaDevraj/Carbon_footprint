# Copyright (c) 2025, Aruna D and contributors








import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    conditions = {}

    if filters.get("from_date") and filters.get("to_date"):
        conditions["creation"] = ["between", [filters["from_date"], filters["to_date"]]]

    # Get raw data
    data = frappe.get_all(
        "Carbon Footprint Log",
        filters=conditions,
        fields=["name", "reference_type", "reference_name", "creation"]
    )

    frappe.msgprint(f"📦 Debug: Raw data = {frappe.as_json(data)}")

    # Return expected structure
    columns = [
        {"fieldname": "name", "label": "ID", "fieldtype": "Link", "options": "Carbon Footprint Log"},
        {"fieldname": "reference_type", "label": "Reference Type", "fieldtype": "Link", "options": "DocType"},
        {"fieldname": "reference_name", "label": "Reference Name", "fieldtype": "Dynamic Link", "options": "reference_type"},
        {"fieldname": "creation", "label": "Created On", "fieldtype": "Datetime"},
    ]

    return columns, data
