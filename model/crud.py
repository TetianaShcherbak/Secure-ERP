from model import data_manager


def crud_create(file_name, data_to_add, user_id):
    database = data_manager.read_table_from_file(file_name) 

    for data in database:
        if data[0] == user_id:
            return False

    if data_to_add not in database:
        database.append(data_to_add)      

    data_manager.write_table_to_file(file_name, database, separator=';')

    return True
    

def crud_read(file_name):
    file_content = data_manager.read_table_from_file(file_name)

    return file_content


def crud_update(file_name, user_id, new_data_table):
    database = data_manager.read_table_from_file(file_name)

    new_data_table[0] = user_id
    
    crud_delete(data_file=file_name, user_id=user_id)
    crud_create(file_name, new_data_table,user_id)


def crud_delete(user_id, data_file):
    data = data_manager.read_table_from_file(data_file)
    for entry in data:
        if entry[0] == user_id:
            data.remove(entry)
            data_manager.write_table_to_file(data_file, data, separator=';')
            return True
    return False

#print(crud_update("model/hr/hr.csv", ["test_4","Cecil","1993-04-04","Sales","5"], ["test_7","1111","1993-04-04","Sales","111"]))
###########