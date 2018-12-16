def pallet(func):
    def join():
        print('|APAP20181212202012/100,024/pallet')
        func()
        print('Full/APAP20181212202012/100,024/pallet|')
    return join

def content(func):
    def join():
        print('APAP20181215202012/100,025/box')
        func()
        print('Full/APAP20181215202012/100,025/box')
    return join

def product():
    product = ['APAP20181212202012/100,026',
                'APAP20181212202012/100,027',
                'APAP20181212202012/100,028']
    print(product[0])
    print(product[1])
    print(product[2])

batch = pallet(content(product))
batch()


