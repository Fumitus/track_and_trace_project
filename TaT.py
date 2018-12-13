import sys

name, batch, expire = sys.argv[1:]

print(name, batch, expire)

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

def join_product_code(product, lines):
    first_line = lines[0]
    product_code = product + '/' + first_line
    return product_code

product_code = join_product_code(product=product, lines=lines)
print(product_code)



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

def create_product_codes_reg(product_code=product_code, new_filename='product_codes.txt'):
    
    file = open(new_filename, 'a')
    product_code_lines = product_code
    
    file.write(product_code+'\n')
    file.close()
    return product_code_lines

product_code_lines = create_product_codes_reg()
