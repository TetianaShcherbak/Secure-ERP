import sys
from model.sales import sales
from view import terminal as view
import operator


def list_transactions():
    database = sales.read()
    if database != []:
        view.print_table(database, sales.HEADERS)
    else:
        view.print_error_message("Database is empty!!!\n")
    


def add_transaction():
    user_data = view.get_inputs(["Customer ID:\t", "Product:\t", "Price:\t", "Transaction date:\t"])
    if sales.add(user_data):
        view.print_message(f"New data has been added.\n")
    else:
        view.print_error_message(f"User's data has not been created!!!\n")


def update_transaction():
    user_id = view.get_input("Please enter user ID:\t")
    if sales.is_contained(user_id):
        user_data = view.get_inputs(["Customer ID:\t", "Product:\t", "Price:\t", "Transaction date:\t"]) 

        user_data.insert(0,user_id)
        sales.update(user_data)
        view.print_message(f"Record with user ID {user_id} has been update.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def delete_transaction():
    user_id = view.get_input("Please enter user ID:\t")
    if sales.remove(user_id):
        view.print_message(f"Record with user ID {user_id} has been removed.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def get_biggest_revenue_transaction():
    database = sales.read()
    
    id_price_set = {line[2]: float(line[3]) for line in database}
    # price = max(id_price_set.iteritems(), key=operator.itemgetter(1))[1]
    price = max(id_price_set.values())

    for value in id_price_set.values():
        price = max(id_price_set.values())
    for key, value in id_price_set.items():
        if value == price:
            id_of_cheapest = key
    return id_of_cheapest
    
    
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            print("")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)