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
    return parser


def open_not_used_codes(filename="data/codes.txt"):
    """
    Function to read unique codes from a file
    """

    with open(filename, "r") as f:
        lines = file.read().split("\n")
    return lines


def join_product_code_data(name, batch, expire):
    """
    Function to join product data from input
    """
    product = name + batch + expire
    return product


def create_box_code(product, lines, box_size=3):
    """"
    Function to produce `box_code` 
    from uniques code, data from input and box size.
    """
    first_line = lines[0]
    box_code = product + "/" + first_line + "/box"
    return box_code


def join_product_code(product, lines):
    """"
    Function to produce `product_code` 
    from uniques code and data from input
    """
    first_line = lines[0]
    product_code = product + "/" + first_line
    return product_code


def create_pallet_code(product, lines, box_size=3):
    """"
    Function to produce `pallet_code` 
    from uniques code, data from input and pallet size.
    """
    first_line = lines[0]

    pallet_code = product + "/" + first_line + "/pallet"
    return pallet_code


def create_used_codes_reg(new_filename="data/used_codes.txt"):
    """
    Function to register used unique codes.
    """

    lines = open_not_used_codes()
    n_lines = lines[0]
    with open(new_filename, "a") as f:
        file.write(n_lines + "\n")
    return n_lines


def delete_used_codes(filename="data/codes.txt"):
    """
    Function to delete used unique codes 
    from a not used codes list.
    """
    with open(filename, "r") as f:
        contents = file.readlines()

    # remove the line item from list, by line number, starts from 0
    contents.pop(0)

    with open(filename, "w"):
        file.write(contents)
    contents = "".join(contents)

    return filename


def create_product_codes_reg(product_code, new_filename="data/product_codes.txt"):
    """
    Function to create .txt and record 
    unique product codes to it.
    """
    product_code_lines = product_code
    with open(new_filename, "a") as f:
        file.write(product_code + "\n")

    return product_code_lines


def TaT_data_csv(filename="data/Tat_data.csv", pallet_code=None):
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
                "codes": lines[0],
                "product_codes": product_code_lines,
                "box_codes": box_code,
                "pallet_codes": pallet_code,
            }
        )


def main(passed_args=None):
    argument_parser = create_argument_parser()
    args = argument_parser.parse_args()
    product = join_product_code_data(args.name, args.batch, args.expiration)
    lines = open_not_used_codes()
    delete_used_codes()
    create_used_codes_reg()
    product_code_lines = create_product_codes_reg(product_code=product)
    # TaT_data_csv()


if __name__ == "__main__":
    main()
