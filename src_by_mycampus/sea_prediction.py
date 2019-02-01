import pandas as pd
import numpy as np
import datetime

fldname = \
  "년도,월,일,시간,유속,유향,유향deg,수온,염분,유의파고,유의파주기,최대파고,최대파주기,풍속,풍향,풍향deg,기온,기압,시정"

import pandas as pd
df = pd.read_csv('Haewoondae_2016_8.csv',
                 names=fldname.split(','),
                 header=0,
                 na_values=['-', 'null'],
                 dtype={'시간': object, '유향': object, '풍향': object, '시정': object,
                        }
                 )



  
for r in df.itertuples():
    print(r.유속, r.수온)
    break
    
    
def scale_pd_column(column, bottom=None, top=None):
  '''
  (X - 최소값) / (최대 - 최소)
  '''
  if bottom == None:
    bottom = column.min()
  if top == None:
    top = column.max()
  print(column)
  shifted = column.values - bottom
  scaled = shifted / (top - bottom)
  return scaled, bottom, top

print(list(df.columns))

print(df.유속.values[:30])
print(df.유향.values[:30])

sp, b, t = scale_pd_column(df.유속)
print(b, t, sp[:30])