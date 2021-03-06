import sys
import argparse
import csv
import os.path
import json
import sqlite3
from sqlite3 import Error


def create_argument_parser():
    parser = argparse.ArgumentParser(
        prog="Track_and_trace_program",
        description="Enter product parameters for %(prog)s",
    )

    parser.add_argument("name", help="Enter product name in Latin letters")
    parser.add_argument("batch", help="Product batch")
    parser.add_argument("expiration", help="Product expire date in format YYYY/MM")
    parser.add_argument("box", type=int, help = "Determine box size.")
    return parser


def read_codes(box_size, filename="data/codes.txt"):
    """
    Function to read unique code from file
    range is defined according "box" size on input
    """
    if box_size == 1:
        sys.exit('Error: Box_size should be in range from 2 to 10')
    elif box_size in range(11):
           
        with open(filename, "r") as f:
            contents = f.read().splitlines()
            codes = contents[:box_size]
        return codes     

def create_used_codes_reg(box_size, filename="data/codes.txt", new_filename="data/used_codes.txt"):
    """
     Function to register used unique codes.
     """
    with open(filename, "r") as f:
        contents = f.readlines()
        # remove the line item from list, by line number, starts from 0
        range_to_delete = int(box_size)
        del contents[range_to_delete:]
        
    with open(new_filename, "a") as f:
        contents = "".join(contents)
        f.write(contents)

def delete_codes(box_size, filename="data/codes.txt"):
    """
    Function to delete used code from list
    to create new file for used_codes registration
    """
    with open(filename, "r") as f:
        contents = f.readlines()
        # remove the line item from list, by line number, starts from 0
        range_to_delete = int(box_size)
        del contents[:range_to_delete]
        
    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
        
    
def join_product_code_data(name, batch, expire):
    """
    Function to join product data from input
    """
    product = name + batch + expire
    return product


def join_product_code(product, code):
    """"
    Function to produce `product_code` 
    from uniques code and data from input
    """
    first_line = str(code)
    product_code = product + "/" + first_line
    return product_code

def create_box_code(product, code):
    """"
    Function to produce `box_code` 
    from uniques code, data from input and box size.
    """
    first_line = code
    box_code = product + "/" + first_line + "/box"
    return box_code

def product_codes_to_list(product, codes):
    """
    Funtion to join product_codes to a list
    """
    
    box_code = create_box_code(product, codes[0])
    product_codes_list = []
       
    for i in range(len(codes)):
        if i == 0:
            box_code = create_box_code(product, codes[i])
        else:
            product_codes_list.append(join_product_code(product, codes[i]))
    
    return product_codes_list, box_code

def product_code_group(box_code, product_codes_list):
    """
    Function to create dictionary from 
    box_code and product_codes_list
    """
    box = {box_code:product_codes_list}
    print(box)
    return box

def create_product_codes_reg(box, new_filename="data/product_codes.txt"):
    """
    Function to create .txt and record 
    unique product codes to it.
    """
    product_code_lines = str(box)
    with open(new_filename, "a") as f:
        f.write(product_code_lines + "\n")



def create_connection(db_file):
    """ create a database connection to a SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_project(conn, project):
    """
    Create a new project into the box_table
    :param conn:
    :param project:
    :return: project id
    """
    sql = '''INSERT INTO product_table(product_name, product_batch)
            VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = '''INSERT INTO box_table(box, codes, product_codes_list,box_code, project_id)
            VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid

def main(passed_args=None):
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()
    product = join_product_code_data(args.name, args.batch, args.expiration)
    box_size = args.box
    codes = read_codes(box_size)
    create_used_codes_reg(box_size)
    product_codes_list, box_code = product_codes_to_list(product, codes)    
    box = product_code_group(box_code, product_codes_list)
    create_product_codes_reg(box)
    delete_codes(box_size)
    database = "data/sqlite_track_and_trace.db"
    sql_create_product_table = """ CREATE TABLE IF NOT EXISTS product_table (
                                        id integer PRIMARY KEY,
                                        product_name,
                                        product_batch
                                    ); """
    sql_create_box_table = """ CREATE TABLE IF NOT EXISTS box_table (
                                        id integer PRIMARY KEY,
                                        box,
                                        codes,
                                        product_codes_list,
                                        box_code,
                                        project_id
                                    );"""
    
    conn = create_connection(database)
    if conn is not None:
        # create product_table
        create_table(conn, sql_create_product_table)
        # create box_table
        create_table(conn, sql_create_box_table)
    else:
        print("Error! Cannot create the database connection.")

    with conn:
        #create a new project for product
        project = (args.name, args.batch)
        project_id = create_project(conn, project)

        # create a new task for product batch

        task = (str(box), str(codes), str(product_codes_list), str(box_code), str(project_id))
        create_task(conn, task)


    
if __name__ == "__main__":
    main()
