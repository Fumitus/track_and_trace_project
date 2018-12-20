import sys
import argparse
import csv
import os.path


def create_argument_parser():
    parser = argparse.ArgumentParser(
        prog="Track_and_trace_program",
        description="Enter product parameters for %(prog)s",
    )

    parser.add_argument("name", help="Enter product name in Latin letters")
    parser.add_argument("batch", help="Product batch")
    parser.add_argument("expiration", help="Product expire date in format YYYY/MM")
    parser.add_argument("box", help = "Determine box size. How much 'code' is put in one box")
    return parser


def read_codes(box_size, filename="data/codes.txt"):
    """
    Function to read unique code from file
    range is defined according "box" size on input
    """
    with open(filename, "r") as f:
        contents = f.read().splitlines()
        codes = contents[:box_size]
        
    return codes

def delete_codes(box_size, filename="data/codes.txt", used_codes_filename="data/used_codes.txt"):
    """
    Function to delete used code from list
    to create new file for used_codes registration
    """
    with open(filename, "r") as f:
        contents = f.read().splitlines()
        # remove line items from list, by line index, starts from 0
        # codes_to_delete = contents[:box_size]
        del contents[:box_size]
           
    with open(used_codes_filename, "a") as f:
        f.write(contents + "\n")
        
    
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
    product_codes_list = []

    box_code = create_box_code(product, codes[0])
        
    product_codes_list.append(join_product_code(product, codes[1]))
    product_codes_list.append(join_product_code(product, codes[2]))
    product_codes_list.append(join_product_code(product, codes[3]))
    product_codes_list.append(join_product_code(product, codes[4]))
    product_codes_list.append(join_product_code(product, codes[5]))

    return product_codes_list, box_code

def product_code_group(box_code, product_codes_list):
    """
    Function to create dictionary from 
    box_code and product_codes_list
    """
    box = {box_code:product_codes_list}
    return box

def create_product_codes_reg(box, new_filename="data/product_codes.txt"):
    """
    Function to create .txt and record 
    unique product codes to it.
    """
    product_code_lines = str(box)
    with open(new_filename, "a") as f:
        f.write(product_code_lines + "\n")


def main(passed_args=None):
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()
    product = join_product_code_data(args.name, args.batch, args.expiration)
    box_size = int(args.box)
    codes = read_codes(box_size)
    product_codes_list, box_code = product_codes_to_list(product, codes)    
    box = product_code_group(box_code, product_codes_list)
    create_product_codes_reg(box)
    delete_codes(box_size)


if __name__ == "__main__":
    main()
