""" Customer Relationship Management (CRM) module
Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import util, crud

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def remove(user_id):
    return crud.crud_delete(DATAFILE,user_id)


def add(data_to_add):
    user_id = util.generate_id()
    data_to_add.insert(0,user_id)
    return crud.crud_create(DATAFILE, data_to_add, user_id)


def update(new_data_table):
    
    return crud.crud_update(DATAFILE, new_data_table)


def get_data():
    return crud.crud_read(DATAFILE)


def select_subscribed_emails():
    data = crud.crud_read(DATAFILE)
    subscribed_emails = []
    for entry in data:
        if entry[3] == '1':
            subscribed_emails.append([entry[2]])
    return subscribed_emails


def check_customer(customer_id):
    database = crud.crud_read(DATAFILE)
    for entry in database:
        if entry[0] == customer_id:
            return True
    return False
