import frappe
from frappe import as_json
import json



@frappe.whitelist()
def user_role(email):
     # Get the current user
    user = frappe.session.user

    # Fetch the user's roles
    # user_roles = frappe.get_roles(user)
    
    user_roles = frappe.db.sql(f"""SELECT role_profile_name FROM `tabUser` WHERE email='{email}';""")

    # Convert the list of roles to a string
    user_roles_string = str(user_roles)
    user_roles_string_converted = user_roles_string[3:-5]

    # Log the user's roles
    # frappe.msgprint(f"User Roles for {user}: {user_roles_string}")
    return user_roles_string_converted

    
    # # Get the current user
    # user = frappe.session.user

    # # Fetch the user's roles
    # user_roles = frappe.get_roles(user)

    # # Log the user's roles
    # # frappe.msgprint(f"User Roles for {user}: {user_roles}")
    # return user_roles

    # # return frappe.db.sql(f"""SELECT role_profile_name FROM `tabUser` WHERE email='{email}';""")

@frappe.whitelist()
def activity_log(docname):
#     user_actions = frappe.db.sql(f"""SELECT * FROM `tabVersion` WHERE docname='{docname}';""", as_dict=True)
#     return as_json(user_actions)
    # user_actions =frappe.db.sql(f"""SELECT * FROM `tabVersion` WHERE docname='NCM0011';""")

    # user_actions_string = str(user_actions)
    # user_actions_string_converted = user_actions_string[5:-5]
    # return user_actions_string
    user_actions = frappe.db.sql(f"""SELECT * FROM `tabVersion` WHERE docname='{docname}';""", as_dict=True)
    # doc = frappe.get_doc({
    #     'doctype': 'Version',
    #     'docname': 'NCM0011'
    # })

    # doc = frappe.get_last_doc("Version", filters={"docname": docname})


    # # Convert datetime objects to string representation
    # for action in user_actions:
    #     action['creation'] = str(action['creation'])
    #     action['modified'] = str(action['modified'])
    
    # # Convert the entire list to JSON
    # return as_json(user_actions)

    # Convert datetime objects to string representation
    for action in user_actions:
        action['creation'] = str(action['creation'])
        action['modified'] = str(action['modified'])
    
    # # Serialize the list of dictionaries to a properly formatted JSON string
    response = json.dumps(user_actions, default=str)
    
    return response

#  try:
#         doc = frappe.get_doc({
#             'doctype': 'Branch',
#             'branch': data['branch']
#         })

#         doc.save()
#         return doc
    
#     except Exception as error:
#         frappe.local.response['success'] = False
#         frappe.local.response['error'] = error

@frappe.whitelist()
def update_document_access(docname, selected_role):
    try:
            # Fetch the document based on the docname
        doc = frappe.get_doc("NCMemo", docname)

        # Clear existing permissions and set new permissions
      
        existing_permissions = doc.get("permissions")
        print("Existing Permissions:", existing_permissions)
        doc.add_permission("read", role=selected_role)
        doc.add_permission("write", role=selected_role)

        doc.append("permissions", {
            "role": selected_role,
            "read": 1,
            "write": 1
        })

        # Save the document
        doc.save()

        if selected_role == 'HOD':
            frappe.get_doc('User', frappe.session.user).add_roles('Secretary')
        else:
            frappe.get_doc('User', frappe.session.user).remove_roles('Secretary')

        return "Access updated successfully"

    except Exception as error:
        frappe.local.response['success'] = False
        frappe.local.response['error'] = str(error)

@frappe.whitelist()
def get_roles():
    # Get the user's roles
    user_roles = frappe.get_roles()

    # Check if 'HOD' is in the user's roles
    is_hod = 'HOD' in user_roles

    return 'HOD' if is_hod else None
