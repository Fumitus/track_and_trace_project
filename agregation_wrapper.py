def agregation(func_to_agregate):
    def box_dict():
        box_list = ['APAP20181215202012/100,025/box']
        product_code_list = ['APAP20181212202012/100,027',
                            'APAP20181212202012/100,028',
                            'APAP20181212202012/100,029']

        for box_dictionary in product_code_list:
            box_dictionary = dict(zip(box_list, product_code_list))
            print(box_dictionary)

        func_to_agregate()

        pallet_list = ['APAP20181212202012/100,027/pallet']
        pallet_dict = dict(zip(pallet_list, box_dictionary))


        print(pallet_dict)

    return box_dict

def product_code_list():

    product_code_list = ['APAP20181212202012/100,027',
                            'APAP20181212202012/100,028',
                            'APAP20181212202012/100,029']
    print(product_code_list)
    return product_code_list

product_code_list()
     
product_code_list_to_pallet_dict = agregation(product_code_list)
product_code_list_to_pallet_dict()


