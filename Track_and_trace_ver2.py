import pandas as pd

#def product_code_lines(name, batch, expire):

name = 'Tarka'
batch = '2018/12/09'
expire = '2020/12'

def read_code_from_file():
    code_from_file = pd.read_csv('codes.csv')
    return code_from_file



def join_batch_and_expire(batch, expire):
    batch_and_expire = batch +'/'+ expire
    return batch_and_expire


def join_product_code(batch_and_expire, code_from_file):
    product_code = batch_and_expire +'/'+ code_from_file
    return product_code


def join_box(product_code):
    box = []
    batch_and_expire = join_product_code()

    while box <= 10:
        box.append(product_code)
    else:
        box_code = batch_and_expire +'/'+ code_from_file
    return box_code



def join_pallet(box_code):
    pallet = []
    while pallet <= 10:
        pallet.append(box_code)
    else:
        pallet_code = batch_and_expire +'/'+ code_from_file
    return pallet_code



# product_code_frame=pd.DataFrame({
#                             'Code': [code_from_file],
#                             'Batch and expire': [batch_and_expire],
#                             'Product Code': [product_code],
#                             'Product name': [name],
#                             'Box': [box_code],
#                             'Pallet': [pallet_code],
#                             'Batch': [batch],
#                             'Expire date': [expire]})
    
    
product_code_frame.to_excel('Output.xlsx', index=False)
return product_code_frame
    

