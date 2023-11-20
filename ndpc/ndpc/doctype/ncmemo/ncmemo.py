# Copyright (c) 2023, sam | iyke and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class NCMemo(Document):
    def on_before_save(self):
        # Ensure that the receiver field is set based on the assigned_to field
        if self.assigned_to:
            # Fetch the user corresponding to the assigned_to field
            user = frappe.db.get_value('Employee', self.assigned_to, 'user')
            
            # Set the receiver field to the fetched user
            self.receiver = user
        else:
            # Handle the case when assigned_to is not set
            frappe.throw('Assigned To field is required.')
