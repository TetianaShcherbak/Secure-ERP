""" Customer Relationship Management (CRM) module
Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util, crud


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

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