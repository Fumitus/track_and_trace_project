import sys
import argparse
import csv
import os.path
import json


def create_argument_parser():
    parser = argparse.ArgumentParser(
        prog="Track_and_trace_program",
        description="Enter product parameters for %(prog)s",
    )

    parser.add_argument("name", help="Enter product name in Latin letters")
    parser.add_argument("batch", help="Product batch")
    parser.add_argument("expiration", help="Product expire date in format YYYY/MM")
    return parser

def code_management(filename="data/codes.txt", used_codes_filename="data/used_codes.txt"):
    """
    Function to read unique code from file
    to delete used code from list
    to create new file for used_codes registration
    """
    with open(filename, "r") as f:
        contents = f.readlines()
        # remove the line item from list, by line number, starts from 0 
        # and returns it's value
        pop_value = contents.pop(0)
        code = pop_value.strip()
        
        with open(used_codes_filename, "a") as f:
            f.write(pop_value)
        
    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)
    return code

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

def create_pallet_code(product, code):
    """"
    Function to produce `pallet_code` 
    from uniques code, data from input and pallet size.
    """
    first_line = code

    pallet_code = product + "/" + first_line + "/pallet"
    return pallet_code

def stuff():
    """
    Funtion to group product_codes and assign to box_code
    and latter group box_codes and assign to pallet_code
    """
    pass 

def create_product_codes_reg(product_code, new_filename="data/product_codes.txt"):
    """
    Function to create .txt and record 
    unique product codes to it.
    """
    product_code_lines = product_code
    with open(new_filename, "a") as f:
        f.write(product_code_lines + "\n")


def track_data_csv(code, product_code_lines, box_code, pallet_code, filename="data/Track_data.csv"):
    """
    Function to create .csv file and record 
    1. used unique codes from file
    2. generated unique product_codes
    3. box_codes
    4. pallete_codes
    """

    file_exist = os.path.isfile(filename)

    with open(filename, "a", newline="") as csvfile:

        headers = ["codes", "product_codes", "box_codes", "pallet_codes"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        if not file_exist:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow(
            {
                "codes": code,
                "product_codes": product_code_lines,
                "box_codes": box_code,
                "pallet_codes": pallet_code,
            }
        )


def main(passed_args=None):
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()
    product = join_product_code_data(args.name, args.batch, args.expiration)
    codes = code_management()
    product_codes = []
    for i in codes:
        if i == 0:
            box_code = create_box_code(product, codes[i])
        else:
            product_codes.append(join_product_code(product, codes[i]))

    jsonObject = {}
    jsonObject[box_code] = product_codes
    json.dump(jsonObject)
    # product_code = join_product_code(product, code)
    # create_product_codes_reg(product_code)
    # track_data_csv(code, product_code, 'box_code', 'pallet_code')


if __name__ == "__main__":
    main()
