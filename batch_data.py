def batch_data():
    """
    ENter batch data and store in variables"""
    name = input('Enter product name: ')
    batch = input('Enter product batch: ')
    expire = input('ENter product expire date: ')
    print('Product {} batch {} will expire in {}'.format(name,batch,expire))