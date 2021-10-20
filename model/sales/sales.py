""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""
import sys
from model import data_manager, util, crud

sys.path.insert(1, "C:/Users/macie/projekty/secure-erp-python-larxand/")

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def read():

    return crud.crud_read(DATAFILE)

def add(data_to_add):
    trade_id = util.generate_id()

    data_to_add.insert(0,trade_id)

    return crud.crud_create(DATAFILE, data_to_add, trade_id)

def update(new_data_table):

    return crud.crud_update(DATAFILE, new_data_table)

def is_contained(user_id):
    database = read()

    column_for_check = []

    for data in database:
        column_for_check.append(data[0])
    
    return user_id in column_for_check

def remove(user_id):

   return crud.crud_delete(DATAFILE,user_id)