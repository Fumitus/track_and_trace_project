import sys
import argparse

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

def counter(func):
    
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        print(res)
        return res
    wrapper.count = 0
    return wrapper

name, batch, expire = main()

def join_product_code_data(name, batch, expire):
    product = name + batch + expire
    return product

def open_not_used_codes(filename='codes.txt'):
    file = open(filename, 'r')
    lines = file.read().split('\n')
    file.close()
    return lines

product = join_product_code_data(name, batch, expire)
lines = open_not_used_codes()
print(lines)

@counter
def join_product_code(product, lines):
    first_line = lines[0]
    product_code = product + '/' + first_line
    return product_code

product_code = join_product_code(product=product, lines=lines)
print(product_code)

@counter
def create_box_code(product, lines):
    first_line = lines[0]
    box_code = product + '/' + first_line + '/box'
    return box_code

@counter
def create_pallet_code(product, lines):
    first_line = lines[0]
    pallet_code = product + '/' + first_line + '/pallet'
    return pallet_code

def create_used_codes_reg(new_filename='used_codes.txt'):
    
    file = open(new_filename, 'a')
    lines = open_not_used_codes()
    n_lines = lines[0]
    file.write(n_lines+'\n')
    file.close()
    return n_lines

n_lines = create_used_codes_reg()

def delete_used_codes(filename='codes.txt'):
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
    
    file = open(new_filename, 'a')
    product_code_lines = product_code
    
    file.write(product_code+'\n')
    file.close()
    return product_code_lines

# PRODUCT_CODES_GENERATED = 0
# BOX_CODES_GENERATED = 0
# PALLET_CODES_GENERATED = 0

# def code_counter():
#     global PRODUCT_CODES_GENERATED
#     PRODUCT_CODES_GENERATED +=1

#     global BOX_CODES_GENERATED
#     global PALLET_CODES_GENERATED
 
#     BOX_CODES_GENERATED +=1
#     PALLET_CODES_GENERATED +=1

#     pass

product_code_lines = create_product_codes_reg(product_code)




