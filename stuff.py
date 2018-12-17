box_list = ['APAP20181215202012/100,025/box'],
product_code_list = ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']

# expected_result = {'APAP20181215202012/100,025/box': ['APAP20181212202012/100,027', 'APAP20181212202012/100,028', 'APAP20181212202012/100,029']}
result = (box_list, product_code_list)

print(result)


# with open("data/codes.txt", "r") as f:
#     contents = f.readlines()
# # remove the line item from list, by line number, starts from 0
#     pop_value = contents.pop(0)
#     n_lines = pop_value
#     print(n_lines)

#     with open("data/used_codes.txt", "a") as f:
#         f.write(pop_value)

# with open("data/codes.txt", "w") as f:
#     contents = "".join(contents)
#     f.write(contents)
