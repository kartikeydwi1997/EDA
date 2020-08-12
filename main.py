#pip install pandas
#pip install pandas-profiling 
import pandas as pd 
from pandas_profiling import ProfileReport

df=pd.read_csv('country.csv')
print(df)

#generate a report 
profile=ProfileReport(df)
profile.to_file(output_file='country.html')