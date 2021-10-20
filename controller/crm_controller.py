from model.crm import crm
from view import terminal as view
from controller import main_controller


def print_data(data, headers):
    columns_sizes = []
    
    for header in headers:
        columns_sizes.append(0)
    print()

    for entry in data:
        for i, item in enumerate(entry):
            if columns_sizes[i] < len(item):
                if len(item) < len(headers[i]):
                    columns_sizes[i] = len(headers[i])
                else:
                    columns_sizes[i] = len(item)

    table_length = sum(columns_sizes) + len(headers) - 1

    table_separator = ''
    for i, header in enumerate(headers):
        table_separator = table_separator + '|'
        table_separator = table_separator + ('-' * columns_sizes[i])
    table_separator = table_separator + '|'
    
    print('/', end='')
    print('-' * table_length, end='')
    print('\\')

    for i, header in enumerate(headers):
        print(f"|{header : ^{columns_sizes[i]}}", end='')
    print('|')

    print(table_separator)

    for e, entry in enumerate(data):
        for i, item in enumerate(entry):
            print(f"|{item : ^{columns_sizes[i]}}", end='')
        print('|')
        if e + 1 < len(data):
            print(table_separator)

    print('\\', end='')
    print('-' * table_length, end='')
    print('/')

    
def list_customers():
    data = crm.get_data()
    view.print_table(data, crm.HEADERS)


def add_customer():
    customer_data = view.get_inputs(["Enter customer name: ", "Enter customer email: ", "Enter customer subscription status (1 or 0): "])
    if crm.add(customer_data):
        view.print_message(f"User's data has been created")
    else:
        view.print_error_message(f"User's data has not been created")


def update_customer():
    customer_id = view.get_input('Please enter the customer ID: ')
    if crm.check_customer(customer_id):
        customer_data = view.get_inputs(["Enter customer name: ", "Enter customer email: ", "Enter customer subscription status (1 or 0): "])
        customer_data.insert(0,customer_id)
        crm.update(customer_data)
        view.print_message('Database has been updated')
    else:
        view.print_message('Customer doesn\'t exist')


def delete_customer():
    customer_id = view.get_input("Please provide valid user id: ")
    if crm.remove(customer_id):
        view.print_error_message(f'User id {customer_id} removed.')
    else:
        view.print_error_message(f'User id {customer_id} not found, no records removed.')


def get_subscribed_emails():
    data = crm.select_subscribed_emails()
    headers = ['Subscribed emails']
    print_data(data, headers)


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
