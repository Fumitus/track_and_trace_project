import pandas as pd
import csv
import json
import xlsxwriter

#def product_code_lines(name, batch, expire):

name = 'Tarka'
batch = '2018/12/09'
expire = '2020/12'

# def read_code_from_file():
#     code_from_file = pd.read_csv('codes.csv')
#     return code_from_file


#     # with open("codes.csv", newline="") as f:
#     # csvreader = csv.reader(f)
#     # for row in csvreader:
#     #     i = str(row[0]) # first column of the row
#     #     print (i)


# def join_batch_and_expire(batch, expire):
#     batch_and_expire = batch +'/'+ expire
#     return batch_and_expire


# def join_product_code(batch_and_expire, code_from_file):
#     product_code = batch_and_expire +'/'+ code_from_file
#     return product_code


# def join_box(product_code):
#     box = []
#     batch_and_expire = join_product_code()

#     while box <= 10:
#         box.append(product_code)
#     else:
#         box_code = batch_and_expire +'/'+ code_from_file
#     return box_code



# def join_pallet(box_code):
#     pallet = []
#     while pallet <= 10:
#         pallet.append(box_code)
#     else:
#         pallet_code = batch_and_expire +'/'+ code_from_file
#     return pallet_code

# header_keys = {'Code': [None], 'Product name': [name], 'Batch': [batch], 'Expire date': [expire],'Product Code': [None], 'Box': [None], 'Pallet': [None]}

product_code_frame = {}
product_code_frame={'Code': '',
                     'Batch and expire': '',
                     'Product Code': '',
                     'Product name': '',
                     'Box': '',
                     'Pallet': '',
                     'Batch': '',
                     'Expire date': ''}
row_to_update = 'Code'

try: 
   oldvalue = product_code_frame[row_to_update] 
except: 
   oldvalue = ''

# to increment a value

#    try: 
#       newval = int(oldval) 
#       newval += 1
#    except: 
#       newval = 1 


#    drug_dictionary[row_to_update] = "%s" % newval

# to append a value  

   try: 
      newval = int(oldval) 
      newval += 1
   except: 
      newval = 1 


   product_code_frame[row_to_update] = "%s,%s" % (oldval,newval)



# product_code_frame = dict.fromkeys(header_keys)
# # updating the value
# header_keys.append(2)
# print(product_code_frame)





    
# product_code_frame.to_excel('Output.xlsx', index=False)
# # product_code_frame to json file
# json = json.dumps(product_code_frame)
# f = open("dict.json","w")
# f.write(json)
# f.close()

# # product_code_frame to csv file

# w = csv.writer(open("output.csv", "w"))
# for key, val in product_code_frame.items():
#     w.writerow([key, val])


# # product_code_frame to excel file

# workbook = xlsxwriter.Workbook('data.xlsx')
# worksheet = workbook.add_worksheet()

# d = {'a':['e1','e2','e3'], 'b':['e1','e2'], 'c':['e1']}
# row = 0
# col = 0

# for key in d.keys():
#     row += 1
#     worksheet.write(row, col, key)
#     for item in d[key]:
#         worksheet.write(row, col + 1, item)
#         row += 1

# workbook.close()


# return product_code_frame
    

