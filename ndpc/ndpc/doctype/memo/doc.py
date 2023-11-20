# YourDocType.py
from frappe.model.document import Document

class NCMemo(Document):
    def on_before_save(self):
        # Ensure that the receiver field is set to the current user
        if not self.receiver:
            self.receiver = frappe.session.user
