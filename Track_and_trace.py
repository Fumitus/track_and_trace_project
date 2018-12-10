import pandas as pd

def product_code_lines(name, batch, expire):
    
    read_code=pd.read_csv('codes.csv')

    code_from_file = str(read_code.iloc[:1]).strip().split()[2]

    batch_and_expire = str(batch+'/'+expire)

    product_code = batch_and_expire+'/'+code_from_file
    
    product_code_frame=pd.DataFrame({
                                'Code': [code_from_file],
                                'Batch and expire': [batch_and_expire],
                                'Product Code': [product_code],
                                'Product name': [name],
                                'Box': [0],
                                'Pallet': [0],
                                'Batch': [batch],
                                'Expire date': [expire]})
    
    # print(product_code_frame)
    product_code_frame.to_excel('Output.xlsx', index=False)
    return product_code_frame
    

product_code_lines('Tarka','2018/12/09','2020/12')
    