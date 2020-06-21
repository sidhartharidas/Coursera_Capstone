import numpy as np
import pandas as pd

df = pd.read_csv('https://cocl.us/datascience_survey_data',index_col = 0)
print ('Data read into a pandas dataframe!')
df.head()
