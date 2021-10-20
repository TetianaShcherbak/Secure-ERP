from model.hr import hr
from view import terminal as view



def list_employees():
    database = hr.read()

    if database != []:
        view.print_table(database, hr.HEADERS)
    else:
        view.print_error_message("Database is empty!!!\n")


def add_employee():
    user_data = view.get_inputs(["Give Name:\t", "Date of birth:\t", "Department:\t", "Clearance:\t"])

    if hr.add(user_data):
        view.print_message(f"New data has been added.\n")
    else:
        view.print_error_message(f"User's data has not been created!!!\n")


def update_employee():
    user_id = view.get_input("Please enter user ID:\t")
    
    if hr.is_contained(user_id):
        user_data = view.get_inputs(["Give Name:\t", "Date of birth:\t", "Department:\t", "Clearance:\t"]) 

        user_data.insert(0,user_id)
        hr.update(user_data)
        view.print_message(f"Record with user ID {user_id} has been update.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def delete_employee():
    user_id = view.get_input("Please enter user ID:\t")

    if hr.remove(user_id):
        view.print_message(f"Record with user ID {user_id} has been removed.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def get_oldest_and_youngest():
    view.print_error_message("Not implemented yet.")


def get_average_age():
    view.print_error_message("Not implemented yet.")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    view.print_error_message("Not implemented yet.")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


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