import frappe

def get_emission_factor(activity_type, source_type):
    factor = frappe.get_value("Emission Factor",
        {"activity_type": activity_type, "source_type": source_type}, "emission_factor")
    return factor or 0



def create_carbon_log(reference_type, reference_name, emission_source, quantity, activity_type, source_type):
    print("🚀 create_carbon_log called")
    emission_factor = frappe.get_value("Emission Factor",
        {"activity_type": activity_type, "source_type": source_type}, "emission_factor")
    
    print("✅ Emission Factor:", emission_factor)

    if not emission_factor:
        print("❌ Emission Factor not found.")
        return

    carbon_emission = emission_factor * quantity
    print("✅ Calculated Carbon Emission:", carbon_emission)

    try:
        doc = frappe.get_doc({
            "doctype": "Carbon Footprint Log",
            "date": frappe.utils.nowdate(),
            "reference_type": reference_type,
            "reference_name": reference_name,
            "emission_source": emission_source,
            "emission_factor": emission_factor,
            "quantity": quantity,
            "carbon_emission": carbon_emission
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        print("🎉 Carbon Footprint Log Created:", doc.name)
    except Exception as e:
        print("❌ Failed to insert Carbon Footprint Log")
        import traceback
        print(traceback.format_exc())







def handle_expense_claim(doc, method):
    frappe.msgprint(f"Checking expenses in Expense Claim {doc.name}")
    
    for row in doc.expenses:
        frappe.msgprint(f"Expense Type: {row.expense_type}, Mode: {row.custom_travel_mode}, KM: {row.custom_kilometers}")

        if "travel" in (row.expense_type or "").lower():
            if row.custom_travel_mode and row.custom_kilometers:
                frappe.msgprint("Creating carbon log...")
                create_carbon_log(
                    reference_type="Expense Claim",
                    reference_name=doc.name,
                    emission_source="Travel",
                    quantity=row.custom_kilometers,
                    activity_type="Travel",
                    source_type=row.custom_travel_mode
                )
