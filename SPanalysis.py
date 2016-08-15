from sklearn import svm
import pandas as pd
import numpy as np
import IPython
from sklearn.externals import joblib
import sklearn.metrics as stats
from sklearn.metrics import classification_report


#df= pd.read_csv(r"C:\Users\John\jhm4.github.io\SP500.csv", delim_whitespace=True)
#df.to_pickle('SP_df.pkl')
df = pd.read_pickle('SP_df.pkl')
#print(df)
Tickers = df['Ticker']

g = open('SP500_lowPE.txt', 'w')

print(np.mean(df['PE']))
j = 0
for i in df['PE']:
	if i < 15: 
		g.write(Tickers[j])
		g.write(" ")
		g.write(str(i))
		g.write('\n')
	#print(i)
	j += 1