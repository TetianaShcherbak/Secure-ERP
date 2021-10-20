from model.crm import crm
from view import terminal as view
#checking

def list_customers():
    database = crm.read()

    if database != []:
        view.print_table(database, crm.HEADERS)
    else:
        view.print_error_message("Database is empty!!!\n")


def add_customer():
    user_data = view.get_inputs(["Give Name:\t", "Give email:\t", "Is subscribed:\t"])

    if crm.add(user_data):
        view.print_message(f"New data has been added.\n")
    else:
        view.print_error_message(f"User's data has not been created!!!\n")


def update_customer():
    user_id = view.get_input("Please enter customer ID:\t")
    
    if crm.is_contained(user_id):
        user_data = view.get_inputs(["Give Name:\t", "Give email:\t", "Is subscribed:\t"]) 

        user_data.insert(0,user_id)
        crm.update(user_data)
        view.print_message(f"Record with customer ID {user_id} has been update.\n")
    else:
        view.print_error_message(f"Customer ID {user_id} not found!!!\n")


def delete_customer():
    user_id = view.get_input("Please enter Customer ID:\t")

    if crm.remove(user_id):
        view.print_message(f"Record with Customer ID {user_id} has been removed.\n")
    else:
        view.print_error_message(f"Customer ID {user_id} not found!!!\n")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)