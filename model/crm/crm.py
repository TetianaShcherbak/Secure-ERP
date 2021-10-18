""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
import sys
from model import data_manager, util

sys.path.insert(1, "C:/Users/macie/projekty/secure-erp-python-larxand/")

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
