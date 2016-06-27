from sklearn import datasets
import pylab
import pandas as pd
import numpy as np
import IPython
import matplotlib.pyplot as plt
#iris = datasets.load_iris()
#digits = datasets.load_digits()
df= pd.read_csv(r"C:\Users\John\jhm4.github.io\SRPT.csv", parse_dates=['Date'], infer_datetime_format=True)


adjPrice = df[' Adj Close']
s = pd.Series(adjPrice)
lastDate = df.last_valid_index()
train_end = int(round(lastDate*.3))


i = lastDate
j = 0
while i > train_end + 10:
	slice_ = pd.Series(s[lastDate-j:(i-10):-1])
	print(slice_)
	j += 1
	i -= 1

#slice_.plot()
#adjPrice.plot()
#plt.show()
#plot(arange(5))
#print(help(datasets.load_iris()))
#print(digits.data)