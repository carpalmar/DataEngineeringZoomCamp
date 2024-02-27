import sys

import pandas as pd

print(sys.argv)

day = sys.argv[1]

pd = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

print(pd)

print('Funciona para el dia =  f{day}')