import argparse

parser = argparse.ArgumentParser(prog='Track_and_trace_program', 
                                description='Enter product parameters for %(prog)s')
parser.add_argument('Product_name', action='append', 
                    help='Enter product name in Latin letters')
parser.add_argument('Product_batch', action='append', 
                    help='Enter product batch')
parser.add_argument('Product_expire', action='append', 
                    help='Enter product expire date in format YYYY/MM')
args = parser.parse_args()
print(args.Product_name, args.Product_batch, args.Product_expire)
