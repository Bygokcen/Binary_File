import os


def get_table_names():
    table_directory ='tables'
    table_names = []

    for file in os.listdir(table_directory):
        if file.endswith(".pickle"):
            table_name=file[:-7] # '.pickle' silinir
            table_names.append(table_name)
    return table_names