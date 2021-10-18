""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def handle_remove(user_id):
    # CRUD READ
    data = data_manager.read_table_from_file(DATAFILE)
    for entry in data:
        if entry[0] == user_id:
            # CRUD DELETE
            data.remove(entry)
            # CRUD UPDATE
            data_manager.write_table_to_file(DATAFILE, data, separator=';')
            return True
    return False

    




