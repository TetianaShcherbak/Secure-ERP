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


def remove(user_id):
   return crud.crud_delete(user_id,DATAFILE)


def add(data_to_add):
    user_id = util.generate_id()
    data_to_add.insert(0,user_id)
    return crud.crud_create(DATAFILE, data_to_add, user_id)


def update(new_data_table):
    user_id = util.generate_id()
    crud.crud_update(DATAFILE, user_id, new_data_table)