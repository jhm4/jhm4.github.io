from sklearn import svm
import pylab
import pandas as pd
import numpy as np
import IPython
import matplotlib.pyplot as plt
from sklearn.externals import joblib
#iris = datasets.load_iris()
#digits = datasets.load_digits()
df= pd.read_csv(r"C:\Users\John\jhm4.github.io\UBSI2.csv", parse_dates=['Date'], infer_datetime_format=True)


adjPrice = df[' Adj Close']
Volume = df[' Volume']
s = pd.Series(adjPrice)
s_Volume = pd.Series(Volume)
lastDate = df.last_valid_index()
train_end = int(round(lastDate*.3))


#One whole Investment
SVM_data = []
SVM_target = []
z = train_end
lastInvest = lastDate-365-44
#testdate = 850
while z < lastInvest:
	#Profit or Loss
	if s[z-1]-s[z+44] > 0:
		P_L = 1
	else:
		P_L = 0
	Ynumpy = np.array(P_L)

	X = []

	#Calculate PE Ratio
	PE_RAT = s[z+44]/(s[z+44]-s[z+44+365])
	X.append(PE_RAT)

	#Calculate 2-day Net Price Change
	Two_Day = s[z+44]-s[z+46]
	X.append(Two_Day)

	#Calculate 44-day Net Price Change
	Forty_Day = s[z+44]-s[z+88]
	X.append(Forty_Day)

	#10-Day Volatility
	VTY_slice = s[z+44:(z+54)]
	VTY_slice = VTY_slice.as_matrix()
	Volatility = np.var(VTY_slice)
	X.append(Volatility)

	#44 Day Volatility
	VTY_slice_44 = s[(z+44):(z+88)]
	VTY_slice_44 = VTY_slice_44.as_matrix()
	Volatility_44 = np.var(VTY_slice_44)
	X.append(Volatility_44)

	#Xnumpy = np.array(X)
	
	#Calculate Volume
	X.append(s_Volume[z+44])

	#Calculate 10-Day moving average
	i = train_end + 44
	while i <= train_end+94:
		slice_10 = pd.Series(s[i:(i+10)])
		avg = np.mean(slice_10)
		X.append(avg)
		i += 1
	
	#Calculate 50-Day Moving Average
	m = train_end + 44
	while m <= train_end+94:
		slice_50 = pd.Series(s[m:(m+50)])
		avg = np.mean(slice_50)
		X.append(avg)
		m += 1


	Xnumpy = np.array(X)
	SVM_data.append(Xnumpy)
	SVM_target.append(Ynumpy)
	z += 1

#print(SVM_target)
SVM_data = np.array(SVM_data)
SVM_target = np.array(SVM_target)

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(SVM_data, SVM_target)
joblib.dump(clf, 'SVM_Model2.pkl')


#clf2 = joblib.load('SVM_Model2.pkl')

#f = open('SVM_predictions.txt', 'w')

#day = 100
#while day < 200:

#	X_p = []
	
#	PE_RAT_p = s[day]/(s[day]-s[day+365])
#	X_p.append(PE_RAT_p)

#	Two_Day_p = s[day]-s[day+2]
#	X_p.append(Two_Day_p)
	
#	Forty_Day_p = s[day]-s[day+44]
#	X_p.append(Forty_Day_p)
	
#	VTY_slice_p = s[day:(day+10)]
#	VTY_slice_p = VTY_slice_p.as_matrix()
#	Volatility_p = np.var(VTY_slice_p)
#	X_p.append(Volatility_p)

#	VTY_slice_44_p = s[(day):(day+44)]
#	VTY_slice_44_p = VTY_slice_44_p.as_matrix()
#	Volatility_44_p = np.var(VTY_slice_44_p)
#	X_p.append(Volatility_44_p)
	
#	X_p.append(s_Volume[day])
	
#	i = day
#	while i <= day+50:
#		slice_10_p = pd.Series(s[i:(i+10)])
#		avg_p = np.mean(slice_10_p)
#		X_p.append(avg_p)
#		i += 1
	
#	i = day
#	while i <= day+50:
#		slice_50_p = pd.Series(s[i:(i+50)])
#		avg_p = np.mean(slice_50_p)
#		X_p.append(avg_p)
#		i += 1

#	SVM_predict = np.array(X_p)

	#f.write("Current Day: ", s[day])
	#f.write("Next Day: ", s[day-1])

#	f.write(str(clf2.predict(SVM_predict)))
#	day += 1



