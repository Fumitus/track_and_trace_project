import pandas as pd

def read_code(code):
    code = pd.read_csv(code)
    return code
read_code('codes.csv')

def batch_data(name, batch, expire, code):
    """
    ENter batch data and store in variables
    """
    name = input('Enter product name: ')
    batch = input('Enter product batch: ')
    expire = input('Enter product expire date: ')
    product_code = str(batch+expire+code[0])