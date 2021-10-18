from model.crm import crm
from view import terminal as view


def list_customers():
    view.print_error_message("Not implemented yet.")


def add_customer():
    view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    user_id = view.get_input("Please provide valid user id: ")
    if crm.handle_remove(user_id):
        view.print_error_message(f'User id {user_id} removed.')
    else:
        view.print_error_message(f'User id {user_id} not found, no records removed.')


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
        raise KeyError()


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
        except KeyError:
            view.print_error_message("There is no such option!")
