import data_manager

DATABASE_PATHS = {
    "crm": "/Users/tetiana/Documents/CodeCool/Week_Pair_5/secure-erp-python-larxand/model/crm/crm.csv",
    "hr": "/Users/tetiana/Documents/CodeCool/Week_Pair_5/secure-erp-python-larxand/model/hr/hr.csv",
    "sales": "/Users/tetiana/Documents/CodeCool/Week_Pair_5/secure-erp-python-larxand/model/sales/sales.csv",
    "test": "/Users/tetiana/Documents/CodeCool/Week_Pair_5/secure-erp-python-larxand/model/test.csv"
    }

def crud_create(file_name, data_to_add, separator=';'):
    database = crud_read(file_name) 

    if data_to_add not in database:
        database.append(data_to_add)

    new_file = open(file_name, "w")

    for record in database:
        row = separator.join(record)
        new_file.write(row + "\n")

    new_file.close()



def crud_read(file_name):
    file_content = data_manager.read_table_from_file(file_name)

    return file_content


def crud_update(file_name, old_data_table, new_data_table):
    database = data_manager.read_table_from_file(file_name)

    for data in database:

        if data == old_data_table:
            old_data_id = old_data_table[0]
            new_data_id = old_data_id
            new_data_table[0] = new_data_id

            crud_delete(file_name, old_data_id)
            crud_create(file_name, new_data_table)


def crud_delete(file_name, id_data_to_delete: str, separator=';'):
    database = data_manager.read_table_from_file(file_name)

    new_file = open(file_name, "w")
    for record in database:

        if record[0] != id_data_to_delete:
            row = separator.join(record)
            new_file.write(row + "\n")

    new_file.close()






crud_create(DATABASE_PATHS["test"],["id_1","name","age","email","smth else"])
crud_create(DATABASE_PATHS["test"],["id_2","name","age","email","smth else"])
crud_create(DATABASE_PATHS["test"],["id_3","name","age","email","smth else"])
crud_create(DATABASE_PATHS["test"],["id_4","name","age","email","smth else"])
print(crud_read(DATABASE_PATHS["test"]))
crud_delete(DATABASE_PATHS["test"],"id_2")
crud_update(DATABASE_PATHS["test"],["id_3","name","age","email","smth else"],["id_7","name_1","age_1","email_1","smth else_1"])

