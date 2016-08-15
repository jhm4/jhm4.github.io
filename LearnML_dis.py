from sklearn import svm
import pandas as pd
import numpy as np
import IPython
from sklearn.externals import joblib
import sklearn.metrics as stats
import winsound


df= pd.read_csv(r"C:\Users\John\jhm4.github.io\DIS2.csv", parse_dates=['Date'], infer_datetime_format=True)


adjPrice = df[' Adj Close']
Volume = df[' Volume']
s = pd.Series(adjPrice)
s_Volume = pd.Series(Volume)
lastDate = df.last_valid_index()
train_end = int(round(lastDate*.3))


def update(new):
	new = new
	PorL = s[new-1]-s[new+44]

	SVM_data.append(SVM_predict)
	if profitloss > 0:
		PL = 1
	else:
		PL = 0
	SVM_target.append(np.array(PL))
	SVM_data2 = np.array(SVM_data)
	SVM_target2 = np.array(SVM_target)

	clf.fit(SVM_data2, SVM_target2)
	joblib.dump(clf, 'DIS_Model.pkl')



#One whole Investment
SVM_data = []
SVM_target = []
z = train_end
lastInvest = lastDate-365-44
print(str(train_end))

while z < lastInvest:
	#Profit or Loss
	if s[z-1]-s[z+44] > 0:
		P_L = 1
	else:
		P_L = 0
	Ynumpy = np.array(P_L)

	X = []

	#Calculate PE Ratio
	#PE_RAT = s[z]/(s[z]-s[z+365])
	#X.append(PE_RAT)

	Two_Day = s[z]-s[z+2]
	X.append(Two_Day)

	One_Day = s[z]-s[z+1]
	X.append(One_Day)

	Three_Day = s[z]-s[z+3]
	X.append(Three_Day)

	#Calculate 44-day Net Price Change
	#Forty_Day = s[z+44]-s[z+88]
	#X.append(Forty_Day)


	#10-Day Volatility
	VTY_slice = s[z:(z+10)]
	VTY_slice = VTY_slice.as_matrix()
	Volatility = np.var(VTY_slice)
	X.append(Volatility)

	#44 Day Volatility
	#VTY_slice_44 = s[(z+44):(z+88)]
	#VTY_slice_44 = VTY_slice_44.as_matrix()
	#Volatility_44 = np.var(VTY_slice_44)
	#X.append(Volatility_44)

	#Xnumpy = np.array(X)
	
	#Calculate Volume
	X.append(s_Volume[z])


	#10-Day Average
	#i = train_end + 44
	#slice_10 = pd.Series(s[i:i+10])
	#avg_10 = np.mean(slice_10)
	#X.append(avg_10)
	#i = z
	#while i <= z+5:
	#	slice_10 = pd.Series(s[i:(i+10)])
	#	avg = np.mean(slice_10)
	#	X.append(avg)
	#	i += 1
	
	#Calculate 50-Day Moving Average
	#m = z
	#while m <= z+5:
	#	slice_50 = pd.Series(s[m:(m+50)])
	#	avg = np.mean(slice_50)
	#	X.append(avg)
	#	m += 1

	Xnumpy = np.array(X)
	SVM_data.append(Xnumpy)
	SVM_target.append(Ynumpy)
	z += 1
SVM_data2 = np.array(SVM_data)
SVM_target2 = np.array(SVM_target)
#clf = svm.SVC(C=100)#gamma=0.001, C=100.)
clf = svm.LinearSVC(C=100)
clf.fit(SVM_data2, SVM_target2)
joblib.dump(clf, 'DIS_Model.pkl')




f = open('DIS_Predictions1.txt', 'w')

#percentage = 0
day = train_end-1
own = False
ActualEarned = 0
Earned = 0
y_true = []
y_pred = []
print("First: " + str(s[day]))
print("Last: " + str(s[0]))
while day > 0:
	clf2 = joblib.load('DIS_Model.pkl')
	X_p = []
	
	#PE_RAT_p = s[day]/(s[day]-s[day+365])
	#X_p.append(PE_RAT_p)
	
	Two_Day_p = s[day]-s[day+2]
	X_p.append(Two_Day_p)

	One_Day_p = s[day]-s[day+1]
	X_p.append(One_Day_p)

	Three_Day = s[day]-s[day+3]
	X_p.append(Three_Day)

	#Forty_Day_p = s[day]-s[day+44]
	#X_p.append(Forty_Day_p)
	
	VTY_slice_p = s[day:(day+10)]
	VTY_slice_p = VTY_slice_p.as_matrix()
	Volatility_p = np.var(VTY_slice_p)
	X_p.append(Volatility_p)

	#VTY_slice_44_p = s[(day):(day+44)]
	#VTY_slice_44_p = VTY_slice_44_p.as_matrix()
	#Volatility_44_p = np.var(VTY_slice_44_p)
	#X_p.append(Volatility_44_p)
	
	X_p.append(s_Volume[day])
	

	#i = day
	#while i <= day+5:
	#	slice_10_p = pd.Series(s[i:(i+10)])
	#	avg_p = np.mean(slice_10_p)
	#	X_p.append(avg_p)
	#	i += 1

	#i = day
	#while i <= day+5:
	#	slice_50_p = pd.Series(s[i:(i+50)])
	#	avg_p = np.mean(slice_50_p)
	#	X_p.append(avg_p)
	#	i += 1

	SVM_predict = np.array(X_p)
	profitloss = s[day-1]-s[day]
	length = SVM_predict.size
	SVM_new = np.reshape(SVM_predict, (1, length))
	prediction = clf2.predict(SVM_new)

	if prediction == 1:
		y_pred.append(1)
	else:
		y_pred.append(0)

	if profitloss > 0:
		y_true.append(1)
	else:
		y_true.append(0)



	ActualEarned = ActualEarned + s[day-1]-s[day]

	if prediction == 1:
		Earned = Earned + s[day-1]-s[day]
		if own == False:
			own = True
	if prediction == 0:
		if own == True:
			own = False


	update(day)
	
	f.write(str(profitloss))
	f.write(str(prediction))
	f.write('\n')
	day -= 1

print(stats.accuracy_score(y_true, y_pred))
print(str(ActualEarned))
print(str(Earned))

