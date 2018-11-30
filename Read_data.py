
#! Python
import pandas as pd

def read_code(code):
    code = pd.read_csv(code)
    return code
read_code('codes.csv')

