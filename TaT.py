import sys
import argparse
import csv



def main(passed_args=None):

    parser = argparse.ArgumentParser(prog='Track_and_trace_program', 
                                description='Enter product parameters for %(prog)s')
    parser.add_argument('Product_name', action='append', 
                    help='Enter product name in Latin letters')
    parser.add_argument('Product_batch', action='append', 
                    help='Enter product batch')
    parser.add_argument('Product_expire', action='append', 
                    help='Enter product expire date in format YYYY/MM')
    
    args = parser.parse_args(passed_args)
        
    if args.Product_name and args.Product_batch and args.Product_expire: 
        name, batch, expire = args.Product_name[0], args.Product_batch[0], args.Product_expire[0] 
        return name, batch, expire

if __name__ == '__main__':
    main()

name, batch, expire = main()


def join_product_code_data(name, batch, expire):
    """
    Function to join product data from input
    """
    product = name + batch + expire
    return product

def open_not_used_codes(filename='codes.txt'):
    """
    Function to read unique codes from a file
    """
    file = open(filename, 'r')
    lines = file.read().split('\n')
    file.close()
    return lines

product = join_product_code_data(name, batch, expire)
lines = open_not_used_codes()
print(lines)

PRODUCT_CODES = 0
def join_product_code(product=product, lines=lines):
    global PRODUCT_CODES
    PRODUCT_CODES += 1
    """"
    Function to produce `product_code` 
    from uniques code and data from input
    """   
    first_line = lines[0]
    product_code = product + '/' + first_line
    return product_code

product_code = join_product_code()
print(product_code)
print(PRODUCT_CODES)


def create_box_code(product=product, lines=lines, box_size=3):
    """"
    Function to produce `box_code` 
    from uniques code, data from input and box size.
    """
    first_line = lines[0]
    box_code = product + '/' + first_line + '/box'
    return box_code

if PRODUCT_CODES == 3:
    box_code = create_box_code()
else:
    box_code = None


def create_pallet_code(product=product, lines=lines, box_size=3):
    """"
    Function to produce `pallet_code` 
    from uniques code, data from input and pallet size.
    """
    first_line = lines[0]

    
    pallet_code = product + '/' + first_line + '/pallet'
    return pallet_code

def create_used_codes_reg(new_filename='used_codes.txt'):
    """
    Function to register used unique codes.
    """
    file = open(new_filename, 'a')
    lines = open_not_used_codes()
    n_lines = lines[0]
    file.write(n_lines+'\n')
    file.close()
    return n_lines

n_lines = create_used_codes_reg()

def delete_used_codes(filename='codes.txt'):
    """
    Function to delete used unique codes 
    from a not used codes list.
    """
    file = open(filename, 'r')
    contents = file.readlines()
    file.close()

    contents.pop(0) # remove the line item from list, by line number, starts from 0

    file = open(filename, 'w')
    contents = "".join(contents)
    file.write(contents)
    file.close()
    return filename

filename = delete_used_codes()

def create_product_codes_reg(product_code, new_filename='product_codes.txt'):
    """
    Function to create .txt and record 
    unique product codes to it.
    """
    file = open(new_filename, 'a')
    product_code_lines = product_code
    
    file.write(product_code+'\n')
    file.close()
    return product_code_lines

product_code_lines = create_product_codes_reg(product_code)

def TaT_data_csv(filename='Tat_data.csv', pallet_code=None):
    import os.path

    """
    Function to create .csv file and record 
    1. used unique codes from file
    2. generated unique product_codes
    3. box_codes
    4. pallete_codes
    """

    file_exist = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        
        headers = ['codes','product_codes', 'box_codes', 'pallet_codes']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        if not file_exist:
            writer.writeheader() # file doesn't exist yet, write a header
        
        writer.writerow({'codes': lines[0], 'product_codes': product_code_lines, 'box_codes': box_code, 'pallet_codes': pallet_code})

TaT_data_csv()

