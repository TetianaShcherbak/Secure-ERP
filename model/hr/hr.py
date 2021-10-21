""" Human resources (HR) module
Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import util
from model import crud

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


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

