""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
from model import crud

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def read():

    return crud.crud_read(DATAFILE)


def add(data_to_add):
    user_id = util.generate_id()

    data_to_add.insert(0,user_id)

    return crud.crud_create(DATAFILE, data_to_add, user_id)


def update(new_data_table):

    return crud.crud_update(DATAFILE, new_data_table)


def remove(user_id):

    return crud.crud_delete(DATAFILE,user_id)


def is_contained(user_id):
    database = read()

    column_for_check = []

    for data in database:
        column_for_check.append(data[0])

    return user_id in column_for_check 


def look_for_biggest_revenue_transaction(database):

    id_price_set = {line[0]: float(line[3]) for line in database}

    for value in id_price_set.values():

        price = max(id_price_set.values())

    for key, value in id_price_set.items():

        if value == price:
            id_of_max = key

    return {str(id_of_max): str(price)}


def look_for_biggest_revenue_product(database):
    products_and_prices_dict = {}

    for entry in database:

        if entry[2] in products_and_prices_dict.keys():
            products_and_prices_dict[entry[2]] += float(entry[3])
        else:
            products_and_prices_dict[entry[2]] = float(entry[3])

    for value in products_and_prices_dict.values():

        max_revenue = max(products_and_prices_dict.values())

        for key, value in products_and_prices_dict.items():

            if value == max_revenue:
                product_of_max = key
            
    return {str(product_of_max): str(max_revenue)}


def get_index_of_element(element, data_list, reverse = False):
    last_index_in_list = len(data_list) - 1

    if reverse:
        copied_list = data_list.copy()
        copied_list.reverse()
        
        index_of_element_in_revers = copied_list.index(element)
        index_of_element = last_index_in_list - index_of_element_in_revers
    else:
        index_of_element = data_list.index(element)

    return index_of_element
    

def get_pair_sorted_by_order(first_element, second_element, data_list):
    position_of_first_element = data_list.index(first_element)
    position_of_second_element = data_list.index(second_element)

    if position_of_first_element > position_of_second_element:
        first_element, second_element = second_element, first_element

    return first_element, second_element


def get_column_from_data(column_index, data = DATAFILE, type_data_in_column = str):
    data_list = []

    database = crud.crud_read(data)
    
    for row in database:
        needed_data = type_data_in_column(row[column_index])
        data_list.append(needed_data)

    return data_list


def count_transactions_beetween(first_index, second_index, data_list):
    sum_of_transactions = 0

    for i in range(first_index, second_index + 1):
        sum_of_transactions += data_list[i]

    return sum_of_transactions