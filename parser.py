

# parser = argparse.ArgumentParser(prog='Track_and_trace_program', 
#                                 description='Enter product parameters for %(prog)s')
# parser.add_argument('Product_name', action='append', 
#                     help='Enter product name in Latin letters')
# parser.add_argument('Product_batch', action='append', 
#                     help='Enter product batch')
# parser.add_argument('Product_expire', action='append', 
#                     help='Enter product expire date in format YYYY/MM')
# args = parser.parse_args()
# print(args.Product_name, args.Product_batch, args.Product_expire)


import sys
import argparse

def main(passed_args=None):

    parser = argparse.ArgumentParser(prog='Track_and_trace_program', 
                                description='Enter product parameters for %(prog)s')
    parser.add_argument('Product_name', action='append', 
                    help='Enter product name in Latin letters')
    parser.add_argument('Product_batch', action='append', 
                    help='Enter product batch')
    parser.add_argument('Product_expire', action='append', 
                    help='Enter product expire date in format YYYY/MM')
    
    args = parser.parse_args(passed_args)
        
    if args.Product_name and args.Product_batch and args.Product_expire: 
        name, batch, expire = args.Product_name[0], args.Product_batch[0], args.Product_expire[0] 
        return name, batch, expire

if __name__ == '__main__':
    main()