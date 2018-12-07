import pandas as pd

product_code(input('Product name: '), input('Product batch: '), input('Expire date: '))

def read_code(code):
    codes = pd.read_csv(code)
    return codes
read_code('codes.csv')

def product_code(name, batch, expire):
    """
    ENter batch data and store in variables
    """
    product_name = name.capitalize().strip()
    batch_code = batch+expire
    return product_name, batch_code 



product_code=pd.DataFrame({'Batch and expire': ['0'],
                          'Product Code': ['0'],
                          'Product name': ['0'],
                          'Box': [0],
                          'Pallet': [0],
                          'Batch': [0],
                          'Expire date': [0]})

codes_output=codes.join(product_code)
codes_output.to_csv('Output.csv')