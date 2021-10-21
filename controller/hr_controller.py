from model.hr import hr
from view import terminal as view
import datetime
from datetime import datetime


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
    user_id = view.get_input("Please enter user ID")
    
    if hr.is_contained(user_id):
        user_data = view.get_inputs(["Give Name:\t", "Date of birth:\t", "Department:\t", "Clearance:\t"]) 

        user_data.insert(0,user_id)
        hr.update(user_data)
        view.print_message(f"Record with user ID {user_id} has been update.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def delete_employee():
    user_id = view.get_input("Please enter user ID")

    if hr.remove(user_id):
        view.print_message(f"Record with user ID {user_id} has been removed.\n")
    else:
        view.print_error_message(f"User ID {user_id} not found!!!\n")


def get_oldest_and_youngest():
    data = hr.read()

    for _ in range(len(data) - 1):

        for j in range(len(data) - 1):

            if data[j][2] > data[j + 1][2]:
                data[j], data[j + 1] = data[j + 1], data[j]

    oldest_and_youngest = (data[0][1],data[-1][1])

    view.print_general_results(oldest_and_youngest, 'Oldest and youngest employees are:')


def get_average_age():
    user_age = []

    data = hr.read()
    
    current_year = datetime.today().year
    for entry in data:
        user_age.append(current_year - int(entry[2][0:4]))

    avg_age = sum(user_age) / len(user_age)

    view.print_general_results(avg_age, 'Average age of employees is:')


def next_birthdays():
    # Return the names of employees who have birthdays within two weeks from the input date.
    employees_with_nearest_birthdays = []

    data = hr.read()

    current_date = datetime.today().date()
    current_month = current_date.month
    for entry in data:
        user_birthday = datetime.strptime(entry[2], '%Y-%m-%d').date()
        user_month = user_birthday.month

        if current_month > user_month:
            check_date = current_date.replace(year = user_birthday.year - 1)
        else:
            check_date = current_date.replace(year = user_birthday.year)

        date_difference = user_birthday - check_date
        if date_difference.days > 0 and date_difference.days < 14:
            employees_with_nearest_birthdays.append(entry[1])
    
    view.print_general_results(employees_with_nearest_birthdays, 'Employees who have birthdays within two weeks are:')


def count_employees_with_clearance():
    employees_with_clearance = 0

    data = hr.read()
    
    for entry in data:
        if int(entry[4]) > 1:
            employees_with_clearance += 1

    view.print_general_results(employees_with_clearance, 'Number of employees who have at least the input clearance level is:')


def count_employees_per_department():
    employees_in_departments = {}

    data = hr.read()
    
    for entry in data:

        if entry[3] in employees_in_departments.keys():
            employees_in_departments[entry[3]] += 1
        else:
            employees_in_departments[entry[3]] = 1

    view.print_general_results(employees_in_departments, 'Number of employees in departments are:')


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
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)