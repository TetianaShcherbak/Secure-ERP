def print_menu(title, list_options):
    print(title)

    for i, option in enumerate(list_options):
        if i > 0:
            print(f'({i}) {option}')

    print(f'(0) {list_options[0]}')


def print_message(message):
    print(f"{message}\n")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
# table = [[id,product,type],[0,Bazooka,portable]]
def print_table(table):
    number_of_rows = len(table)
    number_of_cols = len(table[0])

    columns_width = []
    '''
    for column_number in range(number_of_cols):
        max_column_width = 0

        for row_number in range(number_of_rows):
            max_column_width = max(max_column_width,len(table[row_number][column_number]))
            columns_width.append(max_column_width)
    
    table_width = sum(columns_width)
    print(columns_width)
    '''
    for number_of_col in range(number_of_cols):
        temp_list = []
        for number_of_row in range(number_of_rows):
            column_width = len(table[number_of_row][number_of_col]) 
            column_width += 2
            temp_list.append(column_width)
        
        max_column_width = max(temp_list)
        
        columns_width.append(max_column_width)

    table_width = sum(columns_width)

    print("/" + "-"*(table_width+(number_of_cols-1)) + "\\")

    table_prepared_to_print = []
    for i in range(len(table)):
        
        row_for_print = []

        for j in range(len(table[i])):
            column = table[i][j]
            column_width = columns_width[j]
            centered_data = column.center(column_width)
            row_for_print.append("|")
            row_for_print.append(centered_data)
        
        row_for_print.append("|")

        delimiter_row = []

        for j in range(len(table[i])):
            column_width = columns_width[j]
            centered_data = column.center(column_width)
            delimiter_row.append("|")
            delimiter_row.append("-"*column_width)
        
        delimiter_row.append("|")

        table_prepared_to_print.append(row_for_print)
        table_prepared_to_print.append(delimiter_row)

    for i in range(len(table_prepared_to_print)-1):
        row = table_prepared_to_print[i]
        string_for_print = "".join(row)
        print(string_for_print)

    print("\\" + "-"*(table_width+(number_of_cols-1)) + "/" + "\n")

print(print_table(table = [["id","product","type"],["0","Bazooka","portable"],["22","3333","456"]]))


def get_input(label):
    return input(f"{label}:\t")


def get_inputs(labels):
    labels_list = []

    for label in labels:
        labels_list.append(input(label))

    return labels_list


def print_error_message(message):
    print(f"{message}\n")
