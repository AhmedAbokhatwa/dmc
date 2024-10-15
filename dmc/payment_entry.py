import frappe

from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry


class CustomPaymentEntry(PaymentEntry):
    def on_update_after_submit(self):

        proforma = self.custom_proforma_invoice_details

        for row in proforma:
            prof = frappe.get_doc("Proforma Invoice", row.proforma_invoice)
            prof.ignore_validate_update_after_submit = True
            prof.db.set('collection_amount', row.to_be_paid)


