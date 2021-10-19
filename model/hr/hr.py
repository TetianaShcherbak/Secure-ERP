""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
import sys
from model import data_manager, util

sys.path.insert(1, "C:/Users/macie/projekty/secure-erp-python-larxand/")

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def handle_update(user_id):
    # CRUD READ
    data = data_manager.read_table_from_file(DATAFILE)
    for entry in data:
        if entry[0] == user_id:
            # CRUD NEW DATA
            name = input("Please provide new name: ")
            date_of_birth 
            data.remove(entry)
            # CRUD UPDATE
            data_manager.write_table_to_file(DATAFILE, data, separator=';')
            return True
    return False
