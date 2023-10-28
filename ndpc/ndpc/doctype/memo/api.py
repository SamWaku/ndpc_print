import frappe



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



